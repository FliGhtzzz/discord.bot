import os
from dotenv import load_dotenv

load_dotenv()  # 自動加載 .env 文件

GEMINI_TOKEN = os.getenv("GEMINI_TOKEN")
DCBOT_TOKEN = os.getenv("DCBOT_TOKEN")

print(f"Gemini Token: {GEMINI_TOKEN}")
print(f"DCBot Token: {DCBOT_TOKEN}")