from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

if __name__ == "__main__":
    # For development convenience; in production use a WSGI server.
    app.run(debug=True)
