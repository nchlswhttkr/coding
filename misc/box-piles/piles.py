def calculate_moves(boxes):
    shortest, tallest = min(boxes), max(boxes)
    heights = [0] * (tallest + 1)

    for box in boxes:
        heights[box] += 1

    moves, current_layer = 0, 0
    for i in range(tallest, shortest, -1):
        if heights[i] != 0:
            current_layer += heights[i]
            moves += current_layer

    return moves


print(calculate_moves([int(input()) for _ in range(int(input()))]))
