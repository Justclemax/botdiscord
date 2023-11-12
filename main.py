import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f" {client.user.name} est en ligne ")
@client.event
async def on_message(message : discord.message):
    
    if message.author.bot == True:
        return
    
    if "hello" in message.content:
        await message.channel.send('hello')


    



if __name__ =="__main__":

    client.run(os.getenv("TOKEN"))