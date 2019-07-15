def get_score(name):
    name = name.replace(" ", "")
    repeated = []

    for char in name:
        if char not in repeated:
            repeated.append(char)

    return len(repeated)


if __name__ == "__main__":

    T = int(input())

    for case in range(1, T + 1):
        leader_name = ""
        leader_score = 0
        citizens = int(input())

        for _ in range(citizens):
            next_name = input()
            next_score = get_score(next_name)

            if next_score > leader_score:
                leader_name, leader_score = next_name, next_score
            elif next_score == leader_score:
                if next_name < leader_name:
                    leader_name, leader_score = next_name, next_score

        print("Case #{}: {}".format(case, leader_name))
