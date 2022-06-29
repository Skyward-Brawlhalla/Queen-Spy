import discord
import json


class DiscordAccount:
    def __init__(self, id, name):
        self.id = id
        self.name = name


async def update_discord_data(ctx):
    guild = ctx.guild
    msg = ''
    num = 1
    discord_member_names = []
    discord_member_ids = []
    discord_accounts = []
    role = discord.utils.get(ctx.message.guild.roles, name="Clan Member")
    for member in guild.members:
        if role in member.roles:
            msg += str(num) + '. ' + member.name + '\n'
            discord_member_ids.append(member.id)
            discord_member_names.append(member.name)
            num += 1
        if role in member.roles:
            account = DiscordAccount(member.id, member.name)
            discord_accounts.append(account.__dict__)
    with open('./data_discord.json', 'w') as f:
        json_string = json.dump(discord_accounts, f)
    msg = '*Updated discord data*'
    return msg
