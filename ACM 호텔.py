def solution(h, w, n):
    room = n // h + 1
    floor = n % h
    if floor == 0:
        floor = h
        room -= 1
    return floor*100 + room


T = int(input())
test = []
for _ in range(T):
    H, W, N = list(map(int, input().split()))
    test.append([H, W, N])
for t in test:
    print(solution(t[0], t[1], t[2]))
