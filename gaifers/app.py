from flask import Flask, jsonify, render_template, url_for

from gaifers.noughts import GameBoard

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


@app.route("/noughts/data")
def noughts_data():
    gameboard = GameBoard()
    return jsonify({'data': gameboard.board})
