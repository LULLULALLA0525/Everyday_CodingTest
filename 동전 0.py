def solution(money, m):
    cnt = 0
    for i in range(len(money)):
        bill = money[i]
        cnt += (m//bill)
        m %= bill
    return cnt


N, M = list(map(int, input().split()))
MONEY = []
for _ in range(N):
    MONEY.insert(0, int(input()))
print(solution(MONEY, M))
