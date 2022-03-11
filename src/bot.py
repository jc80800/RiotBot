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
    
    message_field = message.content.split()
    if not message_field[0] == "!riot":
        return

    text = parse(message_field)
    await message.channel.send(embed=text)

def parse(message_field):
    game = message_field[1]
    if game not in ["!lol"]:
        return f"Incorrect command, {game} is not a proper notation"
    
    attribute = message_field[2]
    if attribute not in ["!summoner"]:
        return f"Incorrect command, {attribute} is not a proper notation"
    
    return api_call.get_api(game, attribute, message_field[3])
    
client.run(TOKEN)