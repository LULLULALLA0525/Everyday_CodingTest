from collections import deque

def rescue_heavy(people_queue, remain):
	heaviest = people_queue.pop()
	if remain >= heaviest:
		return heaviest
	else:
		people_queue.append(heaviest)
		return 0

def rescue_light(people_queue, remain):
	lightest = people_queue.popleft()
	if remain >= lightest:
		return lightest
	else:
		people_queue.appendleft(lightest)
		return 0
	

def solution(people, limit):
	answer = 0
	people_queue = deque(people)

	while people_queue:
		remain = limit
		while True:
			if people_queue:
				rescued = rescue_heavy(people_queue, remain)
				remain -= rescued
			else:
				if remain != limit:
					answer += 1
				break

			if people_queue:
				rescued = rescue_light(people_queue, remain)
				if rescued == 0:
					answer += 1
					break
				else:
					remain -= rescued
			else:
				if remain != limit:
					answer += 1
				break
	
	return answer

people = [70, 80, 50, 50]
limit = 100

print(solution(people, limit))