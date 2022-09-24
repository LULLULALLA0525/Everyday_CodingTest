# 문제 설명
# 어피치와 라이언이 양궁 대회를 하고 있다.
# 과녁은 0~10점이 있으며, 최종 점수가 높은 선수가 승리한다. 단, 최종 점수가 같을 경우 어피치가 승리한다.
# 과녁 칸에 맞은 화살의 개수가 더 많은 사람이 해당 칸의 점수만을 가져간다. 단, 같은 경우 어피치가 가져간다.
# 어피치가 먼저 쏜 상태이며, n은 화살의 개수, info는 어피치가 맞춘 과녁에 대한 정보다.
# info는 0번째 원소부터 각각 10점, 9점, 8점, ..., 0점 과녁에 맞은 화살의 개수다.
# 라이언이 어피치와 가장 큰 점수 차이로 이기기 위해 라이언이 맞춰야 하는 과녁에 대한 정보를 반환해야 한다.
# 만약 경우의 수가 여러가지일 경우, 가장 적은 과녁을 많이 맞춘 과녁 정보를 반환한다.
# 라이언이 이길 수 없을 경우, [-1]을 반환한다.

# 0/1 Knapsack Problem -> Dynamic Programming 활용 가능?!
def compare(a_info, r_info):
    a_score, r_score = 0, 0
    for i in range(11):
        if a_info[i] == 0 and r_info[i] == 0:
            continue
        if a_info[i] >= r_info[i]:
            a_score += 10 - i
        else:
            r_score += 10 - i
    return r_score - a_score


def solution(n, info):
    ryan = [[0] * 11] * (n + 1)
    for arrow in range(1, n + 1):
        optimized = -1000
        for shoot in range(1, arrow + 1):
            prev_info = list(ryan[arrow - shoot])
            expect = 0
            index = -1
            for i in range(len(info)):
                if info[i] == shoot - 1 and prev_info[i] == 0:
                    if info[i] == 0:
                        temp = 10 - i
                    else:
                        temp = 2 * (10 - i)

                    if temp > expect:
                        expect = temp
                        index = i
            prev_info[index] += shoot
            score = compare(info, prev_info)
            if score > optimized:
                optimized = score
                ryan[arrow] = list(prev_info)
    if compare(info, ryan[n]) <= 0:
        return [-1]
    else:
        return ryan[n]


n = int(input())
info = list(map(int, input().split(",")))

print(solution(n, info))
'''
n	info					result
	10 9 8 7 6 5 4 3 2 1 0
5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
1	[1,0,0,0,0,0,0,0,0,0,0]	[-1]
9	[0,0,1,2,0,1,1,1,1,1,1]	[1,1,2,0,1,2,2,0,0,0,0]
10	[0,0,0,0,0,0,0,0,3,4,3]	[1,1,1,1,1,1,1,1,0,0,2]
10  [0,1,1,1,1,1,1,1,1,1,1] [0,0,0,0,0,0,0,0,0,0,0]
'''