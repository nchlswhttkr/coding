# [Advent of Code](https://adventofcode.com)

A seasonal coding challenge.

**2018** -
[1](#day-1-2018) /
[2](#day-2-2018) /
[3](#day-3-2018) /
[4](#day-4-2018) /
[5](#day-5-2018) /
[6](#day-6-2018) /
[7](#day-6-2018) /

**2019** -
[1](#day-1-2019) /

---

## 2018

### [Day 1, 2018](https://adventofcode.com/2018/day/1)

[**Part 1**](./2018/1/1.py)

Sum the inputs to find the eventual frequency.

[**Part 2**](./2018/1/2.py)

Continually iterate through the list of inputs, use some form of hash map to mark which frequencies have already been visited. Find the first repetition.

<details>
<summary>Answers</summary>
423

61126

</details>

### [Day 2, 2018](https://adventofcode.com/2018/day/2)

[**Part 1**](./2018/2/1.py)

Use a hash map/array to store the number of occurences of each character, increment counters for each word that meets criteria (contains a character with two/three occurences).

[**Part 2**](./2018/2/2.py)

Compare all words against each other, and build a string from the characters of the two words that match (same position and value). Output the longest string produced by this to find the closest matching words.

<details>
<summary>Answers</summary>
9139

uqcidadzwtnhsljvxyobmkfyr

</details>

### [Day 3, 2018](https://adventofcode.com/2018/day/3)

[**Part 1**](./2018/3/1.py)

Store a matrix representing the fabric, mark the number of cuts that cover each square. The final result is the number of squares with 2 or more cuts using it.

[**Part 2**](./2018/3/2.py)

Iterating over each cut, mark each square with the ID of the first cut to use it. Each cut is considered 'isolated' until another cut overlaps it. If/when a future cut runs over this square, mark both the ID of the first cut to use the square as well the ID of the current cut as no longer 'isolated'. After processing, only one cut is left isolated.

<details>
<summary>Answers</summary>
121163

943

</details>

### [Day 4, 2018](https://adventofcode.com/2018/day/4)

The input for the problem on this day needs to be sorted before use. Thankfully the input is presentable, and this can be done with a quick command (`sort input > sorted-input`).

[**Part 1**](./2018/4/1.py)

The approach for this is based off the assumption that a guard that falls asleep will wake up before their shift is over.

Iterating through each record in the now-sorted input, one of two scenarios will occur: The guards will change, or the current guard will fall asleep and later wake up. Knowing the guards on shift and they times during which they were asleep (from falling asleep to waking up), you can record how many times any particular guard was asleep on any particular minute.

Once this has been computed, you can find the guard who sleep the most and derive your answer from this.

[**Part 2**](./2018/4/2.py)

Use the same approach as above to compute the frequency with which each guard sleeps on each minute. Instead of finding the guard that sleeps the most, find the guard who is found sleeping the most on any particular minute of their shift, and return the corresponding answer.

<details>
<summary>Answers</summary>
39698

14920

</details>

### [Day 5, 2018](https://adventofcode.com/2018/day/5)

[**Part 1**](./2018/5/1.py)

To solve this problem, you will need to use a struct that supports backwards navigation, such as a double linked list or a stack, the latter being simpler to implement I went with that first.

Iterating through the polymer, characters are pushed to the stack so long as the do not react with the character at the top of the stack. Reacting characters will be clear the top of the stack.

[**Part 2**](./2018/5/2.py)

Apply the same approach as in part 1, trying with each letter removed (first _Aa_, then _Bb_, etc...). Find the smallest result.

Luckily, Python strings have a `translate` method for each character removal.

<details>
<summary>Answers</summary>
11754

4098

</details>

### [Day 6, 2018](https://adventofcode.com/2018/day/6)

[**Part 1**](./2018/6/1.py)

~~TODO: reduce tuples to use only region id~~

This is a slight improvement over the naive approach (iterate through each square of the grid and assign it to the closest point).

Instead, go through each point, which will be the center of its own region. Start from the region center (the current point) and expand out with a growing radius. Continue adding squares to the current region (if acceptable), until no new squares added to the region; You have reached the perimeter of the region. This is a case for an early exit.

This radiating pattern forms a skewed square, because the radius extends in Manhattan distance.

```
RADIUS = 0
. . . .
. . . .
. . O .
. . . .

RADIUS = 1
. . . .
. . X .
. X O X
. . X .

RADIUS = 2
. . X .
. X X X
X X O X
. X X X
```

Squares can be added to a region so long as there is no previously-covered region center that is closer.

Regions that reach the perimeter of the grid are disqualified, because they will extend infinitely.

Once all regions have been processed, find the largest valid (finite) region.

[**Part 2**](./2018/6/2.py)

Each square of the grid starts off with a budgeted distance of `10000`. Each point/region center draws on this. Acceptable regions start with

<details>
<summary>Answers</summary>
5975

38670

</details>

### [Day 7, 2018](https://adventofcode.com/2018/day/7)

[**Part 1**](./2018/7/1.py)

This requires a topological sort

<details>
<summary>Answers</summary>
ABLCFNSXZPRHVEGUYKDIMQTWJO
</details>

---

## 2019 

### [Day 1, 2019](https://adventofcode.com/2019/day/1)

[**Part 1**](./2019/01/1.py)

Sum the fuel volumes needed for each module.

[**Part 2**](./2019/01/1.py)

Sum the fuel volumes needed for each module, in addition to the fuel volumes needed for all significant fuel volumes (positive volumes).

<details>
<summary>Answers</summary>
3317659

4973616
</details>