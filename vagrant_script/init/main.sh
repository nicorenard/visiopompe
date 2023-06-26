#!/usr/bin/env bash


# Main  ----------------------------------------------------------------------

init_main () {
    # See https://stackoverflow.com/questions/59895/get-the-source-directory-of-a-bash-script-from-within-the-script-itself#answer-246128
    local -r _DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

    # Import functions
    source "${_DIR}/bootstrap.sh"
    source "${_DIR}/utils.sh"
    source "${_DIR}/python3.sh"

    # Upgrade packages
    echo ">>> Update system and packages until no more are available (possible reboot)..."
    bootstrap_main

    # Install common system utilities
    echo ">>> Install common system utilities..."
    utils_main

    # Install Python3
    echo ">>> Install 'python3' packages..."
    python3_main
}

