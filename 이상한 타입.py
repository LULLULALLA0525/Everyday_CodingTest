import sys
from collections import defaultdict

input = lambda: sys.stdin.readline()

TP, NUM = 0, 1
def defaultVariable():
    return ("", "")

def checkDigitType(type, digit):
    if type == 'a':
        return 1 <= digit and digit <= 9
    elif type == 's':
        return 1 <= digit and digit <= 4
    elif type == 'b':
        return 5 <= digit and digit <= 9
    else:
        return False

def checkType(type, value):
    for i in range(len(type)):
        if not checkDigitType(type[i], int(value[i])):
            return False
    return True

def throwError(errors, code, message):
    # print(code + " | " + message)
    return errors + 1

def solution(types, codes):
    answer = []
    errors = 0

    type_info = defaultdict(str)
    for type in types:
        tp, info = type.split()
        type_info[tp] = info

    memory = defaultdict(defaultVariable)
    for code in codes:
        keywords = code.split()
        if keywords[0] == "declare":
            tp, var, num = keywords[1:]
            if type_info[tp] == "":
                errors = throwError(errors, code, "tp라는 데이터 타입이 없으면 에러가 발생한다.")
                continue
            elif type_info[var] != "":
                errors = throwError(errors, code, "var이라는 데이터 타입이 있으면 에러가 발생한다.")
                continue
            elif memory[var] != defaultVariable():
                errors = throwError(errors, code, "이미 선언된 변수가 있다면 에러가 발생한다.")
                continue
            elif not checkType(type_info[tp], num):
                errors = throwError(errors, code, "num이 데이터 타입 tp를 만족하지 못할 경우 에러가 발생한다.")
                continue
            else:
                memory[var] = (tp, num)
        elif keywords[0] == "update":
            if keywords[2].isdigit():
                var, num = keywords[1:]
                if memory[var] == defaultVariable():
                    errors = throwError(errors, code, "var이 선언되어 있지 않으면 에러가 발생한다.")
                    continue
                elif not checkType(type_info[memory[var][TP]], num):
                    errors = throwError(errors, code, "num이 var의 데이터 타입을 만족하지 못할 경우 에러가 발생한다.")
                    continue
                else:
                    memory[var] = (memory[var][TP], num)
            else:
                var1, var2 = keywords[1:]
                if memory[var1] == defaultVariable() or memory[var2] == defaultVariable():
                    errors = throwError(errors, code, "var1과 var2가 선언되어 있지 않으면 에러가 발생한다.")
                    continue
                else:
                    tp1, num1 = memory[var1]
                    tp2, num2 = memory[var2]
                    if not checkType(type_info[tp1], num2):
                        errors = throwError(errors, code, "var2의 값이 var1의 데이터 타입을 만족하지 못할 경우 에러가 발생한다.")
                        continue
                    else:
                        memory[var1] = (tp1, num2)
        elif keywords[0] == "print":
            var = keywords[1]
            if memory[var] == defaultVariable():
                errors = throwError(errors, code, "var이 선언되어 있지 않으면 에러가 발생한다.")
                continue
            else:
                answer.append(int(memory[var][NUM]))
        else:
            errors += 1

    answer.append(errors)
    return answer

# a: 1~9, s: 1~4, b: 5~9
TEST_TYPES = [
    "atype aaba",
    "btype assa",
    "ctype asba"
]
TEST_CODES = [
    "declare atype a 1865",     # a <- 1865
    "declare btype b 8923",     # error
    "print a",                  # print 1865
    "print b",                  # error
    "declare ctype c 3399",     # c <- 3399
    "update b 5229",            # error
    "update a c",               # a <- 3399(c)
    "update c 2381",            # c <- 2381
    "print a",                  # print 3329
    "print b",                  # error
    "print c"                   # print 2381
]
print(solution(TEST_TYPES, TEST_CODES))     # [1865, 3399, 2381, 4]