import sys
import discord
import os
import random
PREFIX = 'm;'
VERSION = 'v20190731a'

random.seed()

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
            await message.channel.send('My version is {}'.format(VERSION))
        elif cmd=='hype':
            await message.channel.send('Hype is a subtropical depression!')
        elif cmd=='monsoon':
            mintiness = random.random()
            if mintiness<0.0005:
                mintiness = 0
            else:
                mintiness = random.randrange(1,100)
            await message.channel.send('A very silly person who is currently {}% high on mints'.format(mintiness))
        elif cmd=='sm':
            await message.channel.send('Dipper')

client.run(os.environ['BOT_TOKEN'])