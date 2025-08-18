from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/contacts', 301)

if __name__ == "__main__":
    # For development convenience; in production use a WSGI server.
    app.run(debug=True)
