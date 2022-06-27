from ast import Num
import json


async def delete_link_from_data(brawlhalla_id):
    with open('./data_link.json') as f:
        link_data = json.load(f)
    num = 0
    for link in link_data:
        print('3')
        if str(link['brawlhalla_id']) == str(brawlhalla_id):
            del link_data[num]
            break
        num += 1
    with open('./data_link.json', 'w') as f:
        json_string = json.dump(link_data, f)
