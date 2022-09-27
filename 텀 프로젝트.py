# 프로젝트 팀원 수에는 제한이 없다. -> 모든 학생이 한 팀이 될 수도 있다.
# 모든 학생들은 프로젝트를 함께하고 싶은 학생을 한 명만 선택해야 한다.
# 혼자 하고 싶은 학생은 본인을 선택할 수도 있다.
# 각 학생들이 서로 다른 학생을 골라 최종적으로 시작 학생이 지목되어야만 팀이 성립된다.
# 어느 프로젝트 팀에도 속하지 않는 학생의 수를 계산하는 프로그램을 작성해야 한다.
import sys

MATCHED = 1
NOT_MATCHED = -1
UNKNOWN = 0


def solution(n, pick):
    team = [UNKNOWN] * n

    for i in range(n):
        if pick[i] == i + 1:
            team[i] = MATCHED

    for i in range(n):
        if team[i] != UNKNOWN:
            continue

        # print("checking", i, ",,,")
        waiting = []
        current_idx = i
        while True:
            # print("    checking", current_idx, ",,,")
            waiting.append(current_idx)
            team[current_idx] = NOT_MATCHED
            next_idx = pick[current_idx] - 1

            if next_idx in waiting:
                # print(waiting)
                temp = waiting.index(next_idx)
                for w in range(temp, len(waiting)):
                    team[waiting[w]] = MATCHED
                break
            elif team[next_idx] != UNKNOWN:
                break
            else:
                current_idx = next_idx
    # print(team)
    answer = sum(1 for i in team if i == NOT_MATCHED)
    return answer


inp = lambda: sys.stdin.readline()

test_cases = int(inp())
for _ in range(test_cases):
    n = int(inp())
    pick = list(map(int, inp().split()))
    print(solution(n, pick))

# 2
# 7
# 3 1 3 7 3 4 6         -> 3
# 8
# 1 2 3 4 5 6 7 8       -> 0
