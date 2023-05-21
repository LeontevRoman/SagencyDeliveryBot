import os

from dotenv import load_dotenv
from db.db import DataBase

load_dotenv()
TOKEN = os.getenv('TOKEN_SAGENCY_DELIVERY_BOT')
TEST_TOKEN = os.getenv('TOKEN_TEST_BOT')

DOMAIN = os.getenv('DOMAIN')

WEBHOOK_DOMAIN = f'https://{DOMAIN}'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_DOMAIN}{WEBHOOK_PATH}'

APP_HOST = 'localhost'
APP_PORT = 8080

db = DataBase()

GROUP_NAME = "@sagencydelivery"
