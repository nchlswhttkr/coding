# Googol String

## Google Code Jam Kickstart 2018, Practice Round, Problem B

[Solution Discussion](#solution)

[Problem Link](https://code.google.com/codejam/contest/4374486/dashboard#s=p1)

## Problem

A "0/1 string" is a string in which every character is either 0 or 1. There are two operations that can be performed on a 0/1 string:

* **switch**: Every 0 becomes 1 and every 1 becomes 0. For example, "100" becomes "011".
* **reverse**: The string is reversed. For example, "100" becomes "001".

Consider this infinite sequence of 0/1 strings:

S0 = ""

S1 = "0"

S2 = "001"

S3 = "0010011"

S4 = "001001100011011"

...

SN = SN-1 + "0" + switch(reverse(SN-1)).

You need to figure out the Kth character of Sgoogol, where googol = 10<sup>100</sup>.

## Input

The first line of the input gives the number of test cases, T. Each of the next T lines contains a number K.

## Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the Kth character of S<sub>googol</sub>.

## Limits

1 ≤ T ≤ 100

### Small dataset

1 ≤ K ≤ 10<sup>5</sup>

### Large dataset

1 ≤ K ≤ 10<sup>18</sup>

## Sample

```
Input

4
1
2
3
10

Output

Case #1: 0
Case #2: 0
Case #3: 1
Case #4: 0
```

## Solution

I took a while to get my head around this one, but overall it's a great question that involves a little pattern analysis.

Brute forcing this is not a good idea, as you will need to generate the S<sub>googol</sub> up to 10<sup>18</sup> characters.

To solve this, I made the following deductions

* Since the left and right substrings about the middle zero are reversed and have their bits flipped, a character _K_ steps to the right of the middle zero will be the same as the character _K_ steps to the left of the middle zero, albeit with its bits flipped
* Since a string S<sub>N</sub> has a length equal to `2^N - 1`, and a zero is added to the end of this when creating S<sub>N+1</sub>, then the character in the 2^N<sup>th</sup> will be a zero. This can be extended to say that all positions that are a power of 2 in theS<sub>googol</sub> string will be 0 (1, 2, 4, 8, 16...). Funnily enough, these zeroes end up being middle zeroes for each respective strings

Thus to calculate the character at position _K_ of S<sub>googol</sub>, we calculate the offset from the nearest, smallest middle zero. We calculate this using a log function with base 2, and finding the difference.

If we have a difference of 0, then our character is a middle zero, and we can return that. Otherwise, we know that it is to the right of middle zero, and will have a corresponding position offset to the left, but a bit flip has taken place. Knowing this, we now find how many bit flips have taken place to produce the target character offset to the left of the middle zero.

I wrote a recursive function for this, that tracks the total number of times the bit has been flipped, and return this number once we hit a middle zero. Since middle zeros have been inserted into the string instead of created through reversing a string and flipping its bits, we know no earlier bit flips took place. Because some substrings will be flipped again and again because of their position in the string, the final answer is the remainder when the total number of flips that have taken place is divided by 2.

Overall time complexity comes out to about O(log2(K)), and this recursive approach should also allow for optimisation with tail calls in certain languages, avoiding issues with the worst case when K is incredibly large, and is always offset from the middle zero with each call.

_Perhaps I should rewrite my solution in C++ to test/demonstrate this, watch this space!_
