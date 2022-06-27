from tkinter import Y
from command_link_remove import delete_link_from_data
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

from command_link_add import get_add_link
from command_clan_list import get_clan_list
from command_discord_list import get_discord_list
from command_link_list import get_link_list, get_not_linked_brawlhalla_list, get_not_linked_discord_list, get_left_players
from command_clan_update import get_update_clan
from command_discord_update import DiscordAccount, get_update_discord

with open('./data_discord.json') as data:
    discord_data = json.load(data)
with open('./data_clan.json') as data:
    clan_data = json.load(data)
with open('./data_link.json') as data:
    link_data = json.load(data)

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['qs', 'Qs'],
                   intents=intents, help_command=None)
embed_color = 0x790eab
# TO DO
# delete link command
# see when a link isnt in the clan ingame anymmore


# ⬇️ DISCORD COMMANDS ⬇️
# ⬇️ DISCORD COMMANDS ⬇️
# ⬇️ DISCORD COMMANDS ⬇️


@commands.has_role('DevOps')
@bot.command(name='updi')
async def update_discord_data(ctx):
    msg = await get_update_discord(ctx)
    await ctx.send(msg)


@commands.has_role('DevOps')
@bot.command(name='lsdi')
async def show_all_discord_members(ctx):
    msg_list = await get_discord_list()
    embed1 = discord.Embed(description=msg_list[0], color=embed_color)
    embed2 = discord.Embed(description=msg_list[1], color=embed_color)
    await ctx.channel.send(embed=embed1)
    await ctx.channel.send(embed=embed2)

# ⬇️ CLAN COMMANDS ⬇️
# ⬇️ CLAN COMMANDS ⬇️
# ⬇️ CLAN COMMANDS ⬇️


@commands.has_role('DevOps')
@bot.command(name='upcl')
async def update_clan_data(ctx):
    await ctx.channel.send(get_update_clan())


@commands.has_role('DevOps')
@bot.command(name='lscl')
async def show_all_clan_members(ctx):
    msg_list = await get_clan_list()
    embed1 = discord.Embed(description=msg_list[0], color=embed_color)
    embed2 = discord.Embed(description=msg_list[1], color=embed_color)
    await ctx.channel.send(embed=embed1)
    await ctx.channel.send(embed=embed2)

# ⬇️ LINKING COMMANDS ⬇️
# ⬇️ LINKING COMMANDS ⬇️
# ⬇️ LINKING COMMANDS ⬇️


@commands.has_role('DevOps')
@bot.command(name='rmli')
async def remove_link(ctx, brawlhalla_id):
    msg = await delete_link_from_data(brawlhalla_id=brawlhalla_id)
    await ctx.send('this doesnt work yet')


