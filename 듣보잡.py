import sys
input = sys.stdin.readline
print = sys.stdout.write


D, B = list(map(int, input().split()))
D_LIST = []
for _ in range(D):
    D_LIST.append(input().split("\n")[0])

DB_LIST = []
cnt = 0
for _ in range(B):
    name = input().split("\n")[0]
    if name in D_LIST:
        DB_LIST.append(name)
        cnt += 1

print(str(cnt))
temp = sorted(DB_LIST)
for i in range(cnt):
    print(temp[i])
