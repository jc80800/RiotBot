# bot.py
"""
Main file for the bot for Discord. 
Handles all the events and post accordingly
"""
import os

import discord
from dotenv import load_dotenv
import api_call

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

"""
Event handler for new messages posted
"""
@client.event
async def on_message(message):
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds) # finds the guild matching GUILD

    if message.author == client.user:
        return
    
    message_field = message.content.split()
    if not message_field[0] == "!riot":
        return

    text = parse(message_field)
    if isinstance(text, str):
        await message.channel.send(text)
    else:
        await message.channel.send(embed=text)

"""
Parses User messages and calls function accordingly
"""
def parse(message_field):
    game = message_field[1]
    if game not in ["!lol"]:
        return f"Incorrect command, {game} is not a proper notation"
    
    attribute = message_field[2]
    if attribute not in ["!summoner", "!champion", "!start", "!guess"]:
        return f"Incorrect command, {attribute} is not a proper notation"
    

    return api_call.get_api(message_field)
    
client.run(TOKEN)