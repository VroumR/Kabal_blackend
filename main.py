main.py

from flask import Flask, request, jsonify from datetime import datetime

app = Flask(name)

@app.route("/sephirot", methods=["POST"]) def get_sephirot(): data = request.get_json() birth_date = data.get("birth_date")  # format: YYYY-MM-DD birth_time = data.get("birth_time")  # format: HH:MM (24h)

try:
    dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
except:
    return jsonify({"error": "Invalid date or time format"}), 400

hour = dt.hour
month = dt.month

# Logique de démo
if month == 9 and hour >= 18:
    main_sephira = "Netzach"
    secondary1 = "Hod"
    secondary2 = "Gevurah"
elif month == 7 and hour < 6:
    main_sephira = "Tiferet"
    secondary1 = "Yesod"
    secondary2 = "Binah"
else:
    main_sephira = "Chesed"
    secondary1 = "Yesod"
    secondary2 = "Hod"

return jsonify({
    "main_sephira": main_sephira,
    "secondary_sephirot": [secondary1, secondary2]
})

