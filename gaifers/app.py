import json
import os

from flask import Flask, jsonify, render_template, request, session, url_for

from gaifers.noughts import GameBoard, game_data_default

# Configure app
app = Flask(__name__)

# ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Set the secret key directly
app.secret_key = os.urandom(24)


def get_game_data():
    """Gets original stored game data session json"""
    if "gameData" not in session:
        session["gameData"] = json.dumps(game_data_default.copy())
    return json.loads(session["gameData"])


def validate_game_data(game_data: dict, org_game_data: dict) -> bool:
    """Check game data for any changes
    Dicts should be the same values until the new position is updated
    """
    new_position = game_data["gameData"]["new_position"]

    for key in game_data["gameData"]["boardData"]:
        if key == new_position and game_data["gameData"]["boardData"][key] != "":
            print(f"{new_position} is not empty square")
            return False
        elif game_data["gameData"]["boardData"][key] != org_game_data["gameData"]["boardData"][key]:
            print("new gameData doesn't match old gameData")
            return False
    return True


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

    org_game_data = get_game_data()

    new_position = game_data["gameData"]["new_position"]
    marker = game_data["gameData"]["playerMarker"]

    if validate_game_data(game_data, org_game_data):
        game_data["gameData"]["boardData"][new_position] = marker

    # update session
    session["gameData"] = json.dumps(game_data)
    return jsonify(game_data)
