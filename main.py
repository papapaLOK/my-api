from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "API is working!"}

# 🟦 AI Pinterest Generator API
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    if not data or "prompt" not in data:
        return jsonify({"error": "Missing 'prompt' field"}), 400

    prompt = data["prompt"]

    # 👇 Tu prebehne "generovanie" - zatiaľ statická odpoveď podľa tvojej štruktúry.
    # Môžeš ju neskôr nahradiť AI modelom (zadarmo HuggingFace).
    result = {
        "title": "The Only Toolkit Creators Need",
        "description": "One premium PDF that replaces 10+ apps. No clutter, no confusion — just clarity.",
        "hashtags": [
            "#CreatorTools",
            "#LuxuryPDF",
            "#ContentGrowth",
            "#MinimalistDesign",
            "#NoSubscriptions"
        ],
        "topics": [
            "Content Marketing",
            "Productivity",
            "Branding",
            "Digital Strategy"
        ],
        "image_prompt": "Luxury minimalist Pinterest pin with bold headline 'The Only Toolkit Creators Need', elegant black and gold theme, clean layout, viral-style typography"
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

