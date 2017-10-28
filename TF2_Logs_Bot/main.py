import discord
import asyncio
import urllib.request
import json
import math
import bs4
import requests
from selenium import webdriver
from PIL import Image

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
    if message.content.startswith('!logPing'):
        await client.send_message(message.channel, 'logPong')

    #Actual log stuff 
    if message.content.startswith('http://logs.tf/'):
        #get json data from log
        usersMessage = str(message.content)
        position = usersMessage.find("http://logs.tf")
        logUrlNumber = usersMessage[position+15:position+22]
        response = urllib.request.urlopen('http://logs.tf/json/' + str(logUrlNumber))
        data = json.loads(response.read())

        #Webscrape for name of log and map
        webCode = requests.get('http://logs.tf/' + logUrlNumber)
        webCode = bs4.BeautifulSoup(webCode.text, 'html.parser')
        logName = webCode.find(id = 'log-name').get_text()
        logMap = webCode.find(id = 'log-map').get_text()

        
        #calculate length of game.
        time = data['length']
        timeMinutes = math.floor(time / 60)
        timeSeconds = time % 60
       
                
        #send text messages
        if data['teams']['Red']['score'] > data['teams']['Blue']['score']:
            await client.send_message(message.channel, '```' + str(logName) + '\n' +\
                                      'Map: ' + logMap + '.\n' +\
                                      'Time: ' + str(timeMinutes) + ':' + str(timeSeconds) + '.\n' +\
                                      'RED won with ' + str(data['teams']['Red']['score']) + ' points, ' + str(data['teams']['Red']['kills']) + ' kills and ' + str(data['teams']['Red']['dmg']) + ' damage.\n' +\
                                      'BLU lost with ' + str(data['teams']['Blue']['score']) + ' points, ' + str(data['teams']['Blue']['kills']) + ' kills and ' + str(data['teams']['Blue']['dmg']) + ' damage.```')
        elif data['teams']['Red']['score'] == data['teams']['Blue']['score']:
            await client.send_message(message.channel, '```' + str(logName) + '\n' +\
                                      'Map: ' + logMap + '.\n' +\
                                      'Time: ' + str(timeMinutes) + ':' + str(timeSeconds) + '.\n' +\
                                      'The game was a tie.\n'+\
                                      'BLU scored ' + str(data['teams']['Blue']['score']) + ' points, ' + str(data['teams']['Blue']['kills']) + ' kills and ' + str(data['teams']['Blue']['dmg']) + ' damage.\n' +\
                                      'RED scored ' + str(data['teams']['Red']['score']) + ' points, ' + str(data['teams']['Red']['kills']) + ' kills and ' + str(data['teams']['Red']['dmg']) + ' damage.```')
        else:
            await client.send_message(message.channel, '```' + str(logName) + '\n' +\
                                      'Map: ' + logMap + '.\n' +\
                                      'Time:' + str(timeMinutes) + ':' + str(timeSeconds) + '.\n' +\
                                      'BLU won with ' + str(data['teams']['Blue']['score']) + ' points, ' + str(data['teams']['Blue']['kills']) + ' kills and ' + str(data['teams']['Blue']['dmg']) + ' damage.\n' +\
                                      'RED lost with ' + str(data['teams']['Red']['score']) + ' points, ' + str(data['teams']['Red']['kills']) + ' kills and ' + str(data['teams']['Red']['dmg']) + ' damage.```')
        #Get website screenshot
        driver = webdriver.PhantomJS()
        driver.get('http://logs.tf/' + logUrlNumber)
        driver.save_screenshot('log.png')
        driver.quit()

        #edit image
        im = Image.open('log.png')
        im = im.crop((0,370,1000,850))#im = im.crop((left, top, right, bottom))
        im.save('log.png')

        #send image
        await client.send_file(message.channel, 'log.png')
client.run('<token here>', bot=True)
