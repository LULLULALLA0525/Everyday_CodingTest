n = int(input())
words = []
for _ in range(n):
    words.append(input())

temp1 = set(words)
temp2 = list(temp1)

result = sorted(temp2, key=lambda x: (len(x), x))

for i in range(len(result)):
    print(result[i])