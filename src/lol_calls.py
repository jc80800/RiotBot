"""
Main file for handling League of Legend API calls
"""
import os
import discord
import random 
import pymongo
from dotenv import load_dotenv

load_dotenv()
MONGOPASS = os.getenv('MONGOPASS')
client = pymongo.MongoClient(f"mongodb+srv://mongodbjc:{MONGOPASS}@cluster0.jbrvv.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.riot

"""
Grabs Summoner information on each name given and returns an embed message
"""
def get_summoner_info(lolwatcher, region, name):
    summoner_stat = lolwatcher.summoner.by_name(region, name)
    profile_icon = get_profile_icon(summoner_stat['profileIconId'])
    ranked_info = lolwatcher.league.by_summoner(region, summoner_stat['id'])
    if not ranked_info:
        return generate_embed(summoner_stat, profile_icon, False)
    else:
        return generate_embed(summoner_stat, profile_icon, ranked_info)

"""
Grabs the profile icon image
"""
def get_profile_icon(id):
    return f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/profile-icons/{id}.jpg"

"""
Grabs the ranked icon
"""
def get_ranked_icon(rank):
    return f"https://raw.communitydragon.org/latest/plugins/rcp-fe-lol-shared-components/global/default/{rank}.png"

"""
Generates an discord embed message for a specific user
"""
def generate_embed(stat, profile_icon, ranked_info):
    name = stat['name']
    level = stat['summonerLevel']
    embedVar = discord.Embed(title=name, color=0x00ff00)
    embedVar.add_field(name="Summoner Level: ", value=level, inline=False)
    embedVar.set_thumbnail(url=profile_icon)
    if ranked_info:
        ranked_icon = get_ranked_icon(ranked_info[0]['tier'].lower())
        embedVar.add_field(name="Wins: ", value=ranked_info[0]['wins'])
        embedVar.add_field(name="Losses: ", value=ranked_info[0]['losses'])
        embedVar.set_image(url=ranked_icon)
    else:
        embedVar.add_field(name="Ranked Stat", value="No Ranked Stats Found")
    return embedVar

"""
Starts up a mini-game to guess champion's title
"""
def start_guess_game(lolwatcher, region):
    versions = lolwatcher.data_dragon.versions_for_region(region) 
    champions_version = versions['n']['champion']
    current_champ_list = lolwatcher.data_dragon.champions(champions_version)

    randomChamp = random.choice(list(current_champ_list['data'].keys()))
    champTitle = current_champ_list['data'][randomChamp]['title']

    guessDoc = db.game.find_one({"MainGuess" : True})
    db.game.update_one(guessDoc, {'$set' : {"name" : randomChamp}})

    newEmbed = discord.Embed(title="League Of Legend Champion Titles", color=0x0000ff)
    newEmbed.add_field(name="Title: ", value=champTitle)
    return newEmbed

"""
A guess made by user on the above game
"""
def guess_champ(guess):
    guessDoc = db.game.find_one({"MainGuess" : True})
    if guessDoc["name"] == None:
        return "No Guess Game Started, Try !start"
    else:
        if guess == guessDoc["name"]:
            db.game.update_one(guessDoc, {'$set' : {"name" : None}})
            return "Correct!"
        else:
            return "Incorrect!"
    
def get_champion_info(lolwatcher, champion):
    pass


