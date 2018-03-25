import discord
import asyncio
import urllib.request
import bs4
import requests
from selenium import webdriver

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
    if message.content.startswith('!centerPing'):
        await client.send_message(message.channel, 'centerPong')

    #Actual log stuff 
    if message.content.startswith('https://tf2center.com/lobbies') or message.content.startswith('http://tf2center.com/lobbies'):
        #Get lobby URL
        usersMessage = str(message.content)
        position = usersMessage.find("tf2center.com/lobbies")
        lobbyNumber = usersMessage[position+22:position+28]

        #Get the webpage
        webPage = requests.get("http://tf2center.com/lobbies/" + lobbyNumber)
        webPage = bs4.BeautifulSoup(webPage.text, 'html.parser')
        
        #Send message if the lobby does not exist
        if "TF2Center - lobbies" in str(webPage.title):
            await client.send_message(message.channel, "```Error getting lobby information - lobby is now closed.```")
        else:
            #Get data
            tableElements = webPage.find_all("td")
                
            #Map
            map = tableElements[1].find("a")
            map = str(map)[str(map).find(">")+1:str(map).find("</a>")]

            #Gamemode
            headings = webPage.find_all("h1")
            gamemode = headings[1]
            gamemode = str(gamemode)[str(gamemode).find(">")+1:str(gamemode).find("</h1>")]

            #Config
            config = tableElements[3]
            config = str(config)[str(config).find(">")+1:str(config).find("</td>")]

            #Mumble required
            if "bright-green" in str(tableElements[9]):
                mumble = "true"
            else:
                mumble = "false"

            #Offclassing
            if gamemode == "6v6":
                otherInfo = webPage.find_all("span", class_="getQuickHelp")
                if "Any player" in str(otherInfo[2]):
                    offclassing = "true"
                else:
                    offclassing = "false"

            #Send the message   
            if gamemode == "6v6":
                response = "```Map: " + str(map) + '\n' + "Gamemode: " + gamemode + '\n' + "Config: " + config + '\n' + "Offclassing enabled: " + offclassing + '\n' + "Mumble required: " + mumble + "```"
            else:
                response = "```Map: " + str(map) + '\n' + "Gamemode: " + gamemode + '\n' + "Config: " + config + '\n' + "Mumble required: " + mumble + "```"

            await client.send_message(message.channel, response)

client.run(BOTTOKENHERE, bot=True)
