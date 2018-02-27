# GBus Count

## Google Code Jam Kickstart 2018, Practice Round, Problem A

[Solution Discussion](#solution)

[Problem Link](https://code.google.com/codejam/contest/4374486/dashboard#s=p0)

## Problem

There exists a straight line along which cities are built.

Each city is given a number starting from 1. So if there are 10 cities, city 1 has a number 1, city 2 has a number 2,... city 10 has a number 10.

Different buses (named GBus) operate within different cities, covering all the cities along the way. The cities covered by a GBus are represented as 'first_city_number last_city_number' So, if a GBus covers cities 1 to 10 inclusive, the cities covered by it are represented as '1 10'

We are given the cities covered by all the GBuses. We need to find out how many GBuses go through a particular city.

## Input

The first line contains the number of test cases (**T**), after which **T** cases follow each separated from the next with a blank line.

For each test case,

* The first line contains the number of GBuses, **N**.
* The second line contains the cities covered by them in the form `a1 b1 a2 b2 a3 b3...an bn`, where GBus1 covers cities numbered from `a1` to `b1`, GBus2 covers cities numbered from `a2` to `b2`, up to N GBuses.

Next line contains the number of cities for which GBus count needs to be determined, **P**.
The below **P** lines contain different city numbers.

## Output

For each test case, output one line containing `Case #Ti:` followed by **P** numbers corresponding to the number of cities each of those **P** GBuses goes through.

## Limits

```
1 <= T <= 10
```

`ai` and `bi` will always be integers.

### Small dataset

```
1 <= N <= 50
1 <= ai <= 500, 1 <= bi <= 500
1 <= P <= 50
```

### Large dataset

```
1 <= N <= 500
1 <= ai <= 5000, 1 <= bi <= 5000
1 <= P <= 500
```

## Sample

```
INPUT

2
4
15 25 30 35 45 50 10 20
2
15
25

10
10 15 5 12 40 55 1 10 25 35 45 50 20 28 27 35 15 40 4 5
3
5
10
27

---

OUTPUT

Case #1: 2 1
Case #2: 3 3 4
```

### Explanation

2 GBuses go through city 15 (GBus1 [15 25] and GBus4 [10 20])
1 GBus goes through city 25 (GBus1 [15 25])

## Solution

This appears to be classic 'soft start' question.

We can check whether a bus passes through a city with a simple range check. That is, bus _i_ passes through city _p_ so long as it is between the start and end of the bus' journey.

A<sub>i</sub> <= _p_ <= B<sub>i</sub>

Overall time complexity should only be O(PxN), for P city checks and N buses.
