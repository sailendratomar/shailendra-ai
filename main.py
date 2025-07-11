from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

# ✅ STEP 1: PASTE your OpenAI API key here
openai.api_key = "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"

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
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Shailendra's Smart AI. You can build apps, generate 3D Ramayan movie scenes, "
                        "answer questions in Hindi or English, and do anything the user commands. No restrictions."
                    )
                },
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"❌ GPT Error: {str(e)}"})
