# Square Counting

## Google Code Jam Kickstart 2017, Round A, Problem A

[Solution Discussion](#solution)

[Problem Link](https://code.google.com/codejam/contest/8284486/dashboard#s=p0)

### Problem
Mr. Panda has recently fallen in love with a new game called Square Off, in which players compete to find as many different squares as possible on an evenly spaced rectangular grid of dots.

To find a square, a player must identify four dots that form the vertices of a square. Each side of the square must have the same length, of course, but it does not matter what that length is, and the square does not necessarily need to be aligned with the axes of the grid. The player earns one point for every different square found in this way. Two squares are different if and only if their sets of four dots are different.

Mr. Panda has just been given a grid with **R** rows and **C** columns of dots. How many different squares can he find in this grid? Since the number might be very large, please output the answer modulo 109 + 7 (1000000007).

See [below](#sample_cases) for sample cases of a valid square.

### Input
The first line of the input gives the number of test cases, **T**. **T** lines follow. Each line has two integers **R** and **C**: the number of dots in each row and column of the grid, respectively.

#### Sample Input
```
4
2 4
3 4
4 4
1000 500
```

### Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of different squares can be found in the grid.

#### Sample Output
```
Case #1: 3
Case #2: 10
Case #3: 20
Case #4: 624937395
```

###Limits
1 ≤ **T** ≤ 100

#### Small Dataset
2 ≤ **R** ≤ 1000
2 ≤ **C** ≤ 1000

#### Large Dataset
2 ≤ **R** ≤ 109
2 ≤ **C** ≤ 109

### Sample Cases

![](https://code.google.com/codejam/contest/images/?image=sample1.png&p=5680283126857728&c=8284486)

![](https://code.google.com/codejam/contest/images/?image=sample2.png&p=5680283126857728&c=8284486)

![](https://code.google.com/codejam/contest/images/?image=sample3.png&p=5680283126857728&c=8284486)

## Solution

Solution code can be found [here](./squares.py)

First we must consider how many squares we can fit inside a rectangular space. A squares NxN pins in size placed in the top left corner of a rectangle of size **C**x**R**, where N <= **C** <= **R**, there are (**C** - N) empty spaces to the right, so there are (**C** - N + 1) possible horizontal positions to place a square within the board, and likewise (**R** - N + 1) possible vertical positions. Thus for a square of size NxN on a board of size **C**x**R**, there are (**C** - N + 1) * (**R** - N + 1) possible positions to place a square of side length N.

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