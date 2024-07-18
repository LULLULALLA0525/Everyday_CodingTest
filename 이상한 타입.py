import sys

input = lambda: sys.stdin.readline()

def solution(types, codes):
    answer = []
    errors = 0

    

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