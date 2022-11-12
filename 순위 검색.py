from itertools import combinations
from bisect import bisect_left, bisect_right


def appendInfo(informations, key, score):
    if key not in informations:
        informations[key] = []
    informations[key].append(score)


def buildInfo(informations, information):  # info에 들어있는 문자열 그대로 인자로 받음
    feature = list(information.split())
    # [0]: language, [1]: group, [2]: career, [3]: soul_food, [4]: score

    appendInfo(informations, feature[0] + " " + feature[1] + " " + feature[2] + " " + feature[3], int(feature[4]))

    for i in range(len(feature) - 1):
        feature = list(information.split())
        feature[i] = "-"
        appendInfo(informations, feature[0] + " " + feature[1] + " " + feature[2] + " " + feature[3], int(feature[4]))

    num = [0, 1, 2, 3]
    for combination in list(map(list, combinations(num, 2))):
        feature = feature = list(information.split())
        for i in range(len(feature)):
            if i in combination:
                feature[i] = "-"
        appendInfo(informations, feature[0] + " " + feature[1] + " " + feature[2] + " " + feature[3], int(feature[4]))

    for combination in list(map(list, combinations(num, 3))):
        feature = feature = list(information.split())
        for i in range(len(feature)):
            if i in combination:
                feature[i] = "-"
        appendInfo(informations, feature[0] + " " + feature[1] + " " + feature[2] + " " + feature[3], int(feature[4]))

    appendInfo(informations, "- - - -", int(feature[4]))


def solution(info, queries):
    answer = []
    informations = {}
    for information in info:
        buildInfo(informations, information)

    for key in informations.keys():
        informations[key] = sorted(informations[key])

    for query in queries:
        feature = [q for q in list(query.split()) if q != "and"]
        key = feature[0] + " " + feature[1] + " " + feature[2] + " " + feature[3]
        score = int(feature[4])
        if key not in informations:
            answer.append(0)
            continue
        answer.append(len(informations[key]) - bisect_left(informations[key], score))

    return answer