def solution(s):
    numbers = list(map(int, s.split()))

    answer = "{min} {max}".format(min=min(numbers), max=max(numbers))
    return answer