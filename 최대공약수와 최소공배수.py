def gcd(a, b):
    small, large = min([a, b]), max([a, b])
    answer = small

    for _ in range(small):
        if (large % answer) == 0 and (small % answer) == 0:
            break
        answer -= 1

    return answer


def lcm(a, b):
    small, large = min([a, b]), max([a, b])
    answer = large

    while True:
        if (answer % large) == 0 and (answer % small) == 0:
            break
        answer += 1

    return answer


A, B = list(map(int, input().split()))
print(gcd(A, B))
print(lcm(A, B))
