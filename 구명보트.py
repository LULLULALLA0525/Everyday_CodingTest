def solution(people, limit):
    answer = 0
    rescued = [False for _ in range(len(people))]

    remain = limit
    for i in range(len(people) - 1, -1, -1):
        if rescued[i]:
            continue


    return answer