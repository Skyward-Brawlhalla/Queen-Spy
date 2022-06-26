import json

with open('./data_discord.json') as f:
    discord_data = json.load(f)


async def get_discord_list():
    num = 1
    msg1 = '**All users with [@Clan Member] role in discord**' + '\n'
    msg2 = ''
    for player in discord_data:
        if num <= 25:
            msg1 += str(num) + '. **discord_id**: ' + \
                str(player['id']) + ', **discord_name**: ' + \
                player['name'] + '\n'
        else:
            msg2 += str(num) + '. **discord_id**: ' + \
                str(player['id']) + ', **discord_name**: ' + \
                player['name'] + '\n'
        num += 1
    msg_list = []
    msg_list.append(msg1)
    msg_list.append(msg2)
    return(msg_list)
