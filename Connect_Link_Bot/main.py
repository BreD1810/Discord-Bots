import discord
import asyncio
import re


#Start the discord client
client = discord.Client()

#Print to console to show the bot is starting
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------------------------')

#Runs when a message is sent to discord channel the bot can see
@client.event
async def on_message(message):
    #Test case
    if message.content.startswith('!connectPing'):
        await client.send_message(message.channel, 'connectPong')
        
    #Stop the bot spamming if it sees its own messages.
    if message.author == client.user:
        return

    #Checks if there is a match using regex
    p = re.compile("connect\s*(\S+)\s*;\s*password\s*(\S+)").match(message.content)
    #Run if there is a match.
    if p:
        groups = p.groups()
        await client.send_message(message.channel, "steam://connect/" + groups[0] + "/" + groups[1])

client.run('<token here>', bot=True)
