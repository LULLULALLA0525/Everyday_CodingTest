def solution(gems):
    gem_dict = {}
    for gem_idx in range(len(gems)):
        if gems[gem_idx] in gem_dict.keys():
            gem_dict[gems[gem_idx]].append(gem_idx + 1)
        else:
            gem_dict[gems[gem_idx]] = []
            gem_dict[gems[gem_idx]].append(gem_idx + 1)
    print(gem_dict)

    first_gem_index = []
    for gem in gem_dict.keys():
        first_gem_index.append(gem_dict[gem][0])
    min_index = max(first_gem_index)

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

# 1 2 3 4 5 6 7 8
# 1 2 3 1 2 2 3 1
# 1 -> 1, 4, 8
# 2 -> 2, 5, 6
# 3 -> 3, 7
print("태우야 사랑해")
