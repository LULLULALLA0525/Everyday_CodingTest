from itertools import combinations
from itertools import product
from bisect import bisect_left
from bisect import bisect_right

def solution(dice):
    answer = [
        [],     # dice 조합
        []      # 승률
    ]
    cases = list(combinations(range(1, len(dice) + 1), len(dice)//2))

    for case in cases:
        me = case
        you = tuple(die for die in range(1, len(dice) + 1) if die not in case)
        if me in answer[0] or you in answer[0]:
            continue
        
        list_me = [dice[picked - 1] for picked in me]
        list_you = [dice[picked - 1] for picked in you]

        result_me = sorted(list(map(lambda x: sum(x), list(product(*list_me)))))
        result_you = sorted(list(map(lambda x: sum(x), list(product(*list_you)))))
        
        total_win = 0
        total_lose = 0
        for score in result_me:
            total_win += bisect_left(result_you, score)
            total_lose += len(result_you) - bisect_right(result_you, score)

        if total_win >= total_lose:
            answer[0].append(me)
            answer[1].append(total_win / (len(result_me) * len(result_you)))
        else:
            answer[0].append(you)
            answer[1].append(total_lose / (len(result_me) * len(result_you)))

    max_win_rate = 0
    max_case = []
    for i in range(len(answer[0])):
        if answer[1][i] > max_win_rate:
            max_case = answer[0][i]
            max_win_rate = answer[1][i]

    return max_case