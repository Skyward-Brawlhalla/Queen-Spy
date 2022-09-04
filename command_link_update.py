import json

# todo
# get link list data
# get clan member data
# in link list replace clan member name with clan member data names

class User:
    def __init__(self, brawlhalla_id, brawlhalla_name, discord_id,
                 discord_name):
        self.brawlhalla_id = brawlhalla_id
        self.brawlhalla_name = brawlhalla_name
        self.discord_id = discord_id
        self.discord_name = discord_name

def update_links(ctx):
  # get link list
  with open('./data_link_'+ctx.guild.name+'.json') as f1:
    link_data = json.load(f1)
  # get clan list
  with open('./data_clan_'+ctx.guild.name+'.json') as f2:
    clan_data = json.load(f2)

  link_data_new = []  
  # in link list replace clan member name with clan member data names
  for account in link_data:
    for clan_member in clan_data['clan']:
      if str(account['brawlhalla_id']) == str(clan_member['brawlhalla_id']):
        if account['brawlhalla_name'] != clan_member['name']:
          print('old name: ' + account['brawlhalla_name'])
          print('new name: ' + clan_member['name'])
          account['brawlhalla_name'] = clan_member['name']
          #link_data_new.append(account)
        break
    #link_data_new.append(account)
  #print(link_data_new)
  link_data_new = link_data
  with open('./data_link_' + ctx.guild.name + '.json', 'w') as f:
    json.dump(link_data_new, f)
  msg = 'Updated Dair Link Data' 
  return msg
    
  