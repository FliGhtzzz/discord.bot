import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv() 

GEMINI_TOKEN = os.getenv("GEMINI_TOKEN")
genai.configure(api_key=GEMINI_TOKEN)

# 配置生成參數
generation_config = {
    'temperature': 0.7,      # 控制隨機性，0-1之間
    'top_p': 1,              # 控制輸出多樣性
    'top_k': 40,             # 選擇最可能的詞彙
    'max_output_tokens': 2048  # 最大輸出token數
}

# 安全設置
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]

# 創建模型實例
model = genai.GenerativeModel(
    'gemini-pro',
    generation_config=generation_config,
    safety_settings=safety_settings
)

# 發送提示
prompt = "說明Python的主要特點"
response = model.generate_content(prompt)

# 輸出回覆
print(response.text)