main.py

from flask import Flask, request, jsonify from sephirot_logic import get_sephirot_info

app = Flask(name)

@app.route("/sephirot", methods=["POST"]) def get_sephirot(): data = request.get_json() birth_date = data.get("birth_date")  # format: YYYY-MM-DD birth_time = data.get("birth_time")  # format: HH:MM (24h)

result = get_sephirot_info(birth_date, birth_time)
if "error" in result:
    return jsonify(result), 400

return jsonify(result)

if name == "main": app.run(debug=True)
