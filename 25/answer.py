with open('input.txt.txt') as puzzle_file:
    puzzle_input = [tuple(int(s.strip()) for s in line.split(',')) for line in puzzle_file]

groups = {}
for p1 in puzzle_input:
    for p2 in puzzle_input:
        if sum(abs(a - b) for a, b in zip(p1, p2)) > 3:
            continue
        s1 = groups.get(p1)
        if s1 is None:
            s1 = set((p1, ))
            groups[p1] = s1
        s2 = groups.get(p2)
        if s2 is None:
            s2 = set((p2, ))
            groups[p2] = s2
        if s1 is not s2:
            s1.update(s2)
            for p in s2:
                groups[p] = s1
print(len(set(map(frozenset, groups.values()))))
