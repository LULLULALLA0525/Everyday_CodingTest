def solution(gems):
	gem_list = {}
	for gem_idx in range(len(gems)):
		if gems[gem_idx] in gem_list.keys():
			gem_list[gems[gem_idx]].append(gem_idx)
		else:
			gem_list[gems[gem_idx]] = []
			gem_list[gems[gem_idx]].append(gem_idx)
	print(gem_list)

	start_idx, end_idx = 0, 0
	answer = [start_idx, end_idx]
	return answer

gems = list(input().split())
#DIA RUBY RUBY DIA DIA EMERALD SAPPHIRE DIA
#AA AB AC AA AC
#XYZ XYZ XYZ
#ZZZ YYY NNNN YYY BBB

print(solution(gems))
#[3, 7]
#[1, 3]
#[1, 1]
#[1, 5]

#0 1 2 3 4 5 6 7
#1 2 3 1 2 2 3 1
#1 -> 0, 3, 7
#2 -> 1, 4, 5
#3 -> 2, 6
print("태우야 사랑해")