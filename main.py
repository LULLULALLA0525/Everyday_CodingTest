import sys

input = lambda: sys.stdin.readline()

DEFAULT = 0
ENEMY = 1
FRIEND = 2


INFO = [[]]


def set_enemy(n, a, b):
	if INFO[a][b] == DEFAULT:
		INFO[a][b] = ENEMY
		for person in range(1, n + 1):
			if person == b:
				continue
			if INFO[a][person] == FRIEND:
				res = set_enemy(n, person, b)
				if not res:
					return False
			elif INFO[a][person] == ENEMY:
				res = set_friend(n, person, b)
				if not res:
					return False
	elif INFO[a][b] == ENEMY:
		INFO[a][b] = ENEMY
	elif INFO[a][b] == FRIEND:
		return False

	if INFO[b][a] == DEFAULT:
		INFO[b][a] = ENEMY
		for person in range(1, n + 1):
			if person == a:
				continue
			if INFO[b][person] == FRIEND:
				res = set_enemy(n, person, a)
				if not res:
					return False
			elif INFO[b][person] == ENEMY:
				res = set_friend(n, person, a)
				if not res:
					return False
	elif INFO[b][a] == ENEMY:
		INFO[b][a] = ENEMY
	elif INFO[b][a] == FRIEND:
		return False
		
	return True


def set_friend(n, a, b):
	if INFO[a][b] == DEFAULT:
		INFO[a][b] = FRIEND
		for person in range(1, n + 1):
			if person == b:
				continue
			if INFO[a][person] == FRIEND:
				res = set_friend(n, person, b)
				if not res:
					return False
			elif INFO[a][person] == ENEMY:
				res = set_enemy(n, person, b)
				if not res:
					return False
	elif INFO[a][b] == FRIEND:
		INFO[a][b] = FRIEND
	elif INFO[a][b] == ENEMY:
		return False

	if INFO[b][a] == DEFAULT:
		INFO[b][a] = FRIEND
		for person in range(1, n + 1):
			if person == a:
				continue
			if INFO[b][person] == FRIEND:
				res = set_friend(n, person, a)
				if not res:
					return False
			elif INFO[b][person] == ENEMY:
				res = set_enemy(n, person, a)
				if not res:
					return False
	elif INFO[b][a] == FRIEND:
		INFO[b][a] = FRIEND
	elif INFO[b][a] == ENEMY:
		return False

	return True
		

def solution(n, rivals):
	for _ in range(n):
		INFO.append([DEFAULT] * (n + 1))
	result = True
	for rival in rivals:
		result = set_enemy(n, rival[0], rival[1])
		if not result:
			break
	if result:
		return 1
	else:
		return 0

N, M = list(map(int, input().split()))
RIVALS = []
for _ in range(M):
	RIVALS.append(list(map(int, input().split())))
print(solution(N, RIVALS))
