import json

with open('./data_link.json') as f:
    link_data = json.load(f)


async def get_add_link():
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
