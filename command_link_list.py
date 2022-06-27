import json
import discord


async def get_link_list():
    with open('./data_link.json') as f:
        link_data = json.load(f)
    num = 1
    msg1 = '**All links between discord and brawlhalla**\n'
    msg2 = ''
    for user in link_data:
        if num <= 25:
            msg1 += '**' + str(num) + '**: \n**brawlhalla_id**: ' + \
                str(user['brawlhalla_id']) + '\n**brawlhalla_name**: ' + \
                user['brawlhalla_name'] + '\n**discord_id**: ' + \
                str(user['discord_id']) + '\n**discord_name**: ' + \
                user['discord_name'] + '\n\n'
        else:
            msg2 += '**' + str(num) + '**: \n**brawlhalla_id**: ' + \
                str(user['brawlhalla_id']) + '\n**brawlhalla_name**: ' + \
                user['brawlhalla_name'] + '\n**discord_id**: ' + \
                str(user['discord_id']) + '\n**discord_name**: ' + \
                user['discord_name'] + '\n\n'
        num += 1
    msg_list = []
    msg_list.append(msg1)
    msg_list.append(msg2)
    return(msg_list)


async def get_not_linked_brawlhalla_list():
    with open('./data_clan.json') as f:
        clan_data = json.load(f)
    with open('./data_link.json') as f:
        link_data = json.load(f)

    new_discord_ids = []
    new_discord_names = []
    for member in clan_data['clan']:
        new_id = True
        for link in link_data:
            if str(link['brawlhalla_id']) == str(member['brawlhalla_id']):
                new_id = False
        if new_id == True:
            new_discord_ids.append(str(member['brawlhalla_id']))
            new_discord_names.append(str(member['name']))

    msg1 = "**The following people are ingame in brawlhalla, but aren't linked yet\n**"
    msg2 = ""
    num = 1
    for (id, name) in zip(new_discord_ids, new_discord_names):
        if num <= 25:
            msg1 += str(num) + '. **brawlhalla_id**: ' + id + \
                ', **brawlhalla_name**: ' + name + '\n'
        else:
            msg2 += str(num) + '. **brawlhalla_id**: ' + id + \
                ', **brawlhalla_name**: ' + name + '\n'
        num += 1

    msg_list = []
    msg_list.append(msg1)
    msg_list.append(msg2)
    return(msg_list)


async def get_not_linked_brawlhalla_list():
    with open('./data_clan.json') as f:
        clan_data = json.load(f)
    with open('./data_link.json') as f:
        link_data = json.load(f)

    new_brawlhalla_ids = []
    new_brawlhalla_names = []
    for member in clan_data['clan']:
        new_id = True
        for link in link_data:
            if str(link['brawlhalla_id']) == str(member['brawlhalla_id']):
                new_id = False
        if new_id == True:
            new_brawlhalla_ids.append(str(member['brawlhalla_id']))
            new_brawlhalla_names.append(str(member['name']))

    msg1 = "**The following people are in the in-game clan, but aren't linked yet\n**"
    msg2 = ""
    num = 1
    for (id, name) in zip(new_brawlhalla_ids, new_brawlhalla_names):
        if num <= 25:
            msg1 += str(num) + '. **brawlhalla_id**: ' + id + \
                ', **brawlhalla_name**: ' + name + '\n'
        else:
            msg2 += str(num) + '. **brawlhalla_id**: ' + id + \
                ', **brawlhalla_name**: ' + name + '\n'
        num += 1

    msg_list = []
    msg_list.append(msg1)
    msg_list.append(msg2)
    return(msg_list)


async def get_not_linked_discord_list():
    with open('./data_discord.json') as f:
        data_discord = json.load(f)
    with open('./data_link.json') as f:
        link_data = json.load(f)

    new_discord_ids = []
    new_discord_names = []
    for account in data_discord:
        new_id = True
        for link in link_data:
            if str(link['discord_id']) == str(account['id']):
                new_id = False
        if new_id == True:
            new_discord_ids.append(str(account['id']))
            new_discord_names.append(str(account['name']))

    msg1 = "**The following people are in the discord, but aren't linked yet\n**"
    msg2 = ""
    num = 1
    for (id, name) in zip(new_discord_ids, new_discord_names):
        if num <= 25:
            msg1 += str(num) + '. **discord_id**: ' + id + \
                ', **discord_name**: ' + name + '\n'
        else:
            msg2 += str(num) + '. **discord_id**: ' + id + \
                ', **discord_name**: ' + name + '\n'
        num += 1

    msg_list = []
    msg_list.append(msg1)
    msg_list.append(msg2)
    return(msg_list)


async def get_left_players():
    with open('./data_link.json') as f:
        link_data = json.load(f)
    with open('./data_clan.json') as f:
        clan_data = json.load(f)

    msg = "**The following accounts are linked, but aren't in the clan anymore**\n"
    num = 1
    for link in link_data:
        entry_exists = False
        for member in clan_data['clan']:
            if str(link['brawlhalla_id']) == str(member['brawlhalla_id']):
                entry_exists = True
        if entry_exists == False:
            msg += str(num) + '. **brawlhalla_id**: ' + \
                link["brawlhalla_id"] + ', **brawlhalla_name**: ' + \
                link['brawlhalla_name'] + '\n'
            num += 1

    return msg
