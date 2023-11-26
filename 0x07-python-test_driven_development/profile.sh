#!/bin/bash

# Check if correct number of arguments are provided
if [ "$#" -ne 3 ]; then
	echo "Usage: $0 <file_name> <function_name> <function_call>"
    exit 1
fi

file_name=$1
function_name=$2
function_call=$3
insert_text="@profile"

# Ensure profiles directory exists or create it
mkdir -p profiles

# Using sed to add text before the specified function
sed -e "/^def $function_name/ s/^/$insert_text\n/" "$file_name" > profiles/"$file_name"

echo "Text added to profiles/$file_name"

echo "$function_call" >> profiles/"$file_name"

kernprof -l -v profiles/"$file_name"

rm *.lprof
