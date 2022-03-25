#!/usr/bin/env bash

# Constants  -----------------------------------------------------------------

UNUSED_PACKAGES="unattended-upgrades"


# Functions  -----------------------------------------------------------------

_reboot () {
    ### Poweroff system and tel user to restart it manually.

    echo "(!) WARNING: system must be REBOOTed (manually)!"
    echo ""
    echo " => Operating system will now halt... <="
    echo "    Once powered-off, guest operating system must be restarted manually,"
    echo "    and its provisionning rerun!"
    echo ""
    echo "    Please re-run following Vagrant command:"
    echo ""
    echo "        \$ vagrant up --provision"
    echo ""
    systemctl poweroff
    exit 1
}


_update_packages_and_restart_until_no_more_updates () {
    # Upgrade packages
    echo ">>> Check available packages updates..."
    apt update
    local -r _packages="$( apt list --upgradable )"
    rc="${?}"
    if (( $rc == 1 )); then
        echo "/!\ ERRORS on 'apt list --upgradable'!"
        exit 1
    fi
    local -r _nb_packages="$( echo "${_packages}" |wc -l )"
    if (( $_nb_packages > 1 )); then
        echo ">>>     There is ${_nb_packages} packages updates available: upgrade will be called."
        apt upgrade -y
        _reboot
    fi
    # else
    echo ">>>     There is no (more) updates -- continue..."
}


_remove_unused_packages () {
    echo ">>> Remove unused packages..."
    apt purge -y "${UNUSED_PACKAGES}"
    apt autoremove -y
}

_apt_norecommends () {
    echo ">>> Configure APT to not automatically install recommended packages..."
    copy "/etc/apt/apt.conf.d/50norecommends"

    # Ensure config. is correct
    apt update
}


# Main  ----------------------------------------------------------------------

bootstrap_main () {
    _update_packages_and_restart_until_no_more_updates
    _remove_unused_packages
    _apt_norecommends
}

