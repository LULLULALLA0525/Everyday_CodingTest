def solution(n):
    devil_num = []

    for i in range(10000):
        s = '000' + str(i)
        for j in range(len(s) + 1):
            devil_num.append(int(s[:j] + '666' + s[j:]))
    temp = set(devil_num)
    devil_num = list(temp)
    devil_num = sorted(devil_num)

    return devil_num[n - 1]


n = int(input())
print(solution(n))
