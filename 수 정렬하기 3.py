import sys
input = sys.stdin.readline

N = int(input())
numbers = [0] * 10001
for _ in range(N):
    numbers[int(input())] += 1

for i in range(1, 10001):
    for _ in range(numbers[i]):
        print(i)
