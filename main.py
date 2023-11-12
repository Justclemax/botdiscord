import os
import discord
from dotenv import load_dotenv


load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)







if __name__ =="__main__":

    client.run(os.getenv("TOKEN"))