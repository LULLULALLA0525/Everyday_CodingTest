def solution(cards):
    cycles = []
    num_of_cards = len(cards)
    cards.insert(0, 0)
    opened = [False] * (num_of_cards + 1)

    for i in range(len(cards)):
        if opened[i]:
            continue
        cycle = []
        cur = i
        while not opened[cur]:
            opened[cur] = True
            cycle.append(cur)
            cur = cards[cur]
        cycles.append(cycle.copy())

    if len(cycles) == 2:
        return 0
    else:
        cycles = sorted(cycles, key=lambda x: len(x), reverse=True)
        return len(cycles[0]) * len(cycles[1])


# 8 6 3 7 2 5 1 4
CARDS = list(map(int, input().split()))
print(solution(CARDS))
# 12
