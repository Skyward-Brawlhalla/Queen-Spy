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


def clan_request(ctx):
    using_clan = set_using_clan(ctx)
    time.sleep(0.10)  # 0.10 might be possible
    return requests.get("https://api.brawlhalla.com/clan/" + using_clan + "/?api_key=" + os.environ['API_KEY'])

def set_using_clan(ctx):
  if ctx.guild.name == "Skyward":
    return skyward_clan_id
  elif ctx.guild.name == "Dair":
    return dair_clan_id
