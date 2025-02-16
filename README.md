# gaifers

Games in flask, for gamers? Mainly made to learn passing variables to and from the server without reloading the page.

## Terminal Games

Where possible a terminal version has been provided if you run the game script directly.

### noughts and crosses

Run gaifers/noughts.py directly to play a terminal version of noughts and crosses.

### hangman

Run gaifers/hangman.py directly to play a terminal version of hangman.

## Set up

To run the full flask application with dev requirements use:

```
run.sh
```

This will create a virtual environment called .dev-venv, install the dev-requirements.txt into it and run the flask application.

To run with only requirements.txt use one of:

```
run.sh -p
run.sh -prod
```

This will create a virtual environment called .venv, install the requirements.txt into it and run the flask application.

## Tests

Tests have been written using pytest. To set the .dev-venv and run tests use:

```
./tests.sh
```