@remove_link.error
async def missing_question(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('format your message like the following\n`qsrmli brawlhalla_id`')


@commands.has_role('DevOps')
@bot.command(name='lsli')
async def add_link(ctx):
    msg_list = await get_link_list()
    embed1 = discord.Embed(description=msg_list[0], color=embed_color)
    embed2 = discord.Embed(description=msg_list[1], color=embed_color)
    await ctx.channel.send(embed=embed1)
    try:
        await ctx.channel.send(embed=embed2)
    except:
        print('less than 26 entries')

    msg_list2 = await get_not_linked_brawlhalla_list()
    embed3 = discord.Embed(description=msg_list2[0], color=embed_color)
    embed4 = discord.Embed(description=msg_list2[1], color=embed_color)
    await ctx.channel.send(embed=embed3)
    try:
        await ctx.channel.send(embed=embed4)
    except:
        print('less than 26 entries')

    msg_list3 = await get_not_linked_discord_list()
    embed5 = discord.Embed(description=msg_list3[0], color=embed_color)
    embed6 = discord.Embed(description=msg_list3[1], color=embed_color)
    await ctx.channel.send(embed=embed5)
    try:
        await ctx.channel.send(embed=embed6)
    except:
        print('less than 26 entries')

    msg = await get_left_players()
    embed7 = discord.Embed(description=msg, color=embed_color)
    await ctx.send(embed=embed7)


class User:
    def __init__(self, brawlhalla_id, brawlhalla_name, discord_id, discord_name):
        self.brawlhalla_id = brawlhalla_id
        self.brawlhalla_name = brawlhalla_name
        self.discord_id = discord_id
        self.discord_name = discord_name


@commands.has_role('DevOps')
@bot.command(name='adli')
async def add_link(ctx, brawlhalla_id, discord_id):

    # first check if the entry already exists
    with open('./data_link.json') as data:
        link_data = json.load(data)
    new_entry = True
    for user in link_data:
        if str(user['brawlhalla_id']) == str(brawlhalla_id):
            await ctx.send('brawlhalla_id: ' + brawlhalla_id + ' has already been linked')
            new_entry = False
            break
        if str(user['discord_id']) == str(discord_id):
            await ctx.send('discord_id: ' + discord_id + ' has already been linked')
            new_entry = False
            break

    brawlhalla_name = 'blank'
    discord_name = 'blank'

    # check if ids are valid
    if new_entry == True:
        valid_brawlhalla_id = False
        valid_discord_id = False
        # check clan id
        with open('./data_clan.json') as data:
            clan_data = json.load(data)
        for member in clan_data['clan']:
            if str(member['brawlhalla_id']) == str(brawlhalla_id):
                valid_brawlhalla_id = True
                brawlhalla_name = member['name']
        # check dc id
        with open('./data_discord.json') as data:
            discord_data = json.load(data)
        for account in discord_data:
            if str(account['id']) == str(discord_id):
                valid_discord_id = True
                discord_name = account['name']

    # if entry ids are valid, add it
    if ((valid_brawlhalla_id == True) and (valid_discord_id == True) and (new_entry == True)):

        await ctx.send('Are you sure you want to add the following link?,')
        await ctx.send(embed=discord.Embed(description='**brawlhalla_id**: ' + brawlhalla_id + '\n**brawlhalla_name**: ' + brawlhalla_name + '\n**discord_id**: ' + discord_id + '\n**discord_name**: ' + discord_name, color=embed_color))
        await ctx.send('Send `y` to confirm or `n` to cancel.')
        msg = await bot.wait_for('message', check=check)
        if msg.content == 'y':
            user = User(brawlhalla_id, brawlhalla_name,
                        discord_id, discord_name)
            users = []
            users = link_data
            users.append(user.__dict__)
            with open('./data_link.json', 'w') as f:
                some_data = json.dump(users, f)

            embed = discord.Embed(description='**Added Following Link**\n**brawlhalla_id**: ' + brawlhalla_id + '\n**brawlhalla_name**: ' +
                                  brawlhalla_name + '\n**discord_id**: ' + discord_id + '\n**discord_name**: ' + discord_name, color=embed_color)
            await ctx.send(embed=embed)
        elif msg.content == 'n':
            await ctx.send('*Process Canceled*')
        else:
            await ctx.send('Invalid answer, process canceled')
    else:
        await ctx.send("There was an error while trying to make the link. One of the following ids doesn't exist\n`discord_id: " + discord_id + '`\n`brawlhalla_id: ' + brawlhalla_id + '`')


def check(author):
    def inner_check(message):
        return message.author == author and message.content == "Hello"
    return inner_check


@add_link.error
async def missing_question(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('format your message like the following\n`qsadli brawlhalla_id discord_id`')

# ⬇️ EXTRA COMAMNDS ⬇️
# ⬇️ EXTRA COMAMNDS ⬇️
# ⬇️ EXTRA COMAMNDS ⬇️


@bot.command(name='say')
async def add_discord_id(ctx, arg):
    await ctx.channel.send(arg)


@bot.command(name='help')
async def help(ctx):
    await ctx.channel.send('Queen Spy Documentation -> https://github.com/CrossyChainsaw/Queen-Spy')


keep_alive()
bot.run(config.BOT_KEY)
