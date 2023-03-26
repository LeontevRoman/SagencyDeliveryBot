import os

from dotenv import load_dotenv
from db.db import DataBase

load_dotenv()
TOKEN = os.getenv('TOKEN_SAGENCY_DELIVERY_BOT')

db = DataBase()

GROUP_NAME = "@test_test_groupt"
