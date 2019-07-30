import sys
import discord
import os
PREFIX = 'm;'
VERSION = 'v20190730a'

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
        cmd = message.content[len(PREFIX):].split()
        args = cmd[1:]
        cmd = cmd[0].lower()
        if cmd=='version':
            await message.channel.send('My version is ',VERSION)
        elif cmd=='hype':
            await message.channel.send('Hype is a subtropical depression!')
        elif cmd=='monsoon':
            await message.channel.send('A silly person')

client.run(os.environ['BOT_TOKEN'])