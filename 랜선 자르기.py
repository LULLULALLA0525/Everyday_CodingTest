def binary_search(sorted_lines, left, right, n):
    if left + 1 >= right:
        return left
    line_length = (right + left) // 2
    separated = 0
    for line in sorted_lines:
        separated += (line // line_length)
    if separated >= n:
        return binary_search(sorted_lines, line_length, right, n)
    else:
        return binary_search(sorted_lines, left, line_length, n)


def solution(lines, n):
    sorted_lines = sorted(lines)
    line_length = binary_search(sorted_lines, 1, sorted_lines[-1], n)
    separated = 0
    for line in sorted_lines:
        separated += (line // line_length)

    temp = separated
    while temp == separated:
        line_length += 1
        temp = 0
        for line in sorted_lines:
            temp += (line // line_length)

    return line_length - 1


k, n = list(map(int, input().split()))
lines = []
for _ in range(k):
    lines.append(int(input()))
print(solution(lines, n))

# 4 11
# 802
# 743
# 457
# 539

# 200
