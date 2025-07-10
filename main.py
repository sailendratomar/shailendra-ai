from flask import Flask, request, jsonify
from flask_cors import CORS
import openai, os

app = Flask(__name__)
CORS(app)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "✅ Shailendra AI is running!"

@app.route("/ask", methods=["POST"])
def ask():
    prompt = request.json.get("prompt","")
    if not prompt: return jsonify({"reply":"❌ No prompt provided."}),400
    resp = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role":"user","content":prompt}],
      temperature=0.7, max_tokens=800
    )
    return jsonify({"reply":resp.choices[0].message.content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
