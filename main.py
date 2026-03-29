from flask import Flask, request, redirect, jsonify
from models import init_db, insert_url, save_short_code, get_long_url
from utils import encode

app = Flask(__name__)

init_db()

BASE_URL = "http://localhost:5000/"

@app.route("/shorten", methods=["POST"])
def shorten():
    data = request.json
    long_url = data.get("url")

    if not long_url:
        return jsonify({"error": "URL required"}), 400

    # Step 1: Insert URL → get ID
    url_id = insert_url(long_url)

    # Step 2: Convert ID → short code
    short_code = encode(url_id)

    # Step 3: Save short code
    save_short_code(url_id, short_code)

    return jsonify({
        "short_url": BASE_URL + short_code
    })


@app.route("/<short_code>")
def redirect_url(short_code):
    long_url = get_long_url(short_code)

    if long_url:
        return redirect(long_url)
    else:
        return jsonify({"error": "URL not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)