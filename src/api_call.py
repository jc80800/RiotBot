import os
import requests
import json
from dotenv import load_dotenv

from riotwatcher import LolWatcher, ApiError

load_dotenv()
API_KEY = os.getenv('API_KEY')
lol_watcher = LolWatcher(API_KEY)
NA_REGION = 'na1'

def get_simple_api(message_content):
    pass

