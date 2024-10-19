#!/bin/bash

check_venv_exists () {
    venv_name="$1"
    if [[ -d $venv_name ]]; then
        return 0
    else
        echo "$venv_name does not exist, creating new venv"
        create_new_venv "$venv_name"
    fi
}

create_new_venv () {
    venv_name="$1"
    python3 -m venv "$venv_name"

    get_venv_folder_name
    echo "activating venv $venv_path"
    venv_path="$venv_name/$venv_folder/activate"

    source "$venv_path"
    pip install --upgrade pip

    if [[ "$venv_name" == *"dev"* ]]; then
        echo "installing dev requirements"
        pip install -r "dev-requirements.txt"
    else
        echo "installing requirements"
        pip install -r "requirements.txt"
    fi
}

get_venv_folder_name () {
    # venv path on windows is:
    # venv_name/scripts/activate
    # on linux it is:
    # venv_name/bin/activate
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
        venv_folder="scripts"
    else
        venv_folder="bin"
    fi
}

run () {
    prod="$1"

    if "$prod"; then
        echo "running prod requirements.txt"
        venv_name=".venv"
    else
        echo "running with dev requirements.txt"
        venv_name=".dev-venv"
        export FLASK_DEBUG=1
    fi

    echo "using venv name as: $venv_name"

    check_venv_exists "$venv_name"

    get_venv_folder_name
    venv_path="$venv_name/$venv_folder/activate"

    source "$venv_path"
    cd gaifers || exit
    flask run
}

# set default value for prod var
prod=false

while [[ -n "$1" ]]; do
    case "$1" in
        -p | --prod)
            prod=true
            ;;
    esac
    shift
done

run "$prod"
