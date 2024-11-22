import google.generativeai as genai
import time
import discord
from discord import ui, ButtonStyle
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
load_dotenv() 

GEMINI_TOKEN = os.getenv("GEMINI_TOKEN")
DCBOT_TOKEN = os.getenv("DCBOT_TOKEN")

# Configure Gemini
genai.configure(api_key=GEMINI_TOKEN)

# Updated generation config for Gemini
generation_config = {
    'temperature': 0.7,
    'top_p': 1,
    'top_k': 64,
    'max_output_tokens': 1999
}

# Updated safety settings for Gemini
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
        "threshold": "BLOCK_NONE"
    }
]

# Initialize the model once
model = genai.GenerativeModel('gemini-pro')

async def call_ai(prompt: str):
    try:
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
        
        # Use the model with generation config and safety settings
        response = await model.generate_content(
            full_prompt,
            generation_config=generation_config,
            safety_settings=safety_settings
        )
        
        return response.text
    except Exception as e:
        return f"AI 處理時發生錯誤: {str(e)}"