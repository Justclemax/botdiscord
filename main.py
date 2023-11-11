import os
import discord
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)











client.run(os.getenv("TOKEN"))