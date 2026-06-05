from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Webhook server is running"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    print("=== Received webhook ===")
    print(data)
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(debug=True)
