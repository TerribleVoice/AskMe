import os

TG_TOKEN = os.getenv('TG_TOKEN', '1234')

DB_CONFIG = {
    'name': os.getenv('POSTGRES_DB', 'AskMe'),
    'user': os.getenv('POSTGRES_USER', 'admin'),
    'password': os.getenv('POSTGRES_PASSWORD', 'test'),
    'host': os.getenv('POSTGRES_HOST', 'postgres'),
    'port': os.getenv('POSTGRES_PORT', '5432'),
}
