from pyrogram import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.getenv('24486691'))
api_hash = os.getenv('ca0f67ba2c2cccb999f50d904cee9b63')

if not (api_id or api_hash):
    raise Exception('You have to pass both API_ID and API_HASH env variables')

app = Client("auto-reaction", api_id, api_hash)
