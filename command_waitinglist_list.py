import json
import discord

from command_discord_update import DiscordAccount

embed_color = 0x790eab


async def get_waitinglist_list():
    waitinglist_data = get_waitinglist_data()
    embed = discord.Embed(description='', color=embed_color)
    embed.description = '**Waiting List**\n'
    for num, player in enumerate(waitinglist_data, 1):
        if num <= 25:
            embed.description += str(num) + '. **discord_id**: ' + \
                str(player['discord_id']) + ', **discord_name**: ' + \
                player['discord_name'] + '\n'
    return(embed)


def get_waitinglist_data():
    with open('./data_waitinglist.json') as f:
        return json.load(f)
