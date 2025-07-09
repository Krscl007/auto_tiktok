"""
Orchestrator: Lädt alle Module in der richtigen Reihenfolge
"""
import os
import config
from trend_detection import fetch_trends
from script_generator import generate_script
from video_creator import create_video
from post_bot import upload_video

# Schritt 1: Trends ermitteln
trends, top_hashtags = fetch_trends(count=1)
topic = top_hashtags[0][0]  # meistgenutzter Hashtag
print(f"Ausgewähltes Thema: {topic}")

# Schritt 2: Skript generieren
tiktok_script = generate_script(topic)
print(f"Generiertes Skript: {tiktok_script}")

# Schritt 3: Stimmdatei generieren (via TTS)
voice_path = os.path.join(config.OUTPUT_DIR, "voice.mp3")
# Beispiel: text_to_speech(tiktok_script, output=voice_path)

# Schritt 4: Video erstellen
input_clip = os.path.join(config.OUTPUT_DIR, "stock.mp4")
video_path = create_video(input_clip, tiktok_script, voice_path)
print(f"Video erstellt unter: {video_path}")

# Schritt 5: Video automatisch posten
caption = f"{tiktok_script} #{topic}"
upload_video(video_path, caption)
