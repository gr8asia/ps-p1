import os

from flask import Flask, jsonify, render_template, send_from_directory


app = Flask(__name__, template_folder=".")


@app.route("/")
def index():
    names = ["Sumit", "Amit", "Priya", "Neha"]
    return render_template("index.html", names=names)


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/script.js")
def script():
    return send_from_directory(".", "script.js")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
