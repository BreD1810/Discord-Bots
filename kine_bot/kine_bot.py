import asyncio
import discord
from botCredentials import *
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print('-----------------------------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(TOKEN)