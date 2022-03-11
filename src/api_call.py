import os
from dotenv import load_dotenv

from riotwatcher import LolWatcher, ApiError
import lol_calls

load_dotenv()
API_KEY = os.getenv('API_KEY')
lol_watcher = LolWatcher(API_KEY)
NA_REGION = 'na1'
data_dragon_version = lol_watcher.data_dragon.versions_for_region(NA_REGION)

def get_api(game, attribute, value):
    if game == "!lol":
        return get_lol_content(attribute, value)
    

def get_lol_content(attribute, value):
    if attribute == "!summoner":
        return lol_calls.get_summoner_info(lol_watcher, NA_REGION, value)



