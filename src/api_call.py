"""
Main file for API management calls
"""
import os
from dotenv import load_dotenv

from riotwatcher import LolWatcher, ApiError
import lol_calls

load_dotenv()
API_KEY = os.getenv('API_KEY')
lol_watcher = LolWatcher(API_KEY)
NA_REGION = 'na1'
data_dragon_version = lol_watcher.data_dragon.versions_for_region(NA_REGION)

"""
Parses the content more throughly for detailed game and call function accordingly
"""
def get_api(message_field):
    game = message_field[1]
    attribute = message_field[2]
    if game == "!lol":
        return get_lol_content(attribute, message_field)
    
"""
Main function call for League of Legend content call
"""
def get_lol_content(attribute, message_field):
    if attribute == "!summoner":
        value = message_field[3]
        return lol_calls.get_summoner_info(lol_watcher, NA_REGION, value)
    
    elif attribute == "!champion":
        value = message_field[3]
        return lol_calls.get_champion_info(lol_watcher, value)
    
    elif attribute == "!start":
        return lol_calls.start_guess_game(lol_watcher, NA_REGION)
    
    elif attribute == "!guess":
        return lol_calls.guess_champ(message_field[3])



