def init_queens(queens, i):     # i번째 이후의 queen을 모두 초기화
    for q in range(i, len(queens)):
        queens[q] = -1

def solution(n):
    queens = [-1] * n           # 각 row별 queen의 좌표
    board = [[True] * n] * n    # 2차원 보드(True면 배치 가능, False면 배치 불가능

    answer = 0
    return answer

n = int(input())
