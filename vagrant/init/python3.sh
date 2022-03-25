#!/usr/bin/env bash
# Install and configure Python 3


# Constants  -----------------------------------------------------------------

declare -r PYTHON_PACKAGES="python3"
declare -r SETUPTOOLS_PACKAGES="python3-setuptools python3-pip python3-wheel python3-venv"


# Functions  -----------------------------------------------------------------

_install_python3 () {
    echo ">>> Install 'python3' packages..."

    local pkg;

    for pkg in ${PYTHON_PACKAGES}; do
        apt install -y "${pkg}"
    done
    for pkg in ${SETUPTOOLS_PACKAGES}; do
        apt install -y "${pkg}"
    done
}


# Main  ----------------------------------------------------------------------

python3_main () {
    _install_python3
}

