def solution(n):
    bee = [0]
    num = 1
    i = 0
    while True:
        num += 6*i
        bee.append(num)
        if num > n:
            break
    return n


n = int(input())
print(solution(n))
