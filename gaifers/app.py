import json
import os

from flask import Flask, jsonify, render_template, request, session, url_for

from gaifers.noughts import (check_for_draw, check_for_winner,
                             game_data_default, update_turn_marker,
                             validate_game_data)

# Configure app
app = Flask(__name__)

# ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Set the secret key directly
app.secret_key = os.urandom(24)


def get_game_data():
    """Gets original stored game data session json"""
    if "gameData" not in session:
        return reset_game_data()
    return json.loads(session["gameData"])


def reset_game_data():
    """Used to clear session variable"""
    session["gameData"] = json.dumps(game_data_default.copy())
    return json.loads(session["gameData"])


""" App routes """


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/noughts")
def noughts():
    """Play noughts and crossess"""
    return render_template("noughts.html", game_data=reset_game_data())


@app.route("/noughts/reset")
def reset_noughts():
    game_data = reset_game_data()
    return jsonify(game_data)


@app.route("/noughts/game", methods=["POST"])
def noughts_data():
    game_data = request.get_json()

    org_game_data = get_game_data()

    new_position = game_data["gameData"]["new_position"]
    marker = game_data["gameData"]["playerMarker"]

    if validate_game_data(game_data, org_game_data):
        game_data["gameData"]["boardData"][new_position] = marker

        game_data["gameData"]["winner"] = check_for_winner(game_data)

        game_data["gameData"]["draw"] = check_for_draw(game_data)

        if not game_data["gameData"]["draw"] and not game_data["gameData"]["winner"]:

            game_data["gameData"]["playerMarker"] = update_turn_marker(marker)

        # update session
        session["gameData"] = json.dumps(game_data)
    else:
        session["gameData"] = json.dumps(org_game_data)
        game_data = org_game_data
    return jsonify(game_data)
