#!/usr/bin/env bash

# Constants  -----------------------------------------------------------------

declare -r MARIADB_SERVICE="mariadb"
declare -r MARIADB_BIN="mariadb"
declare -r MARIADB_SERVER_MAIN_CONF="/etc/mysql/mariadb.conf.d/50-server.cnf"

declare -r MARIADB_VERSION="10.5"

declare -r MARIADB_PKGS="mariadb-server-${MARIADB_VERSION} mariadb-client-${MARIADB_VERSION} libdbd-mariadb-perl libhtml-template-perl libterm-readkey-perl"
declare -r GRANT_VAGRANT_USER_SQL="GRANT ALL ON *.* TO '${VAGRANT_USER}'@'localhost' IDENTIFIED VIA unix_socket WITH GRANT OPTION"

declare -r MARIADB_CHARSET="utf8mb4"
declare -r MARIADB_COLLATION="utf8mb4_unicode_520_ci"

declare -r DB_NAME="${PROJECT_NAME}"
declare -r DB_USERNAME="${DB_NAME}"
declare -r DB_USER="'${DB_USERNAME}'@'localhost'"
declare -r DB_USER_PASSWORD="${DB_NAME}"
declare -r DB_CREATION_SQL="CREATE DATABASE IF NOT EXISTS ${DB_NAME} CHARACTER SET = '${MARIADB_CHARSET}' COLLATE = '${MARIADB_COLLATION}'"
declare -r DB_USER_CREATION_SQL="CREATE USER IF NOT EXISTS ${DB_USER} IDENTIFIED BY '${DB_USER_PASSWORD}'"
declare -r GRANT_DB_USER_SQL="GRANT ALL ON ${DB_NAME}.* TO ${DB_USER}"


# Functions  -----------------------------------------------------------------

_install_mariadb_packages () {
    echo ">>>     Install packages for MariaDB ${MARIADB_VERSION} server and client..."
    apt install --yes ${MARIADB_PKGS}

    echo ">>>     Grant default '${VAGRANT_USER}' Vagrant user all rights on all MariaDB databases..."
    # See /usr/share/doc/mariadb-server-*/README.txt.gz
    "${MARIADB_BIN}" -e "${GRANT_VAGRANT_USER_SQL}"

    echo ">>>     Shutdown (temporarly) MariaDB server"
    # Stop service via systemd
    systemctl stop "${MARIADB_SERVICE}"
    # Disable service autostart at system start, via systemd
    systemctl disable "${MARIADB_SERVICE}"
}

_set_mariadb_encodings () {
    local -r charset_pattern="^character-set-server[[:space:]]+=[[:space:]]+([[:alpha:][:digit:]_]+)$"
    local -r new_charset="character-set-server = ${MARIADB_CHARSET}"

    local -r collation_pattern="^collation-server[[:space:]]+=[[:space:]]+([[:alpha:][:digit:]_]+)$"
    local -r new_collation="collation-server = ${MARIADB_COLLATION}"

    echo ">>>     Set default MariaDB server character set and encoding..."
    sed -E -i "s/${charset_pattern}/${new_charset}/" "${MARIADB_SERVER_MAIN_CONF}"
    sed -E -i "s/${collation_pattern}/${new_collation}/" "${MARIADB_SERVER_MAIN_CONF}"
}


_start_mariadb_service () {
    echo ">>>     Start MariaDB server"
    # Enable service autostart at system start, via systemd
    systemctl enable "${MARIADB_SERVICE}"
    # Start service via systemd
    systemctl start "${MARIADB_SERVICE}"
}


_create_database () {
    echo ">>>     Create '${DB_NAME}' database (if not exists)..."
    "${MARIADB_BIN}" -e "${DB_CREATION_SQL}"
    echo ">>>     Create '${DB_USERNAME}' database user (if not exists)..."
    "${MARIADB_BIN}" -e "${DB_USER_CREATION_SQL}"
    "${MARIADB_BIN}" -e "${GRANT_DB_USER_SQL}"
}


# Main  ----------------------------------------------------------------------

mariadb_main () {
    echo ">>> Install MariaDB server and client..."
    _install_mariadb_packages
    _set_mariadb_encodings
    _start_mariadb_service
    _create_database
}

