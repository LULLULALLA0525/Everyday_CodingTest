def solution(people, limit):
	answer = 0
	too_heavy = []

	while people:
		remain = limit
		is_boat_full = False

		while not is_boat_full:
			if people:
				person = people.pop()
			else:
				is_boat_full = True
				break
			while remain < person:
				too_heavy.append(person)
				if people:
					person = people.pop()
				else:
					is_boat_full = True
					break
		
			while too_heavy:
				people.append(too_heavy.pop())
		
			if not is_boat_full:
				remain -= person

			if remain == 0:
				is_boat_full = True

		answer += 1

	return answer

people = [70, 80, 50, 50]
limit = 100

print(solution(people, limit))