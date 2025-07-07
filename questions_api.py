import json
from flask import request, jsonify

def register_question_routes(app):

    @app.route("/questions", methods=["GET"])
    def get_questions():
        try:
            with open("questions.json", "r", encoding="utf-8") as f:
                questions = json.load(f)
            return jsonify(questions)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/analyser-test", methods=["POST"])
    def analyser_test():
        try:
            user_answers = request.get_json()
            with open("questions.json", "r", encoding="utf-8") as f:
                questions = json.load(f)

            sephira_scores = {}
            for q in questions:
                matching = next((a for a in user_answers if a["id"] == q["id"]), None)
                if matching:
                    sephira = q["sephira"]
                    score = int(matching["value"])
                    sephira_scores[sephira] = sephira_scores.get(sephira, 0) + score

            if not sephira_scores:
                return jsonify({"error": "Aucune réponse valide reçue."}), 400

            sorted_sephirot = sorted(sephira_scores.items(), key=lambda x: x[1], reverse=True)
            dominante = sorted_sephirot[0][0]
            secondaires = [x[0] for x in sorted_sephirot[1:3]]

            return jsonify({
                "dominante": dominante,
                "secondaires": secondaires,
                "scores": sephira_scores
            })

        except Exception as e:
            return jsonify({"error": str(e)}), 500
