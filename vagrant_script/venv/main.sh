#!/usr/bin/env bash

# Constants  -----------------------------------------------------------------

declare -r VENV_PIP="${PROJECT_VENV_DIR}/bin/pip"
declare -r PYTHON_PACKAGING_TOOLS="setuptools pip wheel"


# Functions  -----------------------------------------------------------------

_create_venv () {
local -r VENV_PARENT_DIRPATH="$( dirname "${PROJECT_VENV_DIR}" )"

echo ">>>     Create dedicated Python virtualenv for '${PROJECT_NAME}' at '${PROJECT_VENV_DIR}'..."
mkdir -p "${VENV_PARENT_DIRPATH}"

"${PYTHON3_BIN}" -m venv "${PROJECT_VENV_DIR}"

local pkg;
for pkg in ${PYTHON_PACKAGING_TOOLS}; do
"${VENV_PIP}" install --upgrade "${pkg}"
done
}


_install_venv_requirements () {
echo ">>>     Install Python modules required as listed in '${PROJECT_REQUIREMENTS_FILE}'..."
"${VENV_PIP}" install --upgrade -r "${PROJECT_REQUIREMENTS_FILE}"
}


# Main  ----------------------------------------------------------------------

venv_main () {
echo ">>> Create and/or update project's dedicated virtualenv..."
_create_venv
_install_venv_requirements
}

