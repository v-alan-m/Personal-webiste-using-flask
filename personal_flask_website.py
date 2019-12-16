from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Website content goes here"

if __name__ == "__main__":
    app.run(port=5000, debug=True)