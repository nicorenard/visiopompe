#!/usr/bin/env bash
# Install Python 3


# Constants  -----------------------------------------------------------------

# These constants should only be used inside this script.
declare -r PYTHON_PACKAGES="python3"
declare -r SETUPTOOLS_PACKAGES="python3-setuptools python3-pip python3-wheel python3-venv"
declare -r PYTHON_MYSQL_PACKAGES="python3-dev default-libmysqlclient-dev build-essential"


# Main  ----------------------------------------------------------------------

echo ">>> Install 'python3' packages..."
apt install -y ${PYTHON_PACKAGES}
apt install -y ${PYTHON_MYSQL_PACKAGES}
apt install -y ${SETUPTOOLS_PACKAGES}

