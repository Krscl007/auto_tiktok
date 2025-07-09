import config
import openai

openai.api_key = config.OPENAI_API_KEY

def generate_script(topic):
    prompt = f"Erstelle ein 15-Sekunden-TikTok-Skript zum Thema {topic}."
    resp = openai.ChatCompletion.create(
        model=config.OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content

if __name__ == '__main__':
    example_topic = "#Beispiel"
    script = generate_script(example_topic)
    print(script)
