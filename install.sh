#!/bin/bash

# Change directory to where this .sh script lives
cd "$(dirname "$0")"

# Set the target prefix (Defaults to empty, keeps Termux path if present)
TARGET_PREFIX="${PREFIX:-}"

# Define the destination binary directory (Defaults to /bin if TARGET_PREFIX is empty)
BIN_DIR="${TARGET_PREFIX}/bin"
[ -z "$TARGET_PREFIX" ] && BIN_DIR="/bin"

# Automatically prompt for sudo if not root and not in Termux
if [ -z "$PREFIX" ] && [ "$EUID" -ne 0 ]; then
    echo "This installation requires root privileges. Elevating..."
    exec sudo "$0" "$@"
fi

# Create the directory if it does not exist
mkdir -p "$BIN_DIR"

# Install and set permissions (Only run if cp succeeds)
if cp src/main.py "$BIN_DIR/is-my-code-cursed"; then
    chmod 755 "$BIN_DIR/is-my-code-cursed"
    echo "Successfully installed to $BIN_DIR/is-my-code-cursed"
else
    echo "Installation failed!" >&2
    exit 1
fi

