import discord
from discord.ext.commands import Bot
import config
import pint
import unite
import hyperlink

TOKEN = config.token

bot_tag = "!u"

client = Bot(command_prefix=bot_tag)
client.remove_command("help")

pink = discord.Color.from_rgb(36, 133, 201)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content == bot_tag:
        return

    elif message.content == bot_tag + " help" or message.content == bot_tag + " h":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = """\
            Ask me to convert stuff like this: ```!u [value] [unit1] to [unit2] (rounder)```The rounder is optional, and defaults to 2 decimal places.
            Example Input: ```!u 10 m to cm```Output: ```1000.0 centimeter```
            """,
            color = pink
        )
        embed.add_field(name="Unit Type", value="""\
        Time Zone
        Angle
        Length/Distance
        Mass/Weight
        Time
        Temperature
        Area
        Volume
        Velocity
        Acceleration
        Energy
        Density
        ...and more!""", inline=True)
        embed.add_field(name="Help Command", value="""\
        `!u h(elp) timezone`
        `!u h(elp) angle`
        `!u h(elp) length/distance`
        `!u h(elp) mass/weight`
        `!u h(elp) time`
        `!u h(elp) temperature`
        `...you get the idea.`""", inline=True)

        embed.add_field(name="Sources", value="`!u sources`", inline=False)

        await message.channel.send(embed=embed)
    elif message.content == bot_tag + " help timezone" or message.content == bot_tag + " h timezone":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = """\
            I can convert times to different time zones!
            Example Input: ```!u 10:30 am est to pst```Output: ```7:30 AM```
            If you don't include AM/PM, I will use 24 hour time. There are some time zones that share abbreviations. Below are all of them listed, along with how to use them with me.""",
            color = pink
        )
        embed.add_field(name="Time Zone Name", value="""\
            Arabia Daylight Time (ADT)
            Atlantic Daylight TIme (ADT)
            Amazon Summer Time (AMST)
            Armenia Summer Time (AMST)
            Amazon Time (AMT)
            Armenia Time (AMT)
            Arabia Standard Time (AST)
            Atlantic Standard Time (AST)
            Bangladesh Standard Time (BST)
            Bougainville Standard Time (BST)
            British Summer Time (BST)
            Central Daylight Time (CDT)
            Cuba Daylight Time (CDT)
            Central Standard Time (CST)
            China Standard Time (CST)
            Cuba Standard Time (CST)
            Gulf Standard Time (GST)
            South Georgia Time (GST)
            India Standard Time (IST)
            Irish Standard Time (IST)
            Israel Standard Time (IST)
            Paraguay Time (PYT)
            Pyongyang Time (PYT)
            West Samoa Time (WST)
            Western Sahara Summer Time (WST)
            """, inline=True)
        embed.add_field(name="Abbreviation", value="""\
            ADT-UTC+4
            ADT-UTC-3
            AMST-UTC-3
            AMST-UTC+5
            AMT-UTC-4
            AMT-UTC+4
            AST-UTC+3
            AST-UTC-4
            BST-UTC+6
            BST-UTC+11
            BST-UTC+1
            CDT-UTC-5
            CDT-UTC-4
            CST-UTC-6
            CST-UTC+8
            CST-UTC-5
            GST-UTC+4
            GST-UTC-2
            IST-UTC+5:30
            IST-UTC+1
            IST-UTC+2
            PYT-UTC-4
            PYT-UTC+8:30
            WST-UTC+14
            WST-UTC+1
            """, inline=True)
            
        await message.channel.send(embed=embed)
    elif message.content == bot_tag + " help angle" or message.content == bot_tag + " h angle":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = """\
            I can convert angle measurements! 
            Example Input: ```!u pi radians to degrees```Output: ```180.0 degree```""",
            color = pink
        )
        await message.channel.send(embed=embed)
    elif message.content == bot_tag + " help length" or message.content == bot_tag + " h length" or message.content == bot_tag + " help distance" or message.content == bot_tag + " h distance":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = """\
            I can convert length/distance measurements! 
            Example Input: ```!u 12 m to in 3```Output: ```472.441 inch```""",
            color = pink
        )
        await message.channel.send(embed=embed)
    elif message.content == bot_tag + " help mass" or message.content == bot_tag + " h mass" or message.content == bot_tag + " help weight" or message.content == bot_tag + " h weight":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = """\
            I can convert mass/weight measurements! 
            Example Input: ```!u 52 tons to kg 5```Output: ```47173.60648 kilogram```""",
            color = pink
        )
        await message.channel.send(embed=embed)
    elif message.content == bot_tag + " help time" or message.content == bot_tag + " h time":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = """\
            I can convert time measurements! 
            Example Input: ```!u 1 minute to attoseconds```Output: ```5.999999999999999×10¹⁹ attosecond```""",
            color = pink
        )
        await message.channel.send(embed=embed)
    elif message.content == bot_tag + " help temperature" or message.content == bot_tag + " h temperature":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = """\
            I can convert temperature measurements! 
            Example Input: ```!u 32 degF to degC```Output: ```0.0 °C```""",
            color = pink
        )
        await message.channel.send(embed=embed)
    elif message.content == bot_tag + " help area" or message.content == bot_tag + " h area":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = """\
            I can convert area measurements! 
            Example Input: ```!u 14 square meters to square feet```Output: ```150.69 foot²```""",
            color = pink
        )
        await message.channel.send(embed=embed)
    elif message.content == bot_tag + " help volume" or message.content == bot_tag + " h volume":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = """\
            I can convert volume measurements! 
            Example Input: ```!u 10 gallons to pints```Output: ```80.0 pint```""",
            color = pink
        )
        await message.channel.send(embed=embed)
    elif message.content == bot_tag + " help velocity" or message.content == bot_tag + " h velocity":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = """\
            I can convert velocity measurements! 
            Example Input: ```!u 120 km/hr to miles/hr 7```Output: ```74.5645431 mile/hour```""",
            color = pink
        )
        await message.channel.send(embed=embed)
    elif message.content == bot_tag + " help acceleration" or message.content == bot_tag + " h acceleration":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = """\
            I can convert acceleration measurements! 
            Example Input: ```!u 120 km/hr squared to miles/hr squared 7```Output: ```74.5645431 mile/hour²```""",
            color = pink
        )
        await message.channel.send(embed=embed)
    elif message.content == bot_tag + " help energy" or message.content == bot_tag + " h energy":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = """\
            I can convert energy measurements! 
            Example Input: ```!u 2100 kcal to joules```Output: ```8786400.0 joule```""",
            color = pink
        )
        await message.channel.send(embed=embed)
    elif message.content == bot_tag + " help density" or message.content == bot_tag + " h density":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = """\
            I can convert density measurements! 
            Example Input: ```!u g/cm**3 to kg/m**3```Output: ```1000.0 kilogram/meter³```""",
            color = pink
        )
        await message.channel.send(embed=embed)
    elif message.content == bot_tag + " sources":
        embed = discord.Embed(
            title = "UniteBot Helper",
            description = "I primarily use the Pint Python unit conversion library to help you convert units. Links to this and more can be found below.",
            color = pink
        )
        embed.add_field(name = "Logo Artist: algooddevils", value = hyperlink.parse("https://twitter.com/algooddevils"), inline=False)
        embed.add_field(name = "Pint", value = hyperlink.parse("https://pint.readthedocs.io/en/0.11/"), inline=False)
        embed.add_field(name = "Time Zone Data", value = hyperlink.parse("https://www.timeanddate.com/time/zones/"), inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith(bot_tag):

        output = unite.convertInput(message.content)

        #check if time zone conversion
        try:
            if ':' in output:
                await message.channel.send(output)
        except:
            print("Not a time zone conversion.")
        #need abbreviated format for temperatures
        if output.dimensionality == "[temperature]":
            await message.channel.send("{:~P}".format(output))

        else:
            await message.channel.send("{:P}".format(output))

client.run(TOKEN)