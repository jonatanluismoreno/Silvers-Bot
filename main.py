import discord
from discord import message

client = discord.Client()

tolerance = 0
LIMIT = 2


# Events
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('oli')
    
    if message.content.startswith('https://'):
        tolerance=+1
        print(tolerance)
        print(message.content)
        if tolerance == LIMIT or tolerance > LIMIT:
            await message.channel.send('Tranqui, manito {0.user}'.format(message.author))


client.run('TOKEN')

