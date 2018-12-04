import sys


def main():
    boxes = sys.stdin.readlines()
    closest_match = ''  # closest match produces the longest string
    for i in range(len(boxes) - 1):
        for j in range(i + 1, len(boxes)):
            match = ''
            for k in range(len(boxes[i])):
                if boxes[i][k] == boxes[j][k]:
                    match += boxes[i][k]
            if len(match) > len(closest_match):
                closest_match = match
    print(closest_match, end="", flush=True)


if __name__ == "__main__":
    main()
