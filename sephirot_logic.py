from datetime import datetime
from convertdate import hebrew

# Dictionnaire des correspondances mois hébraïque → Sefira principale
HEBREW_MONTH_TO_SEPHIRA = {
    1: "Netzach",     # Nissan
    2: "Hod",         # Iyar
    3: "Tiferet",     # Sivan
    4: "Gevurah",     # Tamouz
    5: "Hod",         # Av
    6: "Yesod",       # Eloul
    7: "Malkhut",     # Tichri
    8: "Binah",       # Heshvan
    9: "Chokhmah",    # Kislev
    10: "Gevurah",    # Tevet
    11: "Chesed",     # Shevat
    12: "Tiferet"     # Adar
}

# Dictionnaire des plages horaires → Sefira secondaire 1
HOUR_TO_SEPHIRA = [
    (0, 2.5, "Malkhut"),
    (2.5, 4.5, "Yesod"),
    (4.5, 6.5, "Hod"),
    (6.5, 8.5, "Netzach"),
    (8.5, 10.5, "Tiferet"),
    (10.5, 12.5, "Gevurah"),
    (12.5, 14.5, "Chesed"),
    (14.5, 16.5, "Binah"),
    (16.5, 18.5, "Chokhmah"),
    (18.5, 24, "Daat")
]

def get_hour_sephira(hour):
    for start, end, sephira in HOUR_TO_SEPHIRA:
        if start <= hour < end:
            return sephira
    return "Daat"

def get_sephirot_info(birth_date, birth_time):
    try:
        dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    except ValueError:
        return {"error": "Format de date/heure invalide"}

    h_year, h_month, h_day = hebrew.from_gregorian(dt.year, dt.month, dt.day)

    main_sephira = HEBREW_MONTH_TO_SEPHIRA.get(h_month, "Inconnu")
    secondary_sephira = get_hour_sephira(dt.hour + dt.minute / 60)

    return {
        "gregorian_date": birth_date,
        "hebrew_date": f"{h_day} {h_month} {h_year}",
        "main_sephira": main_sephira,
        "secondary_sephira": secondary_sephira
    }
