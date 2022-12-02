import time
from discord.utils import get

async def assign_all(ctx, role_name):
  role = get(ctx.guild.roles, name=role_name)
  print(role)
  print(ctx.guild.members)
  for member in ctx.guild.members:
    print(member.name)
    await member.add_roles(role)
    time.sleep(3)
