# Advent of Code

[Website](https://adventofcode.com)

A seasonal coding challenge.

## 2018

Choose a day

[1](#day-1-2018) /
[2](#day-2-2018) /
[3](#day-3-2018) /
[4](#day-4-2018) /
[5](#day-5-2018) /

### Day 1, 2018

[See problems](https://adventofcode.com/2018/day/1)

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

[See problems](https://adventofcode.com/2018/day/2)

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

### Day 3, 2018

[See problems](https://adventofcode.com/2018/day/3)

[See code](./2018/3)

**Part 1**

<details>
<summary>Show Answer</summary>
121163
</details>

Store a matrix representing the fabric, mark the number of cuts that cover each square. The final result is the number of squares with 2 or more cuts using it.

**Part 2**

<details>
<summary>Show Answer</summary>
943
</details>

Iterating over each cut, mark each square with the ID of the first cut to use it. Each cut is considered 'isolated' until another cut overlaps it. If/when a future cut runs over this square, mark both the ID of the first cut to use the square as well the ID of the current cut as no longer 'isolated'. After processing, only one cut is left isolated.

### Day 4, 2018

[See problems](https://adventofcode.com/2018/day/4)

[See code](./2018/4)

The input for the problem on this day needs to be sorted before use. Thankfully the input is presentable, and this can be done with a quick command (`sort input > sorted-input`).

**Part 1**

<details>
<summary>Show Answer</summary>
39698
</details>

The approach for this is based off the assumption that a guard that falls asleep will wake up before their shift is over.

Iterating through each record in the now-sorted input, one of two scenarios will occur: The guards will change, or the current guard will fall asleep and later wake up. Knowing the guards on shift and they times during which they were asleep (from falling asleep to waking up), you can record how many times any particular guard was asleep on any particular minute.

Once this has been computed, you can find the guard who sleep the most and derive your answer from this.

**Part 2**

<details>
<summary>Show Answer</summary>
14920
</details>

Use the same approach as above to compute the frequency with which each guard sleeps on each minute. Instead of finding the guard that sleeps the most, find the guard who is found sleeping the most on any particular minute of their shift, and return the corresponding answer.

### Day 5, 2018

[See problems](https://adventofcode.com/2018/day/5)

[See code](./2018/5)

**Part 1**

<details>
<summary>Show Answer</summary>
11754
</details>

To solve this problem, you will need to use a struct that supports backwards navigation, such as a double linked list or a stack, the latter being simpler to implement I went with that first.

Iterating through the polymer, characters are pushed to the stack so long as the do not react with the character at the top of the stack. Reacting characters will be clear the top of the stack.

**Part 2**

<details>
<summary>Show Answer</summary>
4098
</details>

Apply the same approach as in part 1, trying with each letter removed (first _Aa_, then _Bb_, etc...). Find the smallest result.

Luckily, Python strings have a `translate` method for each character removal.
