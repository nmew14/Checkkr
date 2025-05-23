from flask import Flask, request

app = Flask(name)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello from Tech VJ'

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)  # Sirf test ke liye
    return 'OK', 200

if name == "main":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render ka port
    app.run(host='0.0.0.0', port=port)
