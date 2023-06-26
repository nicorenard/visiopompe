#!/usr/bin/env bash
# Bash scripts initialization common constants


# Constants  -----------------------------------------------------------------

declare -r VAGRANT_USER="vagrant"
declare -r PYTHON3_BIN="python3"

declare -r PROJECT_NAME="visiopompe"
declare -r VIRTUALENVS_DIR="/opt/virtualenvs"
declare -r PROJECT_VENV_DIR="${VIRTUALENVS_DIR}/${PROJECT_NAME}"

declare -r PROJECT_SRC_DIR="/usr/share/visiopompe"
declare -r PROJECT_REQUIREMENTS_FILE="${PROJECT_SRC_DIR}/requirements.txt"

