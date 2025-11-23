# https://adventofcode.com/2022/day/9
head: list[int] = [0, 0]
tail: list[int] = [0, 0]
tail_visited: list[list[int]] = [[0, 0]]

def move_head(direction: str) -> None:
    match direction:
        case "U":
            head[1] += 1
        case "D":
            head[1] -= 1
        case "L":
            head[0] -= 1
        case "R":
            head[0] += 1

def tail_adj() -> bool:
    if (head == tail) or (abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1):
        return True

    return False

def move_tail() -> None:
    # Move up
    if head[1] > tail[1]:
        tail[1] += 1
    # Move down
    if head[1] < tail[1]:
        tail[1] -= 1
    # Move right
    if head[0] > tail[0]:
        tail[0] += 1
    # Move left
    if head[0] < tail[0]:
        tail[0] -= 1

with open("./input.txt") as file:
    for line in file:
        direction, steps = line.split()

        for _ in range(int(steps)):
            move_head(direction)

            # Move tail
            if tail_adj():
                continue
            move_tail()

            if tail not in tail_visited:
                tail_visited.append(tail.copy())

print("Part 1 answer: ", len(tail_visited))
