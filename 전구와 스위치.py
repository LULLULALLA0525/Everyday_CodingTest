def determine(bulbs, changed, idx):
	if idx == 0:    # 시작 전구
		if bulbs[idx] == 0:
			next_changed = changed[idx]
		else:   # bulbs[idx] == 1
			next_changed = not changed[idx]
	else:
		if bulbs[idx] == 0:
			next_changed = changed[idx - 1] != changed[idx]
		else:   # bulbs[idx] == 1
			next_changed = changed[idx - 1] == changed[idx]
	return next_changed


def solution(n, start, end):
	bulbs = []
	for i in range(n):
		if start[i] == end[i]:
			bulbs.append(0)
		else:
			bulbs.append(1)

	answer = []
	cases = [False, True]
	for case in cases:
		changed = [case]
		for idx in range(n - 1):
			changed.append(determine(bulbs, changed, idx))
		completed = False
		if bulbs[-1] == 0:
			completed = changed[-2] == changed[-1]
		else:  # bulbs[n - 1] == 1
			completed = changed[-2] != changed[-1]
		if completed:
			count = 0
			for i in range(n):
				if changed[i]:
					count += 1
			answer.append(count)

	if len(answer) == 0:
		return -1
	else:
		return min(answer)


N = int(input())
START = list(map(int, input()))
END = list(map(int, input()))
print(solution(N, START, END))
