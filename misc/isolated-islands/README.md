# Isolated Islands

\>p

## Problem

Given a tropical island map as a grid of 0s and 1s, where 0 represents a region of water and 1 represents a region of land, count the number of islands.

An island is considered to be a collection of land regions where it is possible to travel from any region to any other region of the same island through horizontal and vertical navigation (diagonal movement is not allowed).

```
# INPUT
0 1 0 1 0 0
0 1 0 0 1 0
1 1 1 0 1 0
0 0 0 0 0 1
0 0 1 1 0 0

# OUTPUT
5
```

The vaguely diagonal collection of land regions in the top right is considered a clump of separate islands, because they are connected only through diagonal traversal.

## Solution

Iterate through all regions on the map, and flood whenever a new island is found. Flooding means you should traverse (using your algorithm of choice) to all adjacent land regions from your starting region, and disqualify them.

This means that each time you find a land region, you have found the start of a new island.
