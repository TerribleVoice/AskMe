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
                        CREATE TABLE IF NOT EXISTS {config.get('TABLES', 'TABLE_POSTS')} (
                            id uuid NOT NULL,
                            author_id uuid NOT NULL,
                            subscription_id uuid NOT NULL,
                            content text NOT NULL,
                            created_at timestamp without time zone NOT NULL,
                            price integer
                        );
                        """)
            self.connection.commit()
            
            cursor.execute(f"""
                        CREATE TABLE IF NOT EXISTS {config.get('TABLES', 'TABLE_SUBSCRIPTIONS')} (
                            id uuid NOT NULL,
                            author_id uuid NOT NULL,
                            price int NOT NULL,
                            name varchar NOT NULL,
                            description varchar NOT NULL,
                            parent_subscription_id uuid NULL,
                            CONSTRAINT subscriptions_pk PRIMARY KEY (id),
                            CONSTRAINT subscriptions_fk FOREIGN KEY (author_id) REFERENCES public.users(id)
                        );
                        """)
            self.connection.commit()
            
            cursor.execute(f"""   
                        CREATE TABLE IF NOT EXISTS {config.get('TABLES', 'TABLE_USER_SUBSCRIPTION')} (
                            id uuid NOT NULL,
                            user_id uuid NOT NULL,
                            subscription_id uuid NOT NULL,
                            CONSTRAINT user_subscription_pk PRIMARY KEY (id),
                            CONSTRAINT user_subscription_fk FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE SET NULL,
                            CONSTRAINT user_subscription_fk_1 FOREIGN KEY (subscription_id) REFERENCES public.subscriptions(id)
                        );
                        """)
            
            cursor.execute(f"""
                        CREATE TABLE IF NOT EXISTS {config.get('TABLES', 'TABLE_ACTIVE')} (
                            id_telegram BIGINT NOT NULL,
                            id_user uuid,
                            FOREIGN KEY (id_user) REFERENCES {config.get('TABLES', 'TABLE_USERS')}(id)
                        );
                        """)
            self.connection.commit()
            
            
    def delete_tables(self):
        with self.connection.cursor() as cursor:
            cursor.execute(f'''DROP TABLE {config.get('TABLES', 'TABLE_USERS')} CASCADE;
                               DROP TABLE {config.get('TABLES', 'TABLE_POSTS')} CASCADE;
                               DROP TABLE {config.get('TABLES', 'TABLE_USER_SUBSCRIPTION')} CASCADE;
                               DROP TABLE {config.get('TABLES', 'TABLE_ACTIVE')} CASCADE;
                               DROP TABLE {config.get('TABLES', 'TABLE_SUBSCRIPTIONS')} CASCADE;
                            ''')
            
            self.connection.commit()
            self.close()
            
    # Сверяем логин и пароль
    def check_auth(self, login, password):
        with self.connection.cursor() as cursor:
            select = f"""
            SELECT id
            FROM {config.get('TABLES', 'TABLE_USERS')}
            WHERE login = {repr(login)} AND password = {repr(password)}                     
            """

            cursor.execute(select)
            result = cursor.fetchall()
            return result
    
    # Проверка на активный сеанс
    def check_user_active(self, telegram_id: int):
        with self.connection.cursor() as cursor:
            select = f"""
            SELECT id_user
            FROM {config.get('TABLES', 'TABLE_ACTIVE')}
            WHERE id_telegram = {telegram_id}           
            """

            cursor.execute(select)
            result = cursor.fetchall()
            return result
        
    # Добавление активного сеанса
    def add_user_active(self, telegram_id, user_id):
        with self.connection.cursor() as cursor:
            insert = f"""
            INSERT INTO {config.get('TABLES', 'TABLE_ACTIVE')} (id_telegram, id_user)
            VALUES ({telegram_id}, {repr(user_id)})
            """
            
            cursor.execute(insert)
            self.connection.commit()
            
    # Удаление активного сеанса
    def delete_user_active(self, telegram_id: int):
        with self.connection.cursor() as cursor:
            delete = f"""
            DELETE FROM {config.get('TABLES', 'TABLE_ACTIVE')}
            WHERE id_telegram = {telegram_id}
            """
            
            cursor.execute(delete)
            self.connection.commit()
            
    # Поиск пользователя 
    def seacrh_user(self, nickname):
        with self.connection.cursor() as cursor:
            select = f"""
            SELECT *
            FROM {config.get('TABLES', 'TABLE_SUBSCRIPTIONS')}
            WHERE name = {repr(nickname)}           
            """

            cursor.execute(select)
            result = cursor.fetchall()
            return result
    
    # Поиск пользователей, похожих на пользователя
    def search_many_user(self, nickname):
        with self.connection.cursor() as cursor:
            select = f"""
            SELECT * FROM {config.get('TABLES', 'TABLE_SUBSCRIPTIONS')} 
            WHERE name LIKE {repr(nickname)+repr('%')}
            """
            
            cursor.execute(select)
            result = cursor.fetchall()
            return result
    
    # Проверка, подписан ли пользователь на автора
    def check_user_subscription(self, user_id, subscription_id):
        with self.connection.cursor() as cursor:
            select = f"""
            SELECT * FROM {config.get('TABLES', 'TABLE_USER_SUBSCRIPTION')}
            WHERE user_id = {repr(user_id)} AND subscription_id = {repr(subscription_id)}
            """
            
            cursor.execute(select)
            result = cursor.fetchall()
            return result
    
    # Узнать id автора
    def get_author_id(self, nickname):
        with self.connection.cursor() as cursor:
            select = f"""
            SELECT * FROM {config.get('TABLES', 'TABLE_SUBSCRIPTIONS')}
            WHERE name = {repr(nickname)};
            """
            
            cursor.execute(select)
            result = cursor.fetchall()
            return result
        
    # Получить все подписки пользователя
    def get_all_subscriptions(self, user_id):
        with self.connection.cursor() as cursor:
            select = f"""
            SELECT * FROM {config.get('TABLES', 'TABLE_USER_SUBSCRIPTION')}
            WHERE user_id = {repr(user_id)};
            """
            
            cursor.execute(select)
            result = cursor.fetchall()
            return result
        
    # Получить информацию о блогере
    def get_info_subs(self, sub_id):
        with self.connection.cursor() as cursor:
            select = f"""
            SELECT * FROM {config.get('TABLES', 'TABLE_SUBSCRIPTIONS')}
            WHERE id = {repr(sub_id)};
            """
            
            cursor.execute(select)
            result = cursor.fetchall()
            return result
            
db = Database(db_name=config_db_name,
              db_user=config_db_user,
              db_password=config_db_name_password)

db.create_tables()