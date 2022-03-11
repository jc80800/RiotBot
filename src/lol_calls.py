from riotwatcher import LolWatcher, ApiError
import discord

def get_summoner_info(lolwatcher, region, name, data_dragon):
    summoner_stat = lolwatcher.summoner.by_name(region, name)
    profile_icon = get_profile_icon(summoner_stat['profileIconId'])
    return generate_embed(summoner_stat, profile_icon)

def get_profile_icon(id):
    return f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/profile-icons/{id}.jpg"

def generate_embed(stat, profile_icon):
    name = stat['name']
    level = stat['summonerLevel']
    embedVar = discord.Embed(title=name, color=0x00ff00)
    embedVar.add_field(name="Summoner Level: ", value=level, inline=False)
    embedVar.set_thumbnail(url=profile_icon)
    return embedVar
