words = list(input().upper())
d = {}

for i in range(len(words)):
	if words[i] in d.keys():
		d[words[i]] += 1
	else:
		d[words[i]] = 1

answer = list(sorted(d.keys(), key=lambda x: d[x], reverse=True))

if len(answer) == 1:
	print(answer[0])
elif d[answer[0]] == d[answer[1]]:
	print("?")
else:
	print(answer[0])