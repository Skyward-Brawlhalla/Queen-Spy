import config
import discord
import os
import time
import discord
import json
from ntpath import join
from unittest import result
from keep_alive import keep_alive
from discord.ext import commands
from discord.ext import tasks
from pydoc import classname
from discord.ext import commands
from discord.ext import tasks
from keep_alive import keep_alive
from command_add_link import get_add_link
from command_clan_list import get_clan_list
from command_discord_list import get_discord_list
from command_link_list import get_link_list
from command_update_clan import get_update_clan
from command_update_discord import get_update_discord

with open('./data_discord.json') as data:
    discord_data = json.load(data)
with open('./data_clan.json') as data:
    clan_data = json.load(data)
with open('./data_link.json') as data:
    link_data = json.load(data)

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['qs', 'Qs'], intents=intents)

# DISCORD COMMANDS ⬇️


@commands.has_role('DevOps')
@bot.command(name='updi')
async def update_discord_data(ctx):
    await ctx.send(get_update_discord(ctx=ctx))


@commands.has_role('DevOps')
@bot.command(name='lsdi')
async def show_all_discord_members(ctx):
    msg_list = await get_discord_list()
    embed1 = discord.Embed(description=msg_list[0], color=0x289fb4)
    embed2 = discord.Embed(description=msg_list[1], color=0x289fb4)
    await ctx.channel.send(embed=embed1)
    await ctx.channel.send(embed=embed2)

# CLAN COMMANDS ⬇️


@commands.has_role('DevOps')
@bot.command(name='upcl')
async def update_clan_data(ctx):
    await ctx.channel.send(get_update_clan())


@commands.has_role('DevOps')
@bot.command(name='lscl')
async def show_all_clan_members(ctx):
    msg_list = await get_clan_list()
    embed1 = discord.Embed(description=msg_list[0], color=0x289fb4)
    embed2 = discord.Embed(description=msg_list[1], color=0x289fb4)
    await ctx.channel.send(embed=embed1)
    await ctx.channel.send(embed=embed2)

# LINKING COMMANDS ⬇️
# TODO
# 1. make command to add a link
# 2. notify which accounts arent linked


@commands.has_role('DevOps')
@bot.command(name='lsli')
async def add_link(ctx):
    msg_list = await get_link_list()
    embed1 = discord.Embed(description=msg_list[0], color=0x289fb4)
    embed2 = discord.Embed(description=msg_list[1], color=0x289fb4)
    await ctx.channel.send(embed=embed1)
    await ctx.channel.send(embed=embed2)


@commands.has_role('DevOps')
@bot.command(name='adli')
async def add_link(ctx):
    msg_list = await get_add_link()
    embed1 = discord.Embed(description=msg_list[0], color=0x289fb4)
    embed2 = discord.Embed(description=msg_list[1], color=0x289fb4)
    await ctx.channel.send(embed=embed1)
    await ctx.channel.send(embed=embed2)

# EXTRA COMAMNDS ⬇️


@bot.command(name='say')
async def add_discord_id(ctx, arg):
    await ctx.channel.send(arg)


keep_alive()
bot.run(config.BOT_KEY)
