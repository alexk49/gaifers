#!/bin/bash

. ./helpers.sh

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
