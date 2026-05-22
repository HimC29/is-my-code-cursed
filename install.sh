#!/bin/bash

# change directory to where this .sh script lives
cd "$(dirname "$0")"

# set the target prefix (Defaults to / on Linux, keeps Termux path)
TARGET_PREFIX="${PREFIX:-/}"

# define the destination binary directory
BIN_DIR="$TARGET_PREFIX/bin"

# create the directory if it does not exist
mkdir -p "$BIN_DIR"

# install and set permissions
cp src/main.py "$BIN_DIR/is-my-code-cursed"
chmod 755 "$BIN_DIR/is-my-code-cursed"

echo "Successfully installed to $BIN_DIR/is-my-code-cursed"
