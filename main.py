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
async def call_ai3(ques:str, l:str):
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 1999,
    "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction=f"你是一位專業的翻譯助手,精通多種語言並擅長各類文本的翻譯工作。你的主要任務是協助用戶進行高質量的語言轉換,確保翻譯結果既準確又流暢。請遵循以下指南:仔細理解原文的含義和語境,確保翻譯能夠準確傳達原始信息。根據目標語言的語法規則和表達習慣進行翻譯,使譯文自然流暢。保持原文的風格和語氣,同時適應目標語言的文化背景。正確處理專業術語、成語、俚語和文化特定表達。在需要時提供多個翻譯選項,並解釋各選項的細微差別。注意處理不同語言之間的文化差異,必要時提供文化背景解釋。對於難以直接翻譯的概念或表達,提供恰當的意譯和解釋。保持一致性,特別是在處理長篇文本或技術文檔時。根據用戶的具體需求(如正式/非正式語體、技術/文學翻譯等),調整翻譯策略。提供翻譯建議和語言學習提示,幫助用戶提高語言能力。尊重版權,不翻譯受版權保護的完整作品。請記住,你的目標是提供準確、流暢且符合文化背景的翻譯,同時幫助用戶理解語言和文化的細微差別。保持專業、耐心,並隨時準備解答用戶的問題或澄清疑點。")
    chat_session = model.start_chat(
    history=[]
    )
    response = await chat_session.send_message_async(f"translate {ques} in to {l}")
    return response.text


async def call_ai2(ques:str):
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 1999,
    "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction=f"你是一位專業的寫作助手,擅長各種文體的寫作。你的任務是協助用戶完成他們的寫作項目,無論是創意寫作、學術論文、商業文案還是其他類型的文字工作。請遵循以下指南:仔細閱讀並理解用戶的寫作需求和目標。根據用戶提供的主題、風格和其他要求,提供高品質的文字內容。保持文章的結構清晰,邏輯連貫,並確保語言表達準確、生動。根據不同的寫作類型,適當運用修辭手法,增強文章的表現力和感染力。提供建設性的修改建議,幫助用戶改進他們的寫作。回答用戶關於寫作技巧、語法和風格等方面的問題。尊重版權,不要抄襲或使用未經授權的內容。靈活應對用戶的反饋,根據他們的意見進行調整和修改。請記住,你的目標是幫助用戶提升他們的寫作能力,同時為他們創作出優質的內容。無論遇到什麼樣的寫作任務,都要以專業、友善和富有創意的態度來應對。")
    chat_session = model.start_chat(
    history=[]
    )
    response = await chat_session.send_message_async(f"請依照{ques}為標題產生一個作文")
    return response.text

async def call_ai(ques:str):
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 1999,
    "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction=f"你是一個高效、準確的問答助手,專門設計用來回答用戶的各種問題。你的目標是提供清晰、準確、有見地的回答,同時促進用戶的理解和學習。請遵循以下指南:仔細分析用戶的問題,確保你完全理解他們的詢問內容和意圖。提供簡潔明了的回答,直接針對問題的核心。對於複雜的問題,先給出簡短的總結回答,然後提供更詳細的解釋。使用可靠的信息來源,並在適當的時候引用或提及這些來源。如果問題有多個可能的解釋或答案,列出不同的觀點並解釋它們的差異。對於模糊或不明確的問題,請求澄清或提供可能的解釋方向。在回答中使用例子、類比或圖表來幫助解釋複雜的概念。保持客觀中立,特別是在處理有爭議的話題時。承認知識的局限性。如果無法確定答案,誠實地表明這一點,並提供尋找答案的建議。鼓勵批判性思考。在適當的情況下,引導用戶思考問題的不同方面。對於需要步驟的問題(如數學或編程問題),提供清晰的分步説明。適應不同的知識水平。根據用戶的背景調整回答的深度和複雜性。在回答後,詢問用戶是否需要進一步的解釋或有後續問題。保持禮貌和耐心,即使面對重複或基礎的問題。在討論敏感話題時保持適當和尊重。記住,你的目標不僅是提供正確的答案,還要幫助用戶理解和學習。以友好、專業的態度回應,並始終保持開放和樂於助人的姿態。")
    chat_session = model.start_chat(
    history=[]
    )
    response = await chat_session.send_message_async(f"{ques}")
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

@bot.tree.command(name="questoai",description="以問句問AI問題")
async def userinfo(interaction: discord.Interaction, text: str):
    await interaction.response.defer()
    response = await call_ai(text)
    await interaction.followup.send(f"你的問題是{text},這是回答:\n{response}")

#*******************************************

@bot.tree.command(name="唬爛作文產生器")
async def userinfo(interaction: discord.Interaction, 主題: str):
    try:
        await interaction.response.defer()
        response = await call_ai2(主題)
        await interaction.followup.send(response)
    except Exception as e:
        if not interaction.response.is_done():
            await interaction.response.send_message("發生錯誤，請稍後再試", ephemeral=True)
        else:
            await interaction.followup.send("發生錯誤，請稍後再試", ephemeral=True)
        print(f"Error in userinfo command: {str(e)}")

#*******************************************

@bot.tree.command(name="翻譯",description="翻譯各國語言成你想翻譯的語言")
async def userinfo(interaction: discord.Interaction, text: str, 語言: str):
    await interaction.response.defer()
    response = await call_ai3(text, 語言)
    await interaction.followup.send(text+f"的{語言}翻譯是{response}")

#*******************************************

@bot.tree.command(name="welset",description="set a welcome channel")
async def welset(interaction: discord.Interaction, channel: discord.TextChannel):
    global channelid
    channelid.append(channel.id)
    await interaction.response.send_message(f"Set-Successful ID:{channel.id}")
    print(channelid)


#*******************************************


class ButtonView(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="點擊", style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("[? 好笑嗎](<https://reurl.cc/xpDDYL>)")

@bot.tree.command(name="按鈕產生器")
async def click_click(interaction: discord.Interaction):
    await interaction.response.send_message('別點', view=ButtonView())



#keep_alive.keep_alive()
bot.run(DCBOT_TOKEN)