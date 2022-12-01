#!/bin/bash

set -euo pipefail

# $1    Year, for example 2020
# $2    Day, for example 1

# Prepare working space, assuming the usual Python shenanigans
PROBLEM_DIR="advent-of-code/$1/$2"
if [ ${#2} == "1" ]; then
    PROBLEM_DIR="advent-of-code/$1/0$2" # hacky zero padding, bleh
fi

echo "Advent of Code $1, Day $2 (https://adventofcode.com/$1/day/$2)"

if [ ! -d "$PROBLEM_DIR" ]; then
	mkdir -p "$PROBLEM_DIR"
fi

if [ ! -f "$PROBLEM_DIR/input" ]; then
	SESSION_TOKEN=$(pass show coding/advent-of-code-session-cookie)
	curl --silent --fail "https://adventofcode.com/$1/day/$2/input" --cookie "session=${SESSION_TOKEN}" > "$PROBLEM_DIR/input"
fi

if [ -f "$PROBLEM_DIR/1.py" ]; then
	python3 "$PROBLEM_DIR/1.py" < "$PROBLEM_DIR/input" | pbcopy
	echo "---"
	pbpaste
fi

if [ -f "$PROBLEM_DIR/2.py" ]; then
	python3 "$PROBLEM_DIR/2.py" < "$PROBLEM_DIR/input" | pbcopy
	echo "---"
	pbpaste
fi
