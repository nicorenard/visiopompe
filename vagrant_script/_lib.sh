#!/usr/bin/env bash
# Common material, our "library" for other scripts.


# Constants  -----------------------------------------------------------------

# See https://stackoverflow.com/questions/59895/get-the-source-directory-of-a-bash-script-from-within-the-script-itself#answer-246128
declare -r LIB_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
declare -r FILES="${LIB_DIR}/files"


# Functions  -----------------------------------------------------------------

copy () {
### Copy a file from $FILES in system dir. tree.
###
### Params:
### - $1 (string) Absolute filepath to copy from $FILES
###
### If parent directory of $1 file does not exist, this function will
### create all of its needed and imbricated parents.

local -r filepath="${1}"
local -r dirpath="$( dirname "${filepath}" )"

if [ ! -d "${dirpath}" ]; then
echo ">>>     Creating directories tree for '${dirpath}'..."
mkdir -p "${dirpath}"
fi
echo ">>>     Copy file '${filepath}'..."
cp "${FILES}/${filepath}" "${filepath}"
}

