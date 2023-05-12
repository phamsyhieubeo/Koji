import discord
from discord import app_commands, Embed, File, Emoji, Role, ui
from discord.ext.commands import *
import json
import random
from discord.app_commands import Choice, choices
from dhooks import Webhook
import time

token = "MTA1MjkzMjI3NzE0NDkyODMwNg.GVz8KS.gUnbqF07IcU7-btJIT7yYRcsHl1Cbc4JpN0IBo"
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = Bot('$', intents= intents)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(len(synced))
    except ValueError as e:
        print(e)
        

@bot.tree.command()
async def don_xin_ban(interact: discord.Interaction, member: discord.Member, reason: str=None):
    if reason == None:
        reason = """Địt mẹ thằng lồn súc vật, mày nghĩ ai cũng ai mày???xin lỗi đéo ai như mày đâu thằng lồn siêu siêu súc vật. ĐỊT MẸ CON CHÓ MAI QUỐC ANH VER3 ULTRA PROMAX.
Đụ đĩ mẹ mày thằng lồn đụ má tao nhịn mày hơi lâu rồi nhe.đéo có ai yêu mày đâu improve your self!!!"""
    
    embed = discord.Embed(title= "Discord Ban Letter", description= "This ban letter", colour= discord.Colour.green())
    embed.set_thumbnail(url = member.avatar.url)
    embed.add_field(name= "Users have been reported", value= member.name)
    embed.add_field(name= "Reason", value= reason, inline= False)
    embed.set_footer(text= f"Author: {interact.user.name}")
    
    channel = bot.get_channel(1097092023577747517)
    await interact.response.send_message("Your message has send successfully", ephemeral= True)
    await channel.send(embed = embed)
    

@bot.tree.command()
async def roll(interact: discord.Interaction, _range: int, auto_roll_time: int = None):
    if auto_roll_time != None:
        await interact.response.send_message(random.randint(1, _range))
        channel = bot.get_channel(interact.channel_id)
        for i in range(1, auto_roll_time):
            await channel.send(random.randint(1, _range))

    
    await interact.response.send_message(random.randint(1, _range))

bot.run(token)