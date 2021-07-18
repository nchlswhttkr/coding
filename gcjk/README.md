# Google Code Jam Kickstart

A coding challenge for students, by Google

**2017 Practice Round** - [Country Leader](#country-leader) / [Vote](#vote) / [Sherlock and Parentheses](#sherlock-and-parentheses) \
**2017 Round A** - [Square Counting](#square-counting) \
**2018 Practice Round** - [GBus Count](#gbus-count) / [Googol String](#googol-string) \
**2018 Round G** - [Product Triplets](#product-triplets)

---

### [Country Leader](https://code.google.com/codejam/contest/6304486/dashboard#s=p0)

Nothing too interesting here, store each new character if it has not already appeared.

A more elegant method would be to sort the incoming string and compare adjacent characters, but with a maximum string length of 20, this has no real efficiency payoff.

[Solution](./country-leader)

### [Vote](https://code.google.com/codejam/contest/6304486/dashboard#s=p1)

This is an example of the [ballot problem](https://en.wikipedia.org/wiki/Bertrand%27s_ballot_theorem).

Put simply, if we place all the votes in a cycle, and pair every vote for B with a vote for A, then as long as there is at least one vote for A before this sequence of AB pairs, then A will have at least one vote (thus, leading) more at any point of this sequence. By preceding these pairs by all other As, and starting the cycle at any of these unpaired As, then I will have a sequence of votes such that A is always leading.

For example, if I know there will be 6 votes for A and 3 votes for B, then my cycle would resemble something along the lines of `...AAAABABAB...`. If I start at one of the first 3 As, then A will always be leading, otherwise their lead is not certain. Thus, there is a `3 / 9` chance that A will always lead.

There are (A + B) possible points to start the cycle at, and (A - B) unpaired As to start an acceptable sequence at, then the probability of having an acceptable sequence, that occurs uniformly at random, is given by (A - B) / (A + B).

[Solution](./vote)

### [Sherlock and Parentheses](https://code.google.com/codejam/contest/6304486/dashboard#s=p2)

Since '()' is a valid substring, a long string of '()'s will produce the most valid substrings, as any arbitrary string of '()'s will count as a valid substring.

The next important thing to consider is that for any string, S, of N sequential '()'s, adding an additional '()' will create the following new substrings

- Substring of length 1, the '()' in the new end position
- Substring of length 2, from the old end position to the new end position
- etc...
- Substring of length N, consisting of N '()'s working backwards from the end position

The result of this is when a new '()' is added to the end of a valid string of length N, there will be N + 1 new substrings. Thus to calculate the total number of substrings, start with a empty string (0 valid substrings) and add the maximum possible number of '()' pairs with a rolling counter to hold the number of substrings.

The maximum possible number of pairs is given by the minimum of **L** and **R**. Therefore, the total number of substrings is equal to the sum of all integers ranging from 0 to minimum(**L**, **R**), inclusive.

[Solution](./sherlock-and-parentheses)

### [Square Counting](https://code.google.com/codejam/contest/8284486/dashboard#s=p0)

First we must consider how many squares we can fit inside a rectangular space. A squares NxN pins in size placed in the top left corner of a rectangle of size **C**x**R**, where N <= **C** <= **R**, there are (**C** - N) empty spaces to the right, so there are (**C** - N + 1) possible horizontal positions to place a square within the board, and likewise (**R** - N + 1) possible vertical positions. Thus for a square of size NxN on a board of size **C**x**R**, there are (**C** - N + 1) \* (**R** - N + 1) possible positions to place a square of side length N.

However, there is also the case where squares are placed on an angle. Consider the following boards. There exists a square when all the X points are joined.

```
X  0  0  X      0  X  0  0      0  0  X  0
0  0  0  0      0  0  0  X      X  0  0  0
0  0  0  0      X  0  0  0      0  0  0  X
X  0  0  X      0  0  X  0      0  X  0  0
```

The important detail to note here is that angled squares can only exist within a larger containing square.

In the case of a containing square of side length N, there are N - 1 possible squares that can be made that have their vertices along the perimeter of their containing squares, including one that occupies the full space.

Combining this with our earlier equations, we can say that the total number of unique squares is the number of possible possible positions of a square on the board, multiplied by the number of possible subsquare arrangements that can fit into each of these squares.

```
WHERE N RANGES FROM 2 -> MINIMUM(R, C)

(**R** - N + 1) * (**C** - N + 1) * (N - 1)
```

While this works for small values of **R** and **C**, running an iteration for the minimum of 991312703 and 818140587, as in the large question set, is incredibly slow. Fortunately there is a mathematical approach.

The key thing to note is that (**R** - N + 1), (**C** - N + 1) and (N - 1) all increase/decrease by increments of N, with N ranging 2 to the minimum of **R** and **C**, thus we can make a mathematical series from this. We replace **R** and **C** with A and B, such that A >= B and let i = N - 1, where i ranges from 1 to B - 1. We now have the following series.

```
A = MAXIMUM(R, C)
B = MINIMUM(R, C)
WHERE i RANGES FROM 1 -> (B - 1)

(**R** - N + 1) * (**C** - N + 1) * (N - 1) == (A - i) * (B - i) * i
                                            == (A * B) * i - (A + B) * i^2 + i^3
```

This can be expanded into a polynomial form, and [Faulhaber's Formula](https://en.wikipedia.org/wiki/Faulhaber's_formula#Examples) can be used to obtain a result for the series without needing iteration!

[Solution](./square-counting)

### [GBus Count](https://code.google.com/codejam/contest/4374486/dashboard#s=p0)

This appears to be classic 'soft start' question.

We can check whether a bus passes through a city with a simple range check. That is, bus _i_ passes through city _p_ so long as it is between the start and end of the bus' journey.

A<sub>i</sub> <= _p_ <= B<sub>i</sub>

Overall time complexity should only be O(PxN), for P city checks and N buses.

[Solution](./gbus-count)

### [Googol String](https://code.google.com/codejam/contest/4374486/dashboard#s=p1)

I took a while to get my head around this one, but overall it's a great question that involves a little pattern analysis.

Brute forcing this is not a good idea, as you will need to generate the S<sub>googol</sub> up to 10<sup>18</sup> characters.

To solve this, I made the following deductions

- Since the left and right substrings about the middle zero are reversed and have their bits flipped, a character _K_ steps to the right of the middle zero will be the same as the character _K_ steps to the left of the middle zero, albeit with its bits flipped
- Since a string S<sub>N</sub> has a length equal to `2^N - 1`, and a zero is added to the end of this when creating S<sub>N+1</sub>, then the character in the 2^N<sup>th</sup> will be a zero. This can be extended to say that all positions that are a power of 2 in theS<sub>googol</sub> string will be 0 (1, 2, 4, 8, 16...). Funnily enough, these zeroes end up being middle zeroes for each respective strings

Thus to calculate the character at position _K_ of S<sub>googol</sub>, we calculate the offset from the nearest, smallest middle zero. We calculate this using a log function with base 2, and finding the difference.

If we have a difference of 0, then our character is a middle zero, and we can return that. Otherwise, we know that it is to the right of middle zero, and will have a corresponding position offset to the left, but a bit flip has taken place. Knowing this, we now find how many bit flips have taken place to produce the target character offset to the left of the middle zero.

I wrote a recursive function for this, that tracks the total number of times the bit has been flipped, and return this number once we hit a middle zero. Since middle zeros have been inserted into the string instead of created through reversing a string and flipping its bits, we know no earlier bit flips took place. Because some substrings will be flipped again and again because of their position in the string, the final answer is the remainder when the total number of flips that have taken place is divided by 2.

Overall time complexity comes out to about O(log2(K)), and this recursive approach should also allow for optimisation with tail calls in certain languages, avoiding issues with the worst case when K is incredibly large, and is always offset from the middle zero with each call.

_Perhaps I should rewrite my solution in C++ to test/demonstrate this, watch this space!_

[Solution](./googol-string)

### [Product Triplets](https://code.google.com/codejam/contest/5374486/dashboard#s=p0)

The naive solution here is to find all products of A<sub>x</sub> and A<sub>y</sub> that equal A<sub>z</sub>, but this is O(N<sup>3</sup>) and we can do better (especially when N <= 7000).

A minor improvement we can make off the bat is to sort the array. We can leverage the fact that the product of two nonzero integers will be at least as big as the largest integerfor now, and address the scenario where one or both operands are zero later.

If we process the sorted array in a descending order, then the product of A<sub>i</sub> and A<sub>j</sub> will always be at least as big as A<sub>i</sub>. Knowing the numbers that have preceded A<sub>i</sub>, we note the number of times our target product has appeared, which indicates a satisfactory triplet. We only include numbers that have already been processed, since in the case where A<sub>j</sub> is 1 we want to avoid counting the same triplet multiple times (remembering the problem statement).

In the case where an operand is 0, we calculate the number of triplets where 0 x 0 = 0 and 0 x A<sub>x</sub> = 0 (A<sub>x</sub> is a nonzero integer) using selection from A. It's easy to find how many zero/nonzero integers are in A since it is sorted.

[Solution](./product-triplets)
