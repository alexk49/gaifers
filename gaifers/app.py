from flask import Flask, render_template, url_for

# Configure app
app = Flask(__name__)

# ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


""" App routes """


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/noughts")
def noughts():
    """Play noughts and crossess"""
    return render_template("noughts.html")
