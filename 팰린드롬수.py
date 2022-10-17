def solution(num):
	half = len(num) // 2
	l_point, r_point = 0, len(num) - 1
	for i in range(half):
		if num[i] != num[len(num) - 1 - i]:
			return 'no'
	return 'yes'

while True:
	num = list(input())
	if num == ['0']:
		break
	print(solution(num))