#!/bin/bash

# ID regex pattern
pattern="([[:space:]]|%20)[0-9a-f]{32}"

# Root directory
root_dir=$(pwd)

# Function to treat a directory
treat_directory() {
    for item in "$1"/*; do
        if [ -f "$item" ]; then
            treat_file "$item"
        elif [ -d "$item" ]; then
            treat_directory "$item"
        fi
    done
    change_base_name "$1"
}

# Function to treat a file
treat_file() {
    if [[ "$1" == *.md ]]; then
        sed -i '' -E "s/$pattern//g" "$1"
    fi
    change_base_name "$1"
}

# Function to change base name
change_base_name() {
    base_name=$(basename "$1")
    new_name=$(echo "$base_name" | sed -E "s/$pattern//g")
    if [ "$base_name" != "$new_name" ]; then
        mv "$1" "$(dirname "$1")/$new_name"
    fi
}

# Start processing from the root directory
treat_directory "$root_dir"