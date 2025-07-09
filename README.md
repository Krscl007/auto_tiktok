# Auto TikTok Pipeline

Diese Pipeline automatisiert:
1. **Trend-Erkennung**
2. **Skript-Generierung** (OpenAI o4-mini)
3. **Video-Erstellung** (MoviePy + TTS)
4. **Automatisiertes Posten** (Selenium oder offizielle API)

## Schnellstart

1. **Klonen**  
   `git clone https://github.com/deinusername/auto_tiktok.git && cd auto_tiktok`
2. **Environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   mkdir output && touch output/cookies.pkl
   export OPENAI_API_KEY="..."
   export TIKTOK_API_KEY="..."
   export TIKTOK_COOKIES_PATH="./output/cookies.pkl"
   export OUTPUT_DIR="./output"
