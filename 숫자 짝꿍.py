import sys

input = lambda: sys.stdin.readline()


def solution(x, y):
    x_split = list(x)
    y_split = list(y)

    x_count = [0] * 10
    y_count = [0] * 10

    for i in range(len(x_split)):
        x_count[int(x_split[i])] += 1
    for i in range(len(y_split)):
        y_count[int(y_split[i])] += 1

    duplicated = [0] * 10
    for i in range(10):
        duplicated[i] = min(x_count[i], y_count[i])

    if duplicated == [0] * 10:
        return "-1"

    answer = ''
    for i in range(10):
        temp = [str(i)] * duplicated[i]
        temp.append(answer)
        answer = ''.join(temp)
    if int(answer) == 0:
        return "0"
    return answer


X, Y = list(input().split())
print(solution(X, Y))
