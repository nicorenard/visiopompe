#!/usr/bin/env bash
# Bash script provisioning Vagrant virtual machine.


# Main  ----------------------------------------------------------------------

main () {
# See https://stackoverflow.com/questions/59895/get-the-source-directory-of-a-bash-script-from-within-the-script-itself#answer-246128
local -r _DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Import functions
source "${_DIR}/const.sh"
source "${_DIR}/_lib.sh"

source "${_DIR}/init/main.sh"
source "${_DIR}/venv/main.sh"
source "${_DIR}/mariadb/main.sh"

# Run scripts
init_main
venv_main
mariadb_main
}


main
