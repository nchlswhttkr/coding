#!/bin/bash

set -eu

# $1    Year, for example 2020
# $2    Day, for example 1

# Prepare working space, assuming the usual Python shenanigans
PROBLEM_DIR="advent-of-code/$1/$2"
if [ ${#2} == "1" ]; then
    PROBLEM_DIR="advent-of-code/$1/0$2" # hacky zero padding, bleh
fi
mkdir -p "$PROBLEM_DIR"
echo "import sys" > "$PROBLEM_DIR/1.py"
touch "$PROBLEM_DIR/2.py"
code "$PROBLEM_DIR/1.py"
curl "https://adventofcode.com/$1/day/$2/input" --cookie session=$(cat advent-of-code-oauth-cookie.txt) > "$PROBLEM_DIR/input"
cd $PROBLEM_DIR

# Open the problem
open "https://adventofcode.com/$1/day/$2"
