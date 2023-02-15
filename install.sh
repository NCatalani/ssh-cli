#!/usr/bin/env bash

REQUIREMENTS_FILE="requirements-dev.txt"

function write_log() {
    DATE=$(date '+%d-%m-%Y %H:%M:%S')
    MSG=$1

    echo "[${DATE}] ${MSG}"
}

write_log "SSH-CLI Installer"
write_log "Starting..."
write_log "Creating virtual environment..."
python3 -m venv .env

write_log "Activating..."

source .env/bin/activate

write_log "Installing dependencies..."

pip3 install -r $REQUIREMENTS_FILE

write_log "Done!"

deactivate
