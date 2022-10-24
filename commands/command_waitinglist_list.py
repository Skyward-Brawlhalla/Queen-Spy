import discord

# VARIABLES
embed_color = 0x790eab

async def get_waitinglist_list(ctx):
    skyward_server = ctx.guild
    member_names = []
    waiting_list_role = discord.utils.get(
        skyward_server.roles, name="Waiting List")
    for member in skyward_server.members:
        if waiting_list_role in member.roles:
            member_names.append(member.name)

    embed = discord.Embed(title='', description='', color=embed_color)
    embed.title = '**Waiting List**'
    num = 1
    if len(member_names) > 0:
      for name in member_names:
        if num <= 25:
            embed.description += str(num) + '. ' + '**discord_name**: ' + \
                name + '\n'
        num += 1
    else:
      embed.description += 'waiting list is empty, give someone the `@Waiting List` role and try again'
    return(embed)
