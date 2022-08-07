import json
from unicodedata import name
import discord

from command_discord_update import DiscordAccount

embed_color = 0x790eab


async def get_waitinglist_list(ctx):
    skyward_server = ctx.guild
    member_ids = []
    member_names = []
    waiting_list_role = discord.utils.get(
        skyward_server.roles, name="Waiting List")
    for member in skyward_server.members:
        if waiting_list_role in member.roles:
            member_ids.append(member.id)
            member_names.append(member.name)

    embed = discord.Embed(description='', color=embed_color)
    embed.description = '**Waiting List**\n'
    num = 1
    for id, name in zip(member_ids, member_names):
        if num <= 25:
            embed.description += str(num) + '. **discord_id**: ' + \
                str(id) + ', **discord_name**: ' + \
                name + '\n'
        num += 1
    return(embed)
