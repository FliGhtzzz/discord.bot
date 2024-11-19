
import google.generativeai as genai
import time
import discord
from discord import ui, ButtonStyle
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
load_dotenv() 

GEMINI_TOKEN = os.getenv("GEMINI_TOKEN")
DCBOT_TOKEN = os.getenv("DCBOT_TOKEN")
genai.configure(api_key=GEMINI_TOKEN)
generation_config = {
    'temperature': 0.7,      # 控制隨機性，0-1之間
    'top_p': 1,              # 控制輸出多樣性
    'top_k': 64,             # 選擇最可能的詞彙
    'max_output_tokens': 1999  # 最大輸出token數
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"  # 關閉危險內容的阻攔
    }
]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
intents.members = True
channelid = []
#*******************************************
#*******************************************
#*******************************************
'''
事件區
'''
#*******************************************
async def call_ai(prompt:str):
    full_prompt = f"""
    你是一個專業且詳細的助手。請提供一個全面、深入的回答，並遵守以下指南：

    1. 盡可能詳細地回答問題
    2. 提供豐富的上下文和解釋
    3. 如果問題允許，給出多個視角或方法
    4. 使用具體的例子來闡明觀點
    5. 保持回答的結構性和邏輯性

    原始問題：{prompt}

    請開始你詳細的回答：
    """
    model = genai.GenerativeModel(
    'gemini-pro',
    generation_config=generation_config,
    safety_settings=safety_settings
    )
    
    response = model.generate_content(full_prompt)
    return response.text
#*******************************************

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()  # 同步指令
        print(f"同步完成，共 {len(synced)} 條指令。")
    except Exception as e:
        print(f"指令同步失敗: {e}")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="你的感情"))

#*******************************************

@bot.event
async def on_message(message):
    if message.author ==  bot.user:
        return
    
#*******************************************

@bot.event
async def on_member_remove(member):#member.guild.id
    guild=member.guild
    global channelid
    for channel in guild.text_channels:
        if channel.id in channelid:
                wel_channel = bot.get_channel(channel.id)
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
    guild=member.guild
    global channelid
    for channel in guild.text_channels:
        if channel.id in channelid:
                wel_channel = bot.get_channel(channel.id)
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
#*******************************************
#*******************************************
'''
指令區  
'''#@bot.hybrid_command
@bot.tree.command(name="repeat",description="repeat text")
async def repeat(interaction: discord.Interaction, text: str):    
    await interaction.response.send_message(text)

#*******************************************

@bot.tree.command(name="version",description="tell you the bots' version")
async def cmd(interaction: discord.Interaction):
    await interaction.response.send_message('0.3.1, 更新了AI和debug', ephemeral=True)

#*******************************************
    
@bot.tree.command(name="userinfo",description="check user's info")
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
    
    
@bot.tree.command(name="time",description="check time")
async def userinfo(interaction: discord.Interaction):
    t = time.time()
    t1 = time.localtime(t)
    t2 = time.strftime('%Y/%m/%d %H:%M:%S',t1)
    await interaction.response.send_message(f"# It is {t2}  Have a nice day <3")

#*******************************************

@bot.tree.command(name="questoai",description="例如1+1=?，請以這種形式")
async def userinfo(interaction: discord.Interaction, 想問的問題: str):
    await interaction.response.defer()
    response = await call_ai(想問的問題)
    await interaction.followup.send(response)

#*******************************************

@bot.tree.command(name="唬爛作文產生器")
async def userinfo(interaction: discord.Interaction, 作文的主題: str):
    await interaction.response.defer()
    response = await call_ai(f"以{作文的主題}生成一篇作文")
    await interaction.followup.send(response)

#*******************************************

@bot.tree.command(name="翻譯",description="翻譯各國語言成你想翻譯的語言")
async def userinfo(interaction: discord.Interaction, 原文: str, 語言: str):
    await interaction.response.defer()
    response = await call_ai(f"translate{原文} in to {語言}")
    await interaction.followup.send(f"這是翻譯:\n{response}")

#*******************************************

@bot.tree.command(name="welset",description="set a welcome channel")
async def welset(interaction: discord.Interaction, channel: discord.TextChannel):
    global channelid
    channelid.append(channel.id)
    await interaction.response.send_message(f"Set-Successful ID:{channel.id}")
    print(channelid)


#*******************************************

class ButtonView(discord.ui.View):
    def __init__(self, link, word, *, timeout=180):
        super().__init__(timeout=timeout)
        self.add_item(discord.ui.Button(label=word, style=discord.ButtonStyle.link, url=link))


@bot.tree.command(name="按鈕產生器")
async def click_click(interaction: discord.Interaction, 連結: str, 想顯示的字: str):
    if interaction.response.is_done():
        # 如果互動已被回應，直接跳過
        return

    await interaction.response.send_message(f"`通往{連結}的按鈕:`", view=ButtonView(連結, 想顯示的字))



#keep_alive.keep_alive()
bot.run(DCBOT_TOKEN)