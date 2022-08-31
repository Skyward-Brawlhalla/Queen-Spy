from ast import alias, arg
import random
from tkinter import Y
from command_link_remove import delete_link_from_data
from command_waitinglist_list import get_waitinglist_list
import discord
import os
import json
import time
from ntpath import join
from unittest import result
from keep_alive import keep_alive
from pydoc import classname
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from command_link_add import get_add_link
from command_clan_list import get_clan_list
from command_discord_list import get_discord_list
from command_link_list import get_link_list, get_not_linked_brawlhalla_list, get_not_linked_discord_list, get_left_players
from command_clan_update import update_clan_data
from command_discord_update import DiscordAccount, update_discord_data

# VARIABLES
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['qs', 'Qs'],
                   intents=intents)
embed_color = 0x790eab

# ⬇️ STATUS COMMANDS ⬇️
# ⬇️ STATUS COMMANDS ⬇️
# ⬇️ STATUS COMMANDS ⬇️



@has_permissions(ban_members=True)
@bot.command(name='status', aliases=['tatus', 'st', 's'], description='Shows new discord members, new clan members and if people left the clan')
async def get_status(ctx):    
    # send loading message
    msg_loading_data = await ctx.send('_Loading Data..._')

    # update all data
    await update_discord_data(ctx)
    update_clan_data(ctx)

    # setup all embeds and their corresponding information
    msg_list2 = await get_not_linked_brawlhalla_list(ctx)
    embed_not_linked_brawlhalla_list_first = discord.Embed(
        description=msg_list2[0], color=embed_color)
    embed_not_linked_brawlhalla_list_last = discord.Embed(
        description=msg_list2[1], color=embed_color)

    msg_list3 = await get_not_linked_discord_list(ctx)
    embed_not_linked_discord_list_first = discord.Embed(
        description=msg_list3[0], color=embed_color)
    embed_not_linked_discord_list_last = discord.Embed(
        description=msg_list3[1], color=embed_color)

    msg_left_players = await get_left_players(ctx)
    embed_left_players = discord.Embed(description=msg_left_players,
                                       color=embed_color)

    # send embeds
    # send not linked brawlhalla accounts
    await ctx.channel.send(embed=embed_not_linked_brawlhalla_list_first)
    try:
        await ctx.channel.send(embed=embed_not_linked_brawlhalla_list_last)
    except:
        print('less than 26 entries')

    # send not linked discord accounts
    await ctx.channel.send(embed=embed_not_linked_discord_list_first)
    try:
        await ctx.channel.send(embed=embed_not_linked_discord_list_last)
    except:
        print('less than 26 entries')

    # send all players who left the clan
    await ctx.send(embed=embed_left_players)

    # delete loading message
    await msg_loading_data.delete()


# ⬇️ DISCORD COMMANDS ⬇️
# ⬇️ DISCORD COMMANDS ⬇️
# ⬇️ DISCORD COMMANDS ⬇️



@has_permissions(ban_members=True)
@bot.command(name='lsdi', aliases=['lsdc'], description='Show all clan members in discord')
async def show_all_discord_members(ctx):
    msg = await update_discord_data(ctx)
    await ctx.send(msg)

    msg_list = await get_discord_list(ctx)
    embed1 = discord.Embed(description=msg_list[0], color=embed_color)
    embed2 = discord.Embed(description=msg_list[1], color=embed_color)
    await ctx.channel.send(embed=embed1)
    await ctx.channel.send(embed=embed2)


# ⬇️ CLAN COMMANDS ⬇️
# ⬇️ CLAN COMMANDS ⬇️ **
# ⬇️ CLAN COMMANDS ⬇️



@has_permissions(ban_members=True)
@bot.command(name='lscl', description='Show all ingame clan members')
async def show_all_clan_members(ctx):
    await ctx.channel.send(update_clan_data(ctx))

    msg_list = await get_clan_list(ctx)
    embed1 = discord.Embed(description=msg_list[0], color=embed_color)
    embed2 = discord.Embed(description=msg_list[1], color=embed_color)
    await ctx.channel.send(embed=embed1)
    await ctx.channel.send(embed=embed2)


# ⬇️ LINKING COMMANDS ⬇️
# ⬇️ LINKING COMMANDS ⬇️
# ⬇️ LINKING COMMANDS ⬇️


@bot.command(name='rmli', description='Remove a discord-brawlhalla link')
@has_permissions(ban_members=True)
async def remove_link(ctx, brawlhalla_id):
    embed1 = await delete_link_from_data(brawlhalla_id=brawlhalla_id,
                                         bot=bot,
                                         ctx=ctx)


@remove_link.error
async def missing_question(ctx, error):
    await ctx.message.delete()
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            'format your message like the following\n`qsrmli brawlhalla_id`')



@bot.command(name='lsli', description='Show All Links')
@has_permissions(ban_members=True)
async def add_link(ctx):
    await ctx.message.delete()
    msg_list = await get_link_list(ctx)
    embed1 = discord.Embed(description=msg_list[0], color=embed_color)
    embed2 = discord.Embed(description=msg_list[1], color=embed_color)
    await ctx.channel.send(embed=embed1)
    try:
        await ctx.channel.send(embed=embed2)
    except:
        print('less than 26 entries')


