import google.generativeai as genai
import time
import discord
from discord import ui, ButtonStyle
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
GEMINI_TOKEN = os.getenv("GEMINI_TOKEN")
DCBOT_TOKEN = os.getenv("DCBOT_TOKEN")
genai.configure(api_key=GEMINI_TOKEN)
load_dotenv() 

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
async def call_ai3(ques: str, l: str):
    prompt = f"translate {ques} into {l}"
    try:
        response = genai.generate_text(
            model="text-bison-001",  # 確保模型名稱正確
            prompt=prompt,
            temperature=1,
            max_output_tokens=500
        )
        return response["candidates"][0]["output"]
    except Exception as e:
        print(f"AI 調用失敗: {e}")
        return "翻譯失敗，請稍後再試。"


async def call_ai2(ques:str):
    genai.configure(api_key=GEMINI_TOKEN)
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 5000,
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
    genai.configure(api_key=GEMINI_TOKEN)
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 5000,
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
    await interaction.response.send_message('0.0.3, update the AI system', ephemeral=True)

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