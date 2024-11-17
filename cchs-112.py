import discord
import random
import traceback
import typing
import os
import datetime
import time
import requests
import keep_alive
import requests
from bs4 import BeautifulSoup 
from discord.ext import tasks, commands
intents = discord.Intents.all()
intents.message_content = True
welcumid=100
bot = discord.Bot(command_prefix='!', intents=intents)
intents.members = True
#*******************************************
#*******************************************
#*******************************************
'''
事件區
'''

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="/cmd for賴致諺的下體"))

#*******************************************

@bot.event
async def on_message(message):
    if message.author ==  bot.user:
        return
    if message.content == "fuck":
        await message.channel.send("no badword")
    if message.content == "幹":
        await message.channel.send("no badword")
    
#*******************************************

@bot.event
async def on_member_remove(member):
    global welcumid
    if welcumid == 100:
        print(0)
        return
    wel_channel_id = welcumid #ids(不同伺服器要修改) 
    wel_channel = bot.get_channel(wel_channel_id)
    user_id = member.id
    username = member.name
    avatar = member.display_avatar.url
    t = time.time()
    t1 = time.localtime(t)
    t2 = time.strftime('%Y/%m/%d %H:%M:%S',t1)
    embed=discord.Embed(title=f"Leave :\n", description=f"ID: {user_id}\nUser:{member.mention}", color=0x6b5b71)
    embed.set_thumbnail(url="https://animals.sandiegozoo.org/sites/default/files/2016-10/animals_hero_capybara.jpg")
    embed.set_author(name=f"Name:{username}", icon_url=f"{avatar}")
    embed.add_field(name="Publicity!!!", value="* **[Capybara is cute](https://www.google.com/search?q=capybara)**\n* **[About-Taiwan:flag_tw: ](https://eng.taiwan.net.tw/)**", inline=False)
    embed.add_field(name="Leave-Time", value=f"**{t2}**", inline=False)
    await wel_channel.send(embed=embed)

#*******************************************
@bot.event
async def on_member_join(member):
    global welcumid
    if welcumid == 100:
        print(0)
        return
    wel_channel_id = welcumid #ids(不同伺服器要修改)
    wel_channel = bot.get_channel(wel_channel_id)
    user_id = member.id
    username = member.name
    avatar = member.display_avatar.url
    t = time.time()
    t1 = time.localtime(t)
    t2 = time.strftime('%Y/%m/%d %H:%M:%S',t1)
    embed=discord.Embed(title=f"JOIN :\n", description=f"ID: {user_id}\nUser:{member.mention}", color=0x6b5b71)
    embed.set_thumbnail(url="https://animals.sandiegozoo.org/sites/default/files/2016-10/animals_hero_capybara.jpg")
    embed.set_author(name=f"Name:{username}", icon_url=f"{avatar}")
    embed.add_field(name="Publicity!!!", value="* **[Capybara is cute](https://www.google.com/search?q=capybara)**\n* **[About-Taiwan:flag_tw: ](https://eng.taiwan.net.tw/)**", inline=False)
    embed.add_field(name="Join-Time", value=f"**{t2}**", inline=False)
    await wel_channel.send(embed=embed)

#*******************************************
#*******************************************
#*******************************************
'''
指令區  
'''
@bot.slash_command(name="repeat",description="repeat text")
async def test(interaction: discord.Interaction, text: str):    
    await interaction.response.send_message(f'{text}')

#*******************************************

@bot.slash_command(name="cmd",description="finding supported command")
async def cmd(interaction: discord.Interaction):
    await interaction.response.send_message('dick wtf r u expecting??', ephemeral=True)

#*******************************************
    
@bot.slash_command(name="add",description="add a&b")
async def add(interaction: discord.Interaction, a: int, b: int):
    await interaction.response.send_message(a + b)

#*******************************************
    
@bot.slash_command(name="minus",description="minus a&b")
async def minus(interaction: discord.Interaction, a: int, b: int):
    await interaction.response.send_message(a - b)

#*******************************************
    
@bot.slash_command(name="userinfo",description="check user's info")
async def userinfo(interaction: discord.Interaction, user: discord.User):
    user_id = user.id
    avatar = user.display_avatar.url
    botz = bot.user.display_avatar.url
    embed=discord.Embed(title=f"Name:{user.name}", description=f"ID:{user_id}", color=0xc84a14)
    embed.set_thumbnail(url=f"{avatar}")
    embed.set_author(name="Flight's_BOt", icon_url=f"{botz}")
    embed.add_field(name="Publicity!!!", value="* **[Capybara is cute](https://www.google.com/search?q=capybara)**\n* **[About-Taiwan:flag_tw: ](https://eng.taiwan.net.tw/)**", inline=False)
    embed.set_footer(text="Thank for using <3")
    await interaction.response.send_message(embed=embed)
   
#*******************************************
    
    
@bot.slash_command(name="time",description="check time")
async def userinfo(interaction: discord.Interaction):
    t = time.time()
    t1 = time.localtime(t)
    t2 = time.strftime('%Y/%m/%d %H:%M:%S',t1)
    await interaction.response.send_message(f"# It is {t2}  Have a nice day <3")

#*******************************************

@bot.slash_command(name="welset",description="set a welcome channel")
async def welset(interaction: discord.Interaction, channel: discord.TextChannel):
    global welcumid
    welcumid =channel.id
    await interaction.response.send_message(f"Set-Successful ID:{welcumid}")
    print(welcumid)


#*******************************************
    
class ButtonView(discord.ui.View):
    def __init__(self, *, timeout=180):
            super().__init__(timeout=timeout)
    @discord.ui.button(label="點擊", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interation):
        await interation.response.send_message("收到你的點擊")
        
@bot.slash_command(name="按鈕產生器")
async def click_click(interaction: discord.Interaction):
    await interaction.response.send_message('生出了一個按鈕', view=ButtonView())

#*******************************************
    
keep_alive.keep_alive()
bot.run('MTIxNDIwMDY3NDE1ODY0NTI1OA.GFrcTg.LYGt8BZZTQ5NNrMeOgjSHy66FWeMFi2Adl2NzA')