from itertools import combinations


def solution(n, m, cards):
    answer = 0
    idxes = list(combinations(range(len(cards)), 3))
    for idx in idxes:
        result = cards[idx[0]] + cards[idx[1]] + cards[idx[2]]
        if result > m:
            continue
        elif result > answer:
            answer = result
        else:
            continue

    return answer


n, m = list(map(int, input().split()))
cards = list(map(int, input().split()))
print(solution(n, m, cards))
