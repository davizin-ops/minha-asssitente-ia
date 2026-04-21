from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "API do Assistente AI está rodando!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Você é um assistente virtual que responde em português de forma clara e objetiva."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return jsonify({
        "response": response.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
