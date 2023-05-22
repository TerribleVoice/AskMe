import psycopg2 
import configparser

config = configparser.ConfigParser()
config.read('C:\\Users\\Gorob\\Desktop\\bot\\settings\\config.ini')

config_db_name = config.get('DATABASE', 'NAME_DB')
config_db_user = config.get('DATABASE', 'USER_DB')
config_db_name_password = config.get('DATABASE', 'PASSWORD_DB')

class Database:
    def __init__(self, db_name, db_user, db_password, db_host=None, db_port=None):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.connection = psycopg2.connect(database=self.db_name, user=self.db_user, password=self.db_password)
    
    def check_connection(self):
        return self.connection
            
    def close(self):
        self.connection.close()
        
    def create_tables(self):
        with self.connection.cursor() as cursor:
            cursor.execute(f"""                           
                        CREATE TABLE IF NOT EXISTS {config.get('TABLES', 'TABLE_USERS')} (
                            id uuid NOT NULL,
                            login varchar NOT NULL,
                            email varchar NULL,
                            "password" varchar NOT NULL,
                            qiwi_token varchar NULL,
                            "description" text NULL,
                            links text NULL,
                            CONSTRAINT users_pk PRIMARY KEY (id)
                        );
                        """)
            self.connection.commit()
            cursor.execute(f"""
                        CREATE TABLE {config.get('TABLES', 'TABLE_POSTS')} (
                            id uuid NOT NULL,
                            author_id uuid NOT NULL,
                            subscription_id uuid NOT NULL,
                            content text NOT NULL,
                            created_at timestamp without time zone NOT NULL,
                            price integer
                        );
                        """)
            self.connection.commit()
            
    def delete_tables(self):
        with self.connection.cursor() as cursor:
            cursor.execute(f'''DROP TABLE {config.get('TABLES', 'TABLE_USERS')} CASCADE;
                               DROP TABLE {config.get('TABLES', 'TABLE_POSTS')} CASCADE;''')
            
            self.connection.commit()
            self.close()
            
db = Database(db_name=config_db_name,
              db_user=config_db_user,
              db_password=config_db_name_password)

db.create_tables()