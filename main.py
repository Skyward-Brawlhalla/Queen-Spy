import secrets
import config
from keep_alive import keep_alive
import discord
from discord.ext import commands
from discord.ext import tasks
import os
from pydoc import classname
import discord
from discord.ext import commands
from discord.ext import tasks
import time
import json
from keep_alive import keep_alive


bot = commands.Bot(command_prefix=['qs', 'qs'])


@bot.command(name='hi')
async def start(ctx):
    await ctx.channel.send('nsig go crazy')

keep_alive()
bot.run(config.BOT_KEY)
