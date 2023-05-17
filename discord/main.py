import discord
from discord.ext import commands
import json
import requests
import re

with open("config.json") as f:
    config = json.load(f)
token = str(config.get("token"))
channel = int(config.get("channel"))
path = str(config.get("path"))
key = str(config.get("key"))

intents = discord.Intents.all()
client = commands.Bot(command_prefix="TelegramEmppux",intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print(f"Connected -> {client.user.name}")

@client.event
async def on_message(message):
    if message.channel.id == channel:
        content = message.content
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,message.content)
        urls = [x[0] for x in url]
        if len(urls) > 0:
            await message.delete()
        if len(content) < 26:
            user = message.author.name
            r = requests.post(f"{path}?key={key}&user={user}&message={content}")
            print("[" + str(user) + "]" + " - " + "[" + str(content) + "]")

client.run(token)