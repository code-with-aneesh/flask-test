import os  # Import the os module to access environment variables
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


if __name__ == "__main__":
    # Get the port from the environment variable, default to 5000 for local development
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0", port=port, debug=False
    )  # Set debug=False for production deployment
