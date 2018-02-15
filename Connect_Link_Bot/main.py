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

    
    if message.content.startswith('connect '):
        tempMsg = str.replace(message.content, 'connect ');
        temp = temMsg.partition(";password ")
        if temp[2].startswith('"') and temp[2].endswith('"'):
            temp[2] = temp[2].lstrip('"')
            temp[2] = temp[2].rstrip('"')
            
        await client.send_message(message.channel, "steam://connect/" + temp[0] + "/" + temp[2])
        
client.run('<token here>', bot=True)
