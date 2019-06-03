import asyncio
import discord
from botCredentials import *
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print('-----------------------------')


@bot.command()
async def help(ctx):
    await ctx.message.author.send('Hi, i\'m unicornowl\'s Discord bot! My commands are:\n' +
                   ':unicorn:`!links` - Links to unicornowl\'s other pages!\n' +
                   ':unicorn:`!marketplace` - See what unicornowl is selling!\n' +
                   ':unicorn:`!donate` - unicornowl graciously accepts donations!\n' +
                   ':unicorn:`!hud` - Download unicornowl\'s TF2 HUD!\n' +
                   'Also available on unicornowl\'s Discord server:\n' +
                   ':owl:`!dab` - unicornowl do the dab!\n' +
                   ':owl:`!yeet` - Yah yeet!\n')


@bot.command()
async def donate(ctx):
    if isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.message.author.send(
            'If you would be so kind to donate, Kine would really appreciate it!\n' +
            '<https://twitch.streamlabs.com/unicornowl>')


@bot.command()
async def marketplace(ctx):
    if isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.message.author.send('unicornowl\'s marketplace: <https://marketplace.tf/shop/unicornowl>')


@bot.command()
async def hud(ctx):
    if isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.message.author.send('unicornowl uses ahud: <https://huds.tf/forum/showthread.php?tid=191>')


@bot.command()
async def links(ctx):
    if isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.message.author.send('Twitch: <http://twitch.tv/unicornowl>\n' +
                   'Twitter: <https://twitter.com/unicornowlkine>\n' +
                   'Instagram: <https://www.instagram.com/kristinelinneahl/>\n' +
                   'Youtube: <https://www.youtube.com/channel/UCupn_eVNhqY_AN2mSgdYIDQ?>\n' +
                   'Spotify Playlist: <https://open.spotify.com/user/mossepus123?si=M4377HBDTwyIygv-lGCI5g>\n' +
                   'Steam Group: <http://steamcommunity.com/groups/unicornOwl>\n' +
                   'Snapchat: kristinelinnea\n')


@bot.command()
async def yeet(ctx):
    if not isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.send('<:yeet:481453557866954753>')


@bot.command()
async def dab(ctx):
    if not isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.send('<:kinedab2:474552682271735819><:kinedab:392164919853711370>')


@bot.event
async def on_member_join(member):
    print('joined')


bot.run(TOKEN)
