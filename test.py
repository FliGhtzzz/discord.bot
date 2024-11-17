import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.tree.command(name="repeat", description="Repeat the text")
async def repeat(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(text)



bot.run('MTE4ODQyMDk4MzA2MTc1ODAwMg.G_gusQ.5MPGnppPcUX7zOwvb1F8jWWJMEYMoeN3CdaFpg')
