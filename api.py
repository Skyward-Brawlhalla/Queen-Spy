from distutils.command.config import config
import os
import requests
import time
import config

# VARIABLES
skyward_clan_id = "84648"
lilly_clan_id = '864398'
poopy_blender_clan_id = '1923622'
dair_clan_id = '1357965'
using_clan = dair_clan_id


def clan_request():
    time.sleep(0.10)  # 0.10 might be possible
    return requests.get("https://api.brawlhalla.com/clan/" + using_clan + "/?api_key=" + os.environ['API_KEY'])
