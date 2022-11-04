def solution(K, N):
    hotel = []
    for _ in range(15):
        hotel.append([0] * 15)

    for i in range(15):
        hotel[0][i] = i + 1

    for floor in range(1, 15):
        for room in range(15):
            hotel[floor][room] = sum(hotel[floor - 1][:room + 1])

    return hotel[K][N - 1]


T = int(input())
for _ in range(T):
    K = int(input())
    N = int(input())
    print(solution(K, N))
