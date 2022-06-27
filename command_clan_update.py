import json
from api import clan_request


def get_update_clan():
    global clan_data
    data = json.loads(clan_request().content)
    with open('./data_clan.json', 'w') as f:
        clan_data = json.dump(data, f)
    msg = '*Updated Clan Data*'
    return msg
