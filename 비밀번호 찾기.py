N, Q = list(map(int, input().split()))
ID = {}
for _ in range(N):
    link, my_id = list(input().split())
    ID[link] = my_id
for _ in range(Q):
    print(ID[list(input().split())[0]])
