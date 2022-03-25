#!/usr/bin/env bash
# Install and configure Python 3


# Constants  -----------------------------------------------------------------

declare -r APTITUDE_PACKAGES="aptitude libdpkg-perl libfile-fcntllock-perl"
declare -r VIM_PACKAGES="vim vim-doc"


# Functions  -----------------------------------------------------------------

_install_utils_packages () {
    echo ">>> Install some common system utilities packages..."
    apt install -y ${APTITUDE_PACKAGES}
    apt install -y ${VIM_PACKAGES}
}


# Main  ----------------------------------------------------------------------

utils_main () {
    _install_utils_packages
}

