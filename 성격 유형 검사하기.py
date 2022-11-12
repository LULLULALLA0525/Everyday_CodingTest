def solution(survey, choices):
    score = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    length = len(choices)
    for i in range(length):
        if choices[i] == 1:
            score[survey[i][0]] += 3
        elif choices[i] == 2:
            score[survey[i][0]] += 2
        elif choices[i] == 3:
            score[survey[i][0]] += 1
        elif choices[i] == 4:
            continue
        elif choices[i] == 5:
            score[survey[i][1]] += 1
        elif choices[i] == 6:
            score[survey[i][1]] += 2
        elif choices[i] == 7:
            score[survey[i][1]] += 3

    answer = ''
    if score["R"] >= score["T"]:
        answer = ''.join([answer, "R"])
    else:
        answer = ''.join([answer, "T"])

    if score["C"] >= score["F"]:
        answer = ''.join([answer, "C"])
    else:
        answer = ''.join([answer, "F"])

    if score["J"] >= score["M"]:
        answer = ''.join([answer, "J"])
    else:
        answer = ''.join([answer, "M"])

    if score["A"] >= score["N"]:
        answer = ''.join([answer, "A"])
    else:
        answer = ''.join([answer, "N"])

    return answer


SURVEY = list(input().split())
# AN CF MJ RT NA
# TR RT TR
CHOICES = list(map(int, input().split()))
# 5 3 2 7 5
# 7 1 3
print(solution(SURVEY, CHOICES))
# TCMA
# RCJA
