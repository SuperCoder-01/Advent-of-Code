# https://adventofcode.com/2022/day/8
from functools import reduce

tree_map: list[list[int]] = [[int(tree) for tree in line if tree != '\n'] for line in open("./2022/input.txt")]
scenic_scores: list[int] = []
TREE_MAP_LEN: int = len(tree_map)
INVI_TREE_MAP_LEN: int = len(tree_map[0])
trees_visible: int = 0

def get_visibility(row: int, col: int) -> dict[str, bool]:
    visibility: dict[str, bool] = {"top": True, "bottom": True, "left": True, "right": True}
    tree: int = tree_map[row][col] # Get tree

    # Check top
    for i in range(row - 1, -1, -1):
        if tree_map[i][col] >= tree:
            visibility["top"] = False
            break
    # Check bottom
    for i in range(row + 1, TREE_MAP_LEN):
        if tree_map[i][col] >= tree:
            visibility["bottom"] = False
            break
    # Check left
    for i in range(col - 1, -1, -1):
        if tree_map[row][i] >= tree:
            visibility["left"] = False
            break
    # Check right
    for i in range(col + 1, INVI_TREE_MAP_LEN):
        if tree_map[row][i] >= tree:
            visibility["right"] = False
            break

    return visibility

def get_scenic_score(row: int, col: int) -> int:
    count: int = 0
    tree: int = tree_map[row][col] # Get tree

    # Check top
    for i in range(row - 1, -1, -1):
        count += 1
        if tree_map[i][col] >= tree:
            break
    scores: list[int] = [count]
    count = 0
    # Check bottom
    for i in range(row + 1, TREE_MAP_LEN):
        count += 1
        if tree_map[i][col] >= tree:
            break
    scores.append(count)
    count = 0
    # Check left
    for i in range(col - 1, -1, -1):
        count += 1
        if tree_map[row][i] >= tree:
            break
    scores.append(count)
    count = 0
    # Check right
    for i in range(col + 1, INVI_TREE_MAP_LEN):
        count += 1
        if tree_map[row][i] >= tree:
            break
    scores.append(count)

    return reduce(lambda a, b: a * b, scores)

# PART 1
for x, _ in enumerate(tree_map):
    if x in [0, TREE_MAP_LEN - 1]:
        continue
    for y, _ in enumerate(tree_map[x]):
        if y in [0, INVI_TREE_MAP_LEN - 1]:
            continue
        if any(get_visibility(x, y).values()):
            trees_visible += 1
# Trees on the edges: 99 * 4 - 4 = 392
print("Part 1: ", trees_visible + 392)

# PART 2
for x, _ in enumerate(tree_map):
    for y, _ in enumerate(tree_map[x]):
        scenic_scores.append(get_scenic_score(x, y))
        # print(get_scenic_score(x, y))

print("Part 2: ", max(scenic_scores))