# 야근 피로도 = (남은 작업량)^2
# N시간 동안 야근 피로도가 최소여야 한다.
# 1시간 동안 1만큼 작업할 수 있다.
# work는 정수 리스트로, 각 일에 대한 작업량을 의미한다.
# 퇴근까지 남은 시간은 n으로서 전달된다.
# 각 work들 중 남은 시간을 적절히 분배하여 작업하면 된다.
# 그렇게 야근 피로도가 최소가 되도록 작업했을 때의 야근 피로도를 반환한다.
INF = 100000


def solution(n, works):
    works_length = len(works)
    remain_work = [INF] * works_length
    total_work = sum(works) - n
    if total_work <= 0:
        return 0

    temp = True
    while temp:
        temp = False

        remainder = total_work % works_length
        divider = total_work // works_length

        for i in range(len(works)):
            if works[i] <= divider and remain_work[i] == INF:
                total_work -= works[i]
                remain_work[i] = works[i]
                works_length -= 1
                temp = True

    for i in range(len(remain_work)):
        if remain_work[i] == INF:
            remain_work[i] = divider
            if remainder > 0:
                remain_work[i] += 1
                remainder -= 1

    answer = 0
    for w in remain_work:
        answer += (w * w)

    return answer


n = int(input())
# 4
# 1
# 3
works = list(map(int, input().split()))
# 4 3 3
# 2 1 2
# 1 1

print(solution(n, works))
# 12
# 6
# 0
