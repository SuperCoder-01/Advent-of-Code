# https://adventofcode.com/2022/day/9
knots: list[list[int]] = [[0, 0] for _ in range(10)] # Index 0 = head; Index 9 = tail
tail_visited: list[list[int]] = [[0, 0]]

def move_head(direction: str) -> None:
    match direction:
        case "U":
            knots[0][1] += 1
        case "D":
            knots[0][1] -= 1
        case "L":
            knots[0][0] -= 1
        case "R":
            knots[0][0] += 1

def knot_adj(knot1: list[int], knot2: list[int]) -> bool:
    if (knot1 == knot2) or (abs(knot1[0] - knot2[0]) <= 1 and abs(knot1[1] - knot2[1]) <= 1):
        return True

    return False

with open("./input.txt") as file:
    for line in file:
        direction, steps = line.split()

        for _ in range(int(steps)):
            move_head(direction)

            # Check and move knots
            for knot_index in range(1, 10):
                if knot_adj(knots[knot_index], knots[knot_index - 1]):
                    continue

                # Move up
                if knots[knot_index - 1][1] > knots[knot_index][1]:
                    knots[knot_index][1] += 1
                # Move down
                if knots[knot_index - 1][1] < knots[knot_index][1]:
                    knots[knot_index][1] -= 1
                # Move right
                if knots[knot_index - 1][0] > knots[knot_index][0]:
                    knots[knot_index][0] += 1
                # Move left
                if knots[knot_index - 1][0] < knots[knot_index][0]:
                    knots[knot_index][0] -= 1

            if knots[9] not in tail_visited:
                tail_visited.append(knots[9].copy())

print("Part 2 answer: ", len(tail_visited))
