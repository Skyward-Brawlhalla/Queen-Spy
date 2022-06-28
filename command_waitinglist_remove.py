from ast import Num
import json
import discord

embed_color = 0x790eab


async def delete_waiter_from_waitinglist(discord_id, bot, ctx):
    with open('./data_waitinglist.json') as f:
        waitinglist_data = json.load(f)
    num = 0
    for link in waitinglist_data:
        if str(link['discord_id']) == str(discord_id):
            msg1 = await ctx.send('Are you sure you want to delete the following following player from the waiting list?')
            embed1 = discord.Embed(
                description='**discord_id**: ' + str(waitinglist_data[num]['discord_id']) + '\n' + '**discord_name**: ' + str(waitinglist_data[num]['discord_name']), color=embed_color)
            msg2 = await ctx.send(embed=embed1)
            msg3 = await ctx.send('Send `y` to confirm or `n` to cancel.')
            print(num)
            print(waitinglist_data)
            # confirmation message
            msg = await bot.wait_for('message', check=check)
            if msg.content == 'y':
                del waitinglist_data[num]  # delete link
                embed2 = discord.Embed(
                    description='**Deleted the following player**\n' +
                    '**discord_id**: ' + str(waitinglist_data[num]['discord_id']) + '\n' +
                    '**discord_name**: ' + str(waitinglist_data[num]['discord_name']), color=embed_color)
                await ctx.send(embed=embed2)
            elif msg.content == 'n':
                await ctx.send('*Process Canceled*')
            else:
                await ctx.send('Invalid answer, process canceled')
            await msg1.delete()
            await msg2.delete()
            await msg3.delete()
            break

        num += 1
    with open('./data_waitinglist.json', 'w') as f:
        json_string = json.dump(waitinglist_data, f)


def check(author):
    def inner_check(message):
        return message.author == author and message.content == "Hello"
    return inner_check
