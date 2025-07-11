from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ✅ Allows frontend to access backend

@app.route('/')
def home():
    return "✅ Shailendra AI backend is running"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"reply": "❗Please ask something!"})

    # Replace this with real AI logic if needed
    return jsonify({"reply": f"🧠 AI says: You asked - {prompt}"})
