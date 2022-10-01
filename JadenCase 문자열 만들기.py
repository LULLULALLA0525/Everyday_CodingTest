def solution(s):
    str = list(s)

    words = []
    temp = []
    for i in range(len(str)):
        if str[i] == '"':
            continue
        elif str[i] == ' ':
            if temp:
                words.append(''.join(temp))
                temp = []
            words.append(" ")
        else:
            temp.append(str[i])
    if temp:
        words.append(''.join(temp))
        temp = []

    for i in range(len(words)):
        words[i] = words[i].lower()
        words[i] = words[i].capitalize()

    answer = ''.join(words)
    return answer

s = input()
print(solution(s))