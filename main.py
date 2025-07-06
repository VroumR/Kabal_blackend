from flask import Flask, request, jsonify
from sephirot_logic import get_sephirot_info

app = Flask(__name__)

@app.route("/sephirot", methods=["POST"])
def get_sephirot():
    data = request.get_json()
    birth_date = data.get("birth_date")  # format: YYYY-MM-DD
    birth_time = data.get("birth_time")  # format: HH:MM (24h)

    try:
        response = get_sephirot_info(birth_date, birth_time)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
