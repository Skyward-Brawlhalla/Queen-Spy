from ast import Num
import json
import discord

embed_color = 0x790eab


async def delete_link_from_data(brawlhalla_id, bot, ctx):
    with open('./data_link.json') as f:
        link_data = json.load(f)
    num = 0
    for link in link_data:
        if str(link['brawlhalla_id']) == str(brawlhalla_id):
            await ctx.send('Are you sure you want to delete the following link?')
            embed1 = discord.Embed(
                description='**brawlhalla_id**: ' + str(link_data[num]['brawlhalla_id']) + '\n' +
                '**brawlhalla_name**: ' + str(link_data[num]['brawlhalla_name']) + '\n' +
                '**discord_id**: ' + str(link_data[num]['discord_id']) + '\n' +
                '**discord_name**: ' + str(link_data[num]['discord_name']), color=embed_color)
            await ctx.send(embed=embed1)
            await ctx.send('Send `y` to confirm or `n` to cancel.')

            # confirmation message
            msg = await bot.wait_for('message', check=check)
            if msg.content == 'y':
                embed2 = discord.Embed(
                    description='**Deleted the following link**\n' +
                    '**brawlhalla_id**: ' + str(link_data[num]['brawlhalla_id']) + '\n' +
                    '**brawlhalla_name**: ' + str(link_data[num]['brawlhalla_name']) + '\n' +
                    '**discord_id**: ' + str(link_data[num]['discord_id']) + '\n' +
                    '**discord_name**: ' + str(link_data[num]['discord_name']), color=embed_color)
                del link_data[num]  # delete link
                await ctx.send(embed=embed2)
            elif msg.content == 'n':
                await ctx.send('*Process Canceled*')
            else:
                await ctx.send('Invalid answer, process canceled')
            break
        num += 1
    with open('./data_link.json', 'w') as f:
        json_string = json.dump(link_data, f)


def check(author):
    def inner_check(message):
        return message.author == author and message.content == "Hello"
    return inner_check
