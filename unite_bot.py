import discord
from discord.ext.commands import Bot
import config
import pint
import unite

client = discord.Client()

TOKEN = config.token

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content == "!u":
        return

    elif message.content.startswith("!u"):

        output = unite.convertInput(message.content)

        #need abbreviated format for temperatures
        if output.dimensionality == "[temperature]":
            await message.channel.send("{:~P}".format(output))
            
        else:
            await message.channel.send("{:P}".format(output))

client.run(TOKEN)
