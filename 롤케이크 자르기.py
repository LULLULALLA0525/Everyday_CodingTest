def solution(topping):
    answer = 0

    num1 = [0] * 10001
    cnt1 = 0
    num2 = [0] * 10001
    cnt2 = 0

    num1[topping[0]] += 1
    cnt1 += 1
    for i in range(1, len(topping)):
        num2[topping[i]] += 1
        if num2[topping[i]] == 1:
            cnt2 += 1

    for i in range(1, len(topping) - 1):
        num1[topping[i]] += 1
        if num1[topping[i]] == 1:
            cnt1 += 1
        num2[topping[i]] -= 1
        if num2[topping[i]] == 0:
            cnt2 -= 1
        if cnt1 == cnt2:
            answer += 1
    return answer
