def stringTokenizer(s):
    result = []
    temp = []
    num = ""
    for c in s:
        if c == "{":
            continue
        elif c == ",":
            if num == "":
                continue
            else:
                temp.append(int(num))
                num = ""
        elif c == "}":
            if num != "":
                temp.append(int(num))
                num = ""
            if len(temp) == 0:
                continue
            result.append(temp)
            temp = []
        else:
            num += c
    return result


def solution(s):
    answer = []
    tokenized_list = stringTokenizer(s)
    print(tokenized_list)
    for i in range(len(tokenized_list)):
        for j in tokenized_list:
            if len(j) == i + 1:
                for a in answer:
                    j.remove(a)
                answer.append(j[0])
    return answer


# -------------------------------------
s = "{{111}}"

print(solution(s))