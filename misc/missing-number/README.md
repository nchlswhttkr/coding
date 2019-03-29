# Missing Number

Shoutout to @harsilpatel for this one!

## Problem

You are given an array of length **N** - 1 of integers, where each element is a unique integer in the range 1 ... **N**. That is, the array contains all integers from 1 ... **N** bar one in random order.

In O(**N**) time and O(1) auxillary space, find the integer that is missing.

## Solution

A simple solution would be to sort the array and iterate until we find a mismatch, this does not meet the problem constraints.

Instead, because we can calculate the sum of all integers in the range 1 ... **N**, and we can also sum the array, the difference of these two sums will be our missing number (not present in the array).

Summing a lot of numbers, particularly for a large value of **N** is vulnerable to overflows. We can mitigate this by summing the difference as we step through the array, or resolve it entirely by using an XOR. Because each integer is also presently exactly once in the range 1 ... **N**, they will be 'cancelled' out, leaving on the missing integer.
