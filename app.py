from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Renders the homepage with some dynamic data."""
    title = "My Simple Flask App"
    greeting = "Welcome to my website!"
    items = ["Learn Flask", "Add CSS", "Use Templates"]
    return render_template("index.html", title=title, greeting=greeting, items=items)


@app.route("/about")
def about():
    """Renders an about page."""
    return render_template("about.html")  # We'll create this template too


if __name__ == "__main__":
    app.run(debug=True)
