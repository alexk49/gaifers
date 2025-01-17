import json
import os

from flask import (Flask, jsonify, redirect, render_template, request, session,
                   url_for)

from gaifers.hangman import h_game_data_default
from gaifers.noughts import (check_for_draw, check_for_winner,
                             n_game_data_default, update_turn_marker,
                             validate_game_data, validate_marker)

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


def reset_game_data(game_data):
    """Used to clear session variable"""
    session["gameData"] = json.dumps(game_data.copy())
    return json.loads(session["gameData"])


""" App routes """


@app.route("/")
def index():
    return render_template("index.html")


""" Noughts and Crosses """


@app.route("/noughts")
def noughts():
    """Play noughts and crossess"""
    return render_template("noughts.html", game_data=reset_game_data(game_data=n_game_data_default))


@app.route("/noughts/reset")
def reset_noughts():
    game_data = reset_game_data(game_data=n_game_data_default)
    return jsonify(game_data)


@app.route("/noughts/game", methods=["POST"])
def noughts_data():
    game_data = request.get_json()

    org_game_data = get_game_data()

    new_position = game_data["gameData"]["new_position"]
    marker = game_data["gameData"]["playerMarker"]

    if not validate_marker(marker):
        return redirect("/noughts")

    if validate_game_data(game_data, org_game_data):
        game_data["gameData"]["boardData"][new_position] = marker

        game_data["gameData"]["winners"] = check_for_winner(game_data)

        game_data["gameData"]["draw"] = check_for_draw(game_data)

        if not game_data["gameData"]["draw"] and len(game_data["gameData"]["winners"]) == 0:

            game_data["gameData"]["playerMarker"] = update_turn_marker(marker)

        # update session
        session["gameData"] = json.dumps(game_data)
    else:
        session["gameData"] = json.dumps(org_game_data)
        game_data = org_game_data
    return jsonify(game_data)


""" Hangman game """


@app.route("/hangman")
def hangman():
    """Play hangman"""
    return render_template("hangman.html")


@app.route("/hangman/reset")
def reset_hangman():
    game_data = reset_game_data(game_data=h_game_data_default)
    return jsonify(game_data)
