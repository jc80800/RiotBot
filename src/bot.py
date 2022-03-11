# bot.py
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

@client.event
async def on_message(message):
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds) # finds the guild matching GUILD

    if message.author == client.user:
        return
    
    #await message.channel.send(api_call.get_simple_api(message.content))
    

client.run(TOKEN)