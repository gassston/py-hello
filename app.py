from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

app.run(host="0.0.0.0", port=8081, debug=True)
