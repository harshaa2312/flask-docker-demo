from flask import Flask

app = Flask(__name__)  # Use __name__ instead of name

@app.route("/")
def home():
    return "Hello from Flask App!"

if __name__ == "__main__":  # Use __name__ and "__main__"
    app.run(host="0.0.0.0", port=5000)