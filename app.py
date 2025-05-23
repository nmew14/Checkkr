from flask import Flask, request
import os

app = Flask(name)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello from Tech VJ'

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)  # For testing
    return 'OK', 200

if name == "main":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
