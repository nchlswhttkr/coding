# Advent of Code

[Website](https://adventofcode.com)

A seasonal coding challenge.

## 2018

Choose a day

[1](#day-1-2018) /
[2](#day-2-2018) /

### Day 1, 2018

[See code](./2018/1)

**Part 1**

<details>
<summary>Show Answer</summary>
423
</details>

Sum the inputs to find the eventual frequency.

**Part 2**

<details>
<summary>Show Answer</summary>
61126
</details>

Continually iterate through the list of inputs, use some form of hash map to mark which frequencies have already been visited. Find the first repetition.

### Day 2, 2018

[See code](./2018/2)

**Part 1**

<details>
<summary>Show Answer</summary>
9139
</details>

Use a hash map/array to store the number of occurences of each character, increment counters for each word that meets criteria (contains a character with two/three occurences).

**Part 2**

<details>
<summary>Show Answer</summary>
uqcidadzwtnhsljvxyobmkfyr
</details>

Compare all words against each other, and build a string from the characters of the two words that match (same position and value). Output the longest string produced by this to find the closest matching words.
