import discord
import json


class DiscordAccount:
    def __init__(self, id, name):
        self.discord_id = id
        self.discord_name = name


async def add_to_waiting_list(ctx, discord_id):
    skyward_server = ctx.guild
    waiting_list_role = discord.utils.get(
        skyward_server.roles, name="Waiting List")
    for member in skyward_server.members:
        if waiting_list_role in member.roles:
            if str(member.id) == str(discord_id):
                with open('./data_waitinglist.json') as data:
                    waiting_data = json.load(data)

                new_entry = True
                for waiter in waiting_data:
                    if str(waiter['discord_id']) == str(discord_id):
                        new_entry = False

                if new_entry == True:
                    discord_account = DiscordAccount(member.id, member.name)
                    waiting_data.append(discord_account.__dict__)
                    with open('./data_waitinglist.json', 'w') as f:
                        waiting_data = json.dump(waiting_data, f)
                    msg = '*Added ' + member.name + ' to waiting list*'
                    break
                elif new_entry == False:
                    msg = member.name + ' is already in the waiting list'
        else:
            msg = 'The discord account with `discord_id: ' + \
                discord_id + '` does not have the `@Waiting List` role'  # showing the persons name would be nicer
    return msg
