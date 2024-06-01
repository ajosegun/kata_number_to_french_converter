from flask import Flask, jsonify, request
from converter import translate_to_french

app = Flask(__name__)


@app.route("/translate", methods=["GET"])
def translate():
    number = request.args.get("number")
    if number is None:
        return jsonify({"error": "Number is missing in request query parameters"}), 400
    try:
        translated_number = translate_to_french(int(number))
        return jsonify({"translation": translated_number})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
