from riotwatcher import LolWatcher, ApiError
import discord

def get_summoner_info(lolwatcher, region, name):
    summoner_stat = lolwatcher.summoner.by_name(region, name)
    profile_icon = get_profile_icon(summoner_stat['profileIconId'])
    ranked_info = lolwatcher.league.by_summoner(region, summoner_stat['id'])
    if not ranked_info:
        return generate_embed(summoner_stat, profile_icon, False)
    else:
        return generate_embed(summoner_stat, profile_icon, ranked_info)

def get_profile_icon(id):
    return f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/profile-icons/{id}.jpg"

def get_ranked_icon(rank):
    return f"https://raw.communitydragon.org/latest/plugins/rcp-fe-lol-shared-components/global/default/{rank}.png"

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