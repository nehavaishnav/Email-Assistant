import os
print("Looking for mockEmail.json in:", os.getcwd())

from flask import Flask, jsonify, render_template
from transformers import pipeline
import base64
import json

app = Flask(__name__)

# Load models
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
reply_generator = pipeline("text-generation", model="microsoft/DialoGPT-small")

# Load mock email
# Load mock email
with open("mockEmail.json") as f:
    email_data = json.load(f)[0]  # Access the first email dictionary

body_b64 = email_data['payload']['body']['data']
decoded_body = base64.b64decode(body_b64).decode('utf-8')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/email")
def generate_ai_response():
    summary = summarizer(decoded_body, max_length=50, min_length=10, do_sample=False)[0]['summary_text']
    reply = reply_generator(
    f"{decoded_body} Reply:",
    max_new_tokens=100,  # 🔄 Replace max_length with this
    num_return_sequences=1
)[0]['generated_text']

    from_email = next(h["value"] for h in email_data['payload']['headers'] if h["name"] == "From")
    subject = next(h["value"] for h in email_data['payload']['headers'] if h["name"] == "Subject")

    return jsonify({
        "from": from_email,
        "subject": subject,
        "original_email": decoded_body,
        "summary": summary,
        "ai_reply": reply
    })

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
