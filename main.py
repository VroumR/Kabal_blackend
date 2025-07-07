import os
from flask import Flask, request, jsonify
from flask_cors import CORS

from sephirot_logic import get_sephirot_info

app = Flask(__name__)

# ✅ Ajoute ici : autorise les appels depuis ton site GitHub Pages
CORS(app, resources={r"/*": {"origins": "https://vroumr.github.io"}})

@app.route("/sephirot", methods=["POST"])
def get_sephirot():
    data = request.get_json()
    birth_date = data.get("birth_date")
    birth_time = data.get("birth_time")
    try:
        response = get_sephirot_info(birth_date, birth_time)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/")
def home():
    return "✅ KABAL backend fonctionne."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

