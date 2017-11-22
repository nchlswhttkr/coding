# Sherlock and Parentheses

## Google Code Jam Kickstart 2017, Practise Round, Problem C

[Solution Discussion](##Solution)

[Problem Link](https://code.google.com/codejam/contest/6304486/dashboard#s=p2)

### Problem
Sherlock and Watson have recently enrolled in a computer programming course. Today, the tutor taught them about the balanced parentheses problem. A string **S** consisting only of characters ( and/or ) is balanced if:
 - It is the empty string _OR_
 - It has the form (**S**), where **S** is a balanced string _OR_
 - It has the form **S1S2**, where **S1** is a balanced string and **S2** is a balanced string.

Sherlock coded up the solution very quickly and started bragging about how good he is, so Watson gave him a problem to test his knowledge. He asked Sherlock to generate a string **S** of **L** + **R** characters, in which there are a total of **L** left parentheses ( and a total of **R** right parentheses ). Moreover, the string must have as many different balanced non-empty substrings as possible. (Two substrings are considered different as long as they start or end at different indexes of the string, even if their content happens to be the same). Note that **S** itself does not have to be balanced.

Sherlock is sure that once he knows the maximum possible number of balanced non-empty substrings, he will be able to solve the problem. Can you help him find that maximum number?

### Input
The first line of the input gives the number of test cases, **T**. **T** test cases follow. Each test case consists of one line with two integers: **L** and **R**.

#### Sample Input
```
3
1 0
1 1
3 2
```

### Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the answer, as described above.

#### Sample Output
```
Case #1: 0
Case #2: 1
Case #3: 3
```

*In Case 1, the only possible string is (. There are no balanced non-empty substrings.*

*In Case 2, the optimal string is (). There is only one balanced non-empty substring: the entire string itself.*

*In Case 3, both strings ()()( and (()() give the same optimal answer.*

*For the case ()()(, for example, the three balanced substrings are () from indexes 1 to 2, () from indexes 3 to 4, and ()() from indexes 1 to 4.*

### Limits
1 ≤ **T** ≤ 100

#### Small Dataset
0 ≤ **L** ≤ 20 \
0 ≤ **R** ≤ 20 \
1 ≤ **L** + **R** ≤ 20

#### Large Dataset
0 ≤ **L** ≤ 105 \
0 ≤ **R** ≤ 105 \
1 ≤ **L** + **R** ≤ 105

## Solution

Solution code can be found [here](./leader.py)

Since '()' is a valid substring, a long string of '()'s will produce the most valid substrings, as any arbitrary string of '()'s will count as a valid substring.

The next important thing to consider is that for any string, S, of N sequential '()'s, adding an additional '()' will create the following new substrings
 - Substring of length 1, the '()' in the new end position
 - Substring of length 2, from the old end position to the new end position
 - Substring of length N, consisting of N '()'s working backwards from the end position
 - etc...
The result of this is when a new '()' is added to the end of a valid string of length N, there will be N + 1 new substrings. Thus to calculate the total number of substrings, start with a empty string (0 valid substrings) and add the maximum possible number of '()' pairs with a rolling counter to hold the number of substrings.

The maximum possible number of pairs is given by the minimum of **L** and **R**. Therefore, the total number of substrings is equal to the sum of all integers ranging from 0 to minimum(**L**, **R**), inclusive.
