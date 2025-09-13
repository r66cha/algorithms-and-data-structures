l = [
    ["*", 0],
    [0, "*"],
    [0, 0],
]
directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    # --
    (0, -1),
    (0, 1),
    # --
    (1, -1),
    (1, 0),
    (1, 1),
]


counter = 0

for r in range(len(l)):
    for c in range(len(l[0])):
        if l[r][c] == "*":
            continue
        counter = 0
        for dr, dc in directions:
            ...
