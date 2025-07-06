import os
from flask import Flask, request, jsonify
from sephirot_logic import get_sephirot_info

app = Flask(__name__)

@app.route("/sephirot", methods=["POST"])
def get_sephirot():
    data = request.get_json()
    birth_date = data.get("birth_date")  # format: "YYYY-MM-DD"
    birth_time = data.get("birth_time")  # format: "HH:MM"

    try:
        response = get_sephirot_info(birth_date, birth_time)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
