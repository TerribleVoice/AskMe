import os
import logging

LOGGER_LEVEL = logging.INFO
PORT = os.getenv('PORT', 4554)

DB_CONFIG = {
    'name': os.getenv('POSTGRES_DB', 'AskMe'),
    'user': os.getenv('POSTGRES_USER', 'admin'),
    'password': os.getenv('POSTGRES_PASSWORD', 'test'),
    'host': os.getenv('POSTGRES_HOST', 'postgres'),
    'port': os.getenv('POSTGRES_PORT', '5432'),
}