import os

# OpenAI API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "o4-mini"

# TikTok API or Scraping
TIKTOK_API_KEY = os.getenv("TIKTOK_API_KEY")

# Selenium/TikTok
TIKTOK_COOKIES_PATH = os.getenv("TIKTOK_COOKIES_PATH", "cookies.pkl")

# Video settings
VIDEO_DURATION = 15  # seconds
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./output")

# Scheduler settings
TREND_FETCH_INTERVAL = 3600  # seconds
