def solution(gems):
    gem_dict = {}


    start_idx, end_idx = 0, 0
    answer = [start_idx, end_idx]
    return answer


gems_temp = list(input().split())
# DIA RUBY RUBY DIA DIA EMERALD SAPPHIRE DIA
# AA AB AC AA AC
# XYZ XYZ XYZ
# ZZZ YYY NNN YYY BBB

print(solution(gems_temp))
# [3, 7]
# [1, 3]
# [1, 1]
# [1, 5]
