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
    await ctx.message.author.send('Hi, i\'m Unicornowl\'s discord bot! My commands are:\n' +
                   ':unicorn:`!links` - Links to Unicornowl\'s other pages!\n' +
                   ':unicorn:`!marketplace` - See what Unicornowl is selling!\n' +
                   ':unicorn:`!donate` - Unicornowl graciously accepts donations!\n' +
                   ':unicorn:`!hud` - Download Unicornowl\'s TF2 HUD!\n' +
                   'Also available on Unicornowl\'s Discord server:\n' +
                   ':owl:`!dab` - Unicornowl do the dab!\n' +
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
        await ctx.message.author.send('Unicornowl\'s marketplace: <https://marketplace.tf/shop/unicornowl>')


@bot.command()
async def hud(ctx):
    if isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.message.author.send('Unicornowl uses ahud: <https://huds.tf/forum/showthread.php?tid=191>')


@bot.command()
async def links(ctx):
    if isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.message.author.send('Twitch: <http://twitch.tv/unicornowl>\n' +
                   'Twitter: <https://twitter.com/Unicornowlkine>\n' +
                   'Instagram: <https://www.instagram.com/kristinelinneahl/>\n' +
                   'Youtube: <https://www.youtube.com/channel/UCupn_eVNhqY_AN2mSgdYIDQ?>\n' +
                   'Spotify Playlist: <https://open.spotify.com/user/mossepus123?si=M4377HBDTwyIygv-lGCI5g>\n' +
                   'Steam Group: <http://steamcommunity.com/groups/UnicornOwl>\n' +
                   'Snapchat: kristinelinnea\n')


@bot.command()
async def yeet(ctx):
    if not isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.send(':yeet:')


@bot.command()
async def dab(ctx):
    if not isinstance(ctx.message.channel, discord.DMChannel):
        await ctx.send(':kinedab2::kinedab')


@bot.event
async def on_member_join(member):
    print('joined')


bot.run(TOKEN)
