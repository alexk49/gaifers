from flask import Flask, g, jsonify, render_template, request, url_for

from gaifers.noughts import GameBoard

# Configure app
app = Flask(__name__)

# ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


def get_gameboard_obj():
    """
    Gets gameboard object in use across flask session

    Returns new gameboard if obj can't be found
    """
    if 'gameboard' not in g:
        g.gameboard = GameBoard()
    return g.gameboard


""" App routes """


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/noughts")
def noughts():
    """Play noughts and crossess"""
    return render_template("noughts.html", gameboard=GameBoard())


@app.route("/noughts/game", methods=["POST"])
def noughts_data():
    game_data = request.get_json()

    gameboard = get_gameboard_obj()

    for i, (key, value) in enumerate(game_data["boardData"].items()):
        gameboard.board[i] = value

    return jsonify({'boardData': gameboard.board})
