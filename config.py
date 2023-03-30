import os

from dotenv import load_dotenv
from db.db import DataBase

load_dotenv()
TOKEN = os.getenv('TOKEN_SAGENCY_DELIVERY_BOT')
DOMAIN = os.getenv('DOMAIN')

WEBHOOK_DOMAIN = f'https://{DOMAIN}'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_DOMAIN}{WEBHOOK_PATH}'

APP_HOST = '0.0.0.0'
APP_PORT = os.getenv('PORT', default=9000)

db = DataBase()

GROUP_NAME = "@test_test_a"
