import sys

input = lambda: sys.stdin.readline()

def checkType(type, digit):
    if type == 'a':
        return 1 <= digit and digit <= 9
    elif type == 's':
        return 1 <= digit and digit <= 4
    elif type == 'b':
        return 5 <= digit and digit <= 9
    else:
        return False

def solution(types, codes):
    answer = []
    errors = 0

    for code in codes:
        keywords = code.split()
        if keywords[0] == "declare":
            TODO
        elif keywords[0] == "update":
            TODO
        elif keywords[0] == "print":
            TODO
        else:
            errors += 1

    answer += [errors]
    return answer

# a: 1~9, s: 1~4, b: 5~9
TEST_TYPES = [
    "atype aaba",
    "btype assa",
    "ctype asba"
]
TEST_CODES = [
    "declare atype a 1845",     # a <- 1845
    "declare btype b 8923",     # error
    "print a",                  # print 1845
    "print b",                  # error
    "declare ctype c 3329",     # c <- 3329
    "update b 5229",            # error
    "update a c",               # a <- 3329(c)
    "update c 2381",            # c <- 2381
    "print a",                  # print 3329
    "print b",                  # error
    "print c"                   # print 2381
]
print(solution(TEST_TYPES, TEST_CODES))     # [1845, 3329, 2381, 4]