class User:
    def __init__(self, brawlhalla_id, brawlhalla_name, discord_id,
                 discord_name):
        self.brawlhalla_id = brawlhalla_id
        self.brawlhalla_name = brawlhalla_name
        self.discord_id = discord_id
        self.discord_name = discord_name



@bot.command(name='adli', aliases=['addli', 'ali'], description='Create a link between a discord and brawlhalla account')
async def add_link(ctx, brawlhalla_id, discord_id):

    # first check if the entry already exists
    with open('./data_link_'+ctx.guild.name+'.json') as data:
        link_data = json.load(data)
    new_entry = True
    for user in link_data:
        if str(user['brawlhalla_id']) == str(brawlhalla_id):
            await ctx.send('brawlhalla_id: ' + brawlhalla_id +
                           ' has already been linked')
            new_entry = False
            break
        if str(user['discord_id']) == str(discord_id):
            await ctx.send('discord_id: ' + discord_id +
                           ' has already been linked')
            new_entry = False
            break

    brawlhalla_name = 'blank'
    discord_name = 'blank'

    # check if ids are valid
    if new_entry == True:
        valid_brawlhalla_id = False
        valid_discord_id = False
        # check clan id
        with open('./data_clan_'+ctx.guild.name+'.json') as data:
            clan_data = json.load(data)
        for member in clan_data['clan']:
            if str(member['brawlhalla_id']) == str(brawlhalla_id):
                valid_brawlhalla_id = True
                brawlhalla_name = member['name']
        # check dc id
        with open('./data_discord_'+ctx.guild.name+'.json') as data:
            discord_data = json.load(data)
        for account in discord_data:
            if str(account['id']) == str(discord_id):
                valid_discord_id = True
                discord_name = account['name']

    # if entry ids are valid, add it
    if ((valid_brawlhalla_id == True) and (valid_discord_id == True)
            and (new_entry == True)):

        await ctx.send('Are you sure you want to add the following link?,')
        await ctx.send(
            embed=discord.Embed(description='**brawlhalla_id**: ' +
                                brawlhalla_id + '\n**brawlhalla_name**: ' +
                                brawlhalla_name + '\n**discord_id**: ' +
                                discord_id + '\n**discord_name**: ' +
                                discord_name,
                                color=embed_color))
        await ctx.send('Send `y` to confirm or `n` to cancel.')
        msg = await bot.wait_for('message', check=check)
        if msg.content == 'y':
            user = User(brawlhalla_id, brawlhalla_name, discord_id,
                        discord_name)
            users = []
            users = link_data
            users.append(user.__dict__)
            with open('./data_link_'+ctx.guild.name+'.json', 'w') as f:
                some_data = json.dump(users, f)

            embed = discord.Embed(
                description='**Added Following Link**\n**brawlhalla_id**: ' +
                brawlhalla_id + '\n**brawlhalla_name**: ' + brawlhalla_name +
                '\n**discord_id**: ' + discord_id + '\n**discord_name**: ' +
                discord_name,
                color=embed_color)
            await ctx.send(embed=embed)
        elif msg.content == 'n':
            await ctx.send('*Process Canceled*')
        else:
            await ctx.send('Invalid answer, process canceled')
    else:
        await ctx.send(
            "There was an error while trying to make the link. One of the following ids doesn't exist\n`discord_id: "
            + discord_id + '`\n`brawlhalla_id: ' + brawlhalla_id + '`')


def check(author):
    def inner_check(message):
        return message.author == author and message.content == "Hello"

    return inner_check


@add_link.error
async def missing_question(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            'format your message like the following\n`qsadli brawlhalla_id discord_id`'
        )


# ⬇️ WAITING LIST COMAMNDS ⬇️
# ⬇️ WAITING LIST COMAMNDS ⬇️ **
# ⬇️ WAITING LIST COMAMNDS ⬇️


@has_permissions(ban_members=True)
@bot.command(name='lswa', description='Shows Waiting List')
async def get_waiting_list(ctx):
    await ctx.message.delete()
    await ctx.channel.send(embed=await get_waitinglist_list(ctx=ctx))


# ⬇️ OTHER COMMANDS ⬇️
# ⬇️ OTHER COMMANDS ⬇️
# ⬇️ OTHER COMMANDS ⬇️


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    log_channel = bot.get_channel(973594560368373820)
    await log_channel.send("I'm back online!")


@bot.command(name='say')
async def add_discord_id(ctx, arg):
    await ctx.message.delete()
    await ctx.channel.send(arg)


@bot.command(name='meme')
async def add_discord_id(ctx):
    memes = [
        'https://media.discordapp.net/attachments/973594560368373820/991113816299548753/unknown.png',
        'https://cdn.discordapp.com/attachments/973594560368373820/991114373366034512/unknown.png',
        'https://media.discordapp.net/attachments/973594560368373820/991115406716719144/unknown.png?width=589&height=670',
        'https://cdn.discordapp.com/attachments/973594560368373820/991116025158443019/unknown.png'
    ]
    meme = memes[random.randint(0, len(memes) - 1)]
    await ctx.channel.send(meme)


@bot.command(name='doc', aliases=['docs'], description="Send you to the GitHub page")
async def doc(ctx):
    await ctx.channel.send(
        'Queen Spy Documentation -> https://github.com/CrossyChainsaw/Queen-Spy'
    )

keep_alive()
bot.run(os.environ['BOT_KEY'])
