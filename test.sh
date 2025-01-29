#!/bin/bash

. ./helpers.sh

venv_name=".dev-venv"

check_venv_exists "$venv_name"

get_venv_folder_name

venv_path="$venv_name/$venv_folder/activate"

source "$venv_path"

python -m pytest
