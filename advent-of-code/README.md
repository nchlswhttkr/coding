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
[2](#day-2-2019) /
[3](#day-3-2019) /
[4](#day-4-2019) /
[5](#day-5-2019) /
[6](#day-6-2019) /
[7](#day-7-2019) /
[8](#day-8-2019) /
[9](#day-9-2019) /
[10](#day-10-2019) /
[11](#day-11-2019) /
[12](#day-12-2019) /

**2020** -
[1](#day-1-2020) /
[2](#day-2-2020) /
[3](#day-3-2020) /
[4](#day-4-2020) /
[5](#day-5-2020) /

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

[**Part 2**](./2019/01/2.py)

Sum the fuel volumes needed for each module, in addition to the fuel volumes needed for all significant fuel volumes (positive volumes).

<details>
<summary>Answers</summary>
3317659

4973616

</details>

### [Day 2, 2019](https://adventofcode.com/2019/day/2)

You don't need to worry about encountering bad opcodes or wrapping back around to the start of the program.

[**Part 1**](./2019/02/1.py)

Implement the program as specified, processing the opcodes `0`, `1` and `99`. Don't forget to set the program to the "1202 alarm state".

The tricky case is where you modify the current opcode and accidentally perform a second instruction. For example, `1,0,0,0,99` would produce `4` if you first changed the opcode to `2` and then did multiplication. You can fix this by storing the opcode in a variable, I just used an else/if.

[**Part 2**](./2019/02/2.py)

Using your code from part 1, brute force all possible verb and noun combinations for the program until you find one which outputs the target. As the problem says, make sure your program is reset after each run.

<details>
<summary>Answers</summary>
8017076

3146

</details>

### [Day 3, 2019](https://adventofcode.com/2019/day/3)

You can do this more efficiently with a hash map rather than a grid, this was just easier for me to reason with.

You could also consider storing the paths of the two wires in sorted arrays of coordinates. You could process this in a similar way to a merge sort, with a pointer for each array that only needs to iterate through their respective array once.

Turns out you don't need to worry about assumptions like whether the wires always cross, or deal with the edge case where they cross over the central port.

[**Part 1**](./2019/03/1.py)

Treat the board as a cartesian plane, you can find the size with an initial pass. For this part, I made an array of `false`s the size of the board.

Starting from `(0, 0)`, place the first wire. Lay out the wire by marking `true` on each coordinate you cover. Remember to _mark the path between corners_, not just the corners themselves.

Now laying out the second wire, calculate the distance from the origin every time you find a `true` coordinate. Report the shortest distance found.

Make sure you don't accidentally include the wires when they originate from the central port.

[**Part 2**](./2019/03/2.py)

Now we're using steps taken (length) as our metric instead of cartesian distance from central port.

Similar to the first part, except now you have to record the distance (as in length of wire) from the central port for the first wire on your board (`0 1 2 ... N` instead of `true`/`false`). Make sure you don't overwrite a shorter distance when laying out the first wire.

The procedure for laying the second wire should be similarly adjusted, recording the length of the two wires when they intersect. Report the shortest combined length needed to intercept.

<details>
<summary>Answers</summary>
248

28580

</details>

### [Day 4, 2019](https://adventofcode.com/2019/day/4)

[**Part 1**](./2019/04/1.py)

Brute force check each number in the range.

[**Part 2**](./2019/04/2.py)

Same as part 1. If the string doesn't change when it is sorted, then it is in ascending order. If you put each character in a hash map, as long as 2 exists in the value table then a pair of sequential characters exists (since the digits are ordered).

<details>
<summary>Answers</summary>
1748

1180

</details>

### [Day 5, 2019](https://adventofcode.com/2019/day/5)

Note each day has different input because they examine different "systems", in this case `1` and `5` for parts 1 and 2 respectively.

[**Part 1**](./2019/05/1.py)

Adapt your solution from day 2. I introduced the `interpret_args()` function to find the "memory" locations that each argument points to, since you need to consider the mode of the argument as well. You can use the handy snippet `X // 10 ** N % 10` to find the `N + 1`<sup>th</sup> digit of a given number `X`.

[**Part 2**](./2019/05/2.py)

Extending the solution from part 1 with extra opcodes and their accompanying logic. Luckily, you can reuse the same `interpret_args()` logic without adjusting it.

<details>
<summary>Answers</summary>
13210611

584126

</details>

### [Day 6, 2019](https://adventofcode.com/2019/day/6)

[**Part 1**](./2019/06/1.py)

Each planet either orbits nothing or orbits one other planet (a parent-child) relationship. Record each planet's planet if one exists. Calculate the total orbit count by measuring the number of parents and transitive parents for each planet.

[**Part 2**](./2019/06/2.py)

Build two lists from `YOU` and `SAN` that go all the way up to the root planet. Find the closest related common parent. The number of "orbital transfers" or jumps will be the length of the paths to the common parent from the two planets.

<details>
<summary>Answers</summary>
186597

412

</details>

### [Day 7, 2019](https://adventofcode.com/2019/day/7)

[**Part 1**](./2019/07/1.py)

Set up 5 Intcode machine in series, run for each permutation for each thruster signal.

[**Part 2**](./2019/07/2.py)

Set up some form of buffer for each Intcode machine (I used queues). As a machine runs, it should write to the next machine's buffer and read from its own buffer.

Run the first machine until it tries to read from an empty buffer. Run the second machine until it tries to read from an empty buffer. Keep repeating this feedback loop until a machine halts.

<details>
<summary>Answers</summary>
338603

63103596

</details>

### [Day 8, 2019](https://adventofcode.com/2019/day/8)

[**Part 1**](./2019/08/1.py)

Do as specified.

[**Part 2**](./2019/08/2.py)

No need to build layers here, just stored the image as one long string.

Begin with a transparent image (all `2`s). For every character in the string, find out which cell of the image it belongs to. If this cell is currently transparent, colour it appropriately.

Since we have gone from the start of the string and only colour transparent cells, coloured cells from earlier layers will not be overwritten.

<details>
<summary>Answers</summary>
1452

PHPEU

</details>

### [Day 9, 2019](https://adventofcode.com/2019/day/9)

[**Part 1**](./2019/09/1.py)

Update to your Intcode program to allow reading from larger memory sizes. I implemented a dictionary-like object that returned 0 instead `KeyError`s for unaddressed memory.

[**Part 2**](./2019/09/2.py)

Run the program with the new input.

<details>
<summary>Answers</summary>
2427443564

87221

</details>

### [Day 10, 2019](https://adventofcode.com/2019/day/10)

[**Part 1**](./2019/10/1.py)

Comparing each asteroid against every other asteroid, store the angle between them as an X and Y step. Make sure identical angles with different step sizes are not counted twice (ie `(1, 1)` and `(2, 2)` have the same 45deg angle). In that case, the closer asteroid to our current asteroid has a smaller step distance and is blocked the further asteroid.

You only need to compare each asteroid with each asteroid after it, because the step from B to A will just be the step from A to B reversed.

[**Part 2**](./2019/10/2.py)

Keep the angle-preserving component and instead build a list of asteroids along a certain angle, sorted from furthest to closest.

Sort the angles of your origin asteroid, starting from 0deg to 360deg clockwise (that's why I did all the stuff with `get_angle_from_key()`). Loop through the list of asteroid at each angle, "vaporising" the closest one by popping it from the stack.

<details>
<summary>Answers</summary>
263

1110

</details>

## [Day 11, 2019](https://adventofcode.com/2019/day/11)

It was at this point that I learned about the fantastic defaultdict in Python.

[**Part 1**](./2019/11/1.py)

Adapt your Intcode program to traverse and colour the board as described.

My program writes to a buffer, and every time there are at least two outputs in the buffer it uses the first two to colour and turn as instructed.

[**Part 2**](./2019/11/2.py)

Record the size of the board the program covers (furthest distances from origin in X and Y axes), and use this generate your image. Rerun with the new white starting square.

<details>
<summary>Answers</summary>
2082

FARBCFJK

</details>

## [Day 12, 2019](https://adventofcode.com/2019/day/12)

[**Part 1**](./2019/12/1.py)

Not too much to add here, just calculate the velocity change for each pair of moons and then update their positions afterwards.

[**Part 2**](./2019/12/2.py)

Each dimension is independent. Information about the X dimension has no bearing on the Y or Z dimensions.

Finding the number of steps in cycle for the entire system would take unreasonably long. However, it's possible to find the number of steps for a cycle in each dimension. The period of the system's cycle will be the lowest common multiple of the periods of each dimension's cycle. That is, when the moons return to their original position in the X, Y, and Z dimension at the same time, the system has completed a cycle.

<details>
<summary>Answers</summary>
7758

354540398381256

</details>

## [Day 1, 2020](https://adventofcode.com/2020/day/1)

[**Part 1**](./2020/01/1.py)

As always, we start with an introductory problem. You could sum each pair of numbers to find 2020 (O(**N**<sup>2</sup>) is fine), or you could use a hash table/set to quickly determine whether a number's counterpart has appeared.

I initially used Python's dictionary structure, but it turns out they also support [plain sets](https://docs.python.org/3/library/stdtypes.html#set), which is a little cleaner and (I assume) faster.

[**Part 2**](./2020/01/2.py)

Finding a trio takes a little longer, but given we're only dealing with 200 numbers we don't need to concern ourselves too much with performance.

The do a little better than O(**N**<sup>3</sup>), we can use a set again to record which numbers have previously appeared. With each new number, try adding it with each existing number, subtracting the sum from 2020. If the difference has _also_ appeared previously, then we have our trio of numbers.

<details>
<summary>Answers</summary>
960075

212900130

</details>

## [Day 2, 2020](https://adventofcode.com/2020/day/2)

[**Part 1**](./2020/02/1.py)

Break down the input string for necessary arguments, count which password abide by the rule. Conveniently, Python has standard functions for counting substrings/characters.

[**Part 2**](./2020/02/2.py)

Reuse the previous code, but check that the character appears exactly once. You're looking for the XOR operator for this one.

<details>
<summary>Answers</summary>
474

745

</details>

## [Day 3, 2020](https://adventofcode.com/2020/day/3)

[**Part 1**](./2020/03/1.py)

The straightforward approach for me was to just let this iteration run. Go through each row, updating your position and checking for a tree. Each step is just an offset from the last position, in this case (+1, +3).

If you want to be fancy, you can compute the X-offset as a product of the Y-offset. If you're **N** rows down from the start, you're 3**N** steps right from the origin.

Remember that the map wraps around!

[**Part 2**](./2020/03/2.py)

Runs the iteration several times for each slope.

<details>
<summary>Answers</summary>
207

2655892800

</details>

## [Day 4, 2020](https://adventofcode.com/2020/day/4)

[**Part 1**](./2020/04/1.py)

Iterate through each passport, skipping passports that lack a required field. You only need to check for the key's presence at this point!

[**Part 2**](./2020/04/2.py)

Extend your part 1 solution to check that the value for each field meets requirements. Since each field is independent, you can do these checks at the same time that you verify a field's presence.

Python's `lambda` keyword is great for quickly declaring these small functions.

**Bonus**: My [very ugly 5-line solution](./2020/04/2.bad.py) for part 2.

<details>
<summary>Answers</summary>
256

198

</details>

## [Day 5, 2020](https://adventofcode.com/2020/day/5)

[**Part 1**](./2020/05/1.py)

You're making a binary converter! The row/column numbers are denoted by their own binary digits (`B`/`F` and `R`/`L` respectively). The row number needs to be multiplied by 8 (2<sup>3</sup>) because the last three digits denote the column.

If your language supports string to integer conversion with different bases (in this case, 2), you can convert your seat to a string of `1`s and `0`s before parsing it to an integer.

[**Part 2**](./2020/05/2.py)

In addition to finding the highest occupied seat ID, record which seat IDs you've seen. Afterwards, decrementing from the highest occupied seat until you find an unoccupied seat will give you your answer.

<details>
<summary>Answers</summary>
996

671

</details>
