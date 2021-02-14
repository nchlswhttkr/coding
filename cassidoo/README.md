# rendezvouz with cassidoo

Interview problems from the [rendezvouz with cassidoo newsletter](https://cassidoo.co/newsletter/).

### 2021-02-08

> **Implement a `ProductList` class that has two methods, add(`n`) (which pushes the value `n` to the back of the list) and product(`m`) (which returns the product of the last `m` numbers in the list).**

I think this is straightforward in Python, since you can easily push onto a list/stack and read the last `n` items.

A problem like this is a good opportunity to focus on recognising edge cases and catching them in test cases. In the `product(n)` method, it's not specified what should happen if `n` isn't a positive number. What if it's zero or negative? Try to document this with a test case.

### 2021-01-25

> **Given an n x n array, rotate it 90 degrees without making a new array.**

Let's start from smallest square we can and move up.

For a 1x1 square, we can rotate it but nothing changes because it's only one unit long and one unit wide.

For a 2x2 square, each corner swaps with the next corner. The top left corner becomes the top right corner, the top right corner becomes the bottom right corner, and so on.

For a 3x3, think of it as two squares. It's a 1x1 square inside an (empty) 3x3 square. We already know how to rotate a 1x1 square, so focus on the outer layer. The top side needs to become the right side, the right side needs to become the bottom side, and so on.

Rotating the array involves _rotating each layer_ separately. Rotating layers is just like rotating a 2x2 square, but now we need to swap every cell along each sider rather than just corners.

Go down through each layer of the square and rotate each side, make sure you don't rotate corners twice!

If you're looking for an extension, think about what you might do if you need to rotate it 180/270 degrees. I would just repeat the cell-swapping logic two/three times respectively.

```sh
python3 -m unittest 2021-01-25.py

echo "1 2 3
4 5 6
7 8 9" | python3 2021-01-25.py
# 7 4 1
# 8 5 2
# 9 6 3
```
