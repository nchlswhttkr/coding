#!/bin/bash

set -euo pipefail

# $1    Year, for example 2020
# $2    Day, for example 1

# Prepare working space, assuming the usual Python shenanigans
PROBLEM_DIR="advent-of-code/$1/$2"
if [ ${#2} == "1" ]; then
    PROBLEM_DIR="advent-of-code/$1/0$2" # hacky zero padding, bleh
fi

if [ ! -f advent-of-code/cookie.txt ]; then
	read -rp "Session token? > " SESSION_TOKEN
	echo "${SESSION_TOKEN}" > advent-of-code/cookie.txt
else
	SESSION_TOKEN=$(cat advent-of-code/cookie.txt)
fi

if [ ! -d "$PROBLEM_DIR" ]; then
	mkdir -p "$PROBLEM_DIR"
	curl --silent --fail "https://adventofcode.com/$1/day/$2/input" --cookie "session=${SESSION_TOKEN}" > "$PROBLEM_DIR/input"
	code "$PROBLEM_DIR/1.py" "$PROBLEM_DIR/2.py"

	if [[ $(uname -s) == Darwin ]]; then
		osascript -e "
		tell application \"Safari\"
			activate
			make new document with properties { URL: \"https://adventofcode.com/$1/day/$2\" }
		end tell
		" > /dev/null
	fi
else
	[ -f "$PROBLEM_DIR/1.py" ] && python3 "$PROBLEM_DIR/1.py" < "$PROBLEM_DIR/input"
	[ -f "$PROBLEM_DIR/2.py" ] && python3 "$PROBLEM_DIR/2.py" < "$PROBLEM_DIR/input"
fi
