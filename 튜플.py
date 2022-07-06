
def solution(s):
    result = []
    
    isStart, isEnd = True, False
    s_list = []
    temp = []
    num = 0
    for c in s:
        if isStart: 
            isStart = False
        elif c == '}' or c == ',':
            if isEnd:
                continue
            temp.append(num)
            num = 0
            isEnd = False
            if c == '}':
                s_list.append(temp)
                temp = []
                isEnd = True
        elif c == '{':
            isEnd = False
        else:
            num = num * 10 + int(c)

    s_list.sort(key = lambda x: len(x))
    
    for elem in s_list:
        for num in elem:
            if num not in result:
                result.append(num)
                break
    
    return result

# {{2},{2,1},{2,1,3},{2,1,3,4}}
s = input()

# [2, 1, 3, 4]
print(solution(s))