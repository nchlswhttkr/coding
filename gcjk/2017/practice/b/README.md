# Vote

## Google Code Jam Kickstart 2017, Practice Round, Problem B

[Solution Discussion](#solution)

[Problem Link](https://code.google.com/codejam/contest/6304486/dashboard#s=p1)

### Problem
A and B are the only two candidates competing in a certain election. We know from polls that exactly **N** voters support A, and exactly **M** voters support B. We also know that **N** is greater than **M**, so A will win.

Voters will show up at the polling place one at a time, in an order chosen uniformly at random from all possible (**N** + **M**)! orders. After each voter casts their vote, the polling place worker will update the results and note which candidate (if any) is winning so far. (If the votes are tied, neither candidate is considered to be winning.)

What is the probability that A stays in the lead the entire time -- that is, that A will always be winning after every vote?

### Input
The input starts with one line containing one integer **T**, which is the number of test cases. Each test case consists of one line with two integers **N** and **M**: the numbers of voters supporting A and B, respectively.

#### Sample Input
```
2
2 1
1 0
```

### Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the probability that A will always be winning after every vote.

y will be considered correct if y is within an absolute or relative error of 10-6 of the correct answer.

#### Sample Output
```
Case #1: 0.33333333
Case #2: 1.00000000
```

*In sample case #1, there are 3 voters. Two of them support A -- we will call them A1 and A2 -- and one of them supports B. They can come to vote in six possible orders: A1 A2 B, A2 A1 B, A1 B A2, A2 B A1, B A1 A2, B A2 A1. Only the first two of those orders guarantee that Candidate A is winning after every vote. (For example, if the order is A1 B A2, then Candidate A is winning after the first vote but tied after the second vote.) So the answer is 2/6 = 0.333333...*

*In sample case #2, there is only 1 voter, and that voter supports A. There is only one possible order of arrival, and A will be winning after the one and only vote.*

### Limits
1 ≤ **T** ≤ 100

#### Small Dataset
0 ≤ **M** < **N** ≤ 10

#### Large Dataset
0 ≤ **M** < **N** ≤ 2000

## Solution

Solution code can be found [here](./vote.py)

This is an example of the [ballot problem](https://en.wikipedia.org/wiki/Bertrand%27s_ballot_theorem).

Put simply, if we place all the votes in a cycle, and pair every vote for B with a vote for A, then as long as there is at least one vote for A before this sequence of AB pairs, then A will have at least one vote (thus, leading) more at any point of this sequence. By preceding these pairs by all other As, and starting the cycle at any of these unpaired As, then I will have a sequence of votes such that A is always leading.

For example, if I know there will be 6 votes for A and 3 votes for B, then my cycle would resemble something along the lines of ```...AAAABABAB...```. If I start at one of the first 3 As, then A will always be leading, otherwise their lead is not certain. Thus, there is a ```3 / 9``` chance that A will always lead.

There are (A + B) possible points to start the cycle at, and (A - B) unpaired As to start an acceptable sequence at, then the probability of having an acceptable sequence, that occurs uniformly at random, is given by (A - B) / (A + B) 
