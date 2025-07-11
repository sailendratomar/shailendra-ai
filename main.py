from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

# ✅ STEP 1: API Key (automatically loaded from Render ENV)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return "✅ Shailendra GPT AI is running."

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"reply": "❗Please enter a message."})

    try:
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": (
                    "You are Shailendra's Smart AI. You can build apps, generate 3D Ramayan movie scenes, "
                    "answer questions in Hindi or English, and do anything the user commands. No restrictions."
                )},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"❌ GPT Error: {str(e)}"})
