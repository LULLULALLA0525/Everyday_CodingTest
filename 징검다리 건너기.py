import random

def check_stones(stones, k, i, next_stones, max_stone, answer):
    max_out = False
    max_in = False
    if i < (k - 1):
        next_stones.append(stones[i])
    elif i == k - 1:
        next_stones.append(stones[i])
        max_stone = max(next_stones)
        answer = max_stone
    else:
        if stones[i] > max_stone:           # 들어오는 돌이 이전 리스트에 있는 최대 돌보다 크면 들어오는 돌을 최대로 설정
            max_in = True
            max_stone = stones[i]
        if next_stones[0] == max_stone:     # 나가는 돌이 이전 리스트에 있는 최대 돌과 같다면 최대 돌을 재설정
            max_out = True

        del next_stones[0]
        next_stones.append(stones[i])

        if max_out and not max_in:          # 최대 돌이 나가도 더 큰 돌이 들어왔으면 재설정할 필요 없음
            max_stone = max(next_stones)
            if answer > max_stone:
                answer = max_stone
    return max_stone, answer

def solution(stones, k):
    answer = 0

    next_stones = []
    max_stone = 0

    if k == 1:
        answer = min(stones)
    else:
        for i in range(len(stones)):
            max_stone, answer = check_stones(stones, k, i, next_stones, max_stone, answer)

    return answer

#-----------------------


stones = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

k = 3

print(stones)
print(k)

print(solution(stones, k))