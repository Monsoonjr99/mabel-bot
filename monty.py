import sys
import discord
import os
PREFIX = 'm;'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('hello mabel'):
        await message.channel.send('Hello!')
    elif message.content.lower().startswith(PREFIX):
        await message.channel.send('test')

client.run(os.environ['BOT_TOKEN'])