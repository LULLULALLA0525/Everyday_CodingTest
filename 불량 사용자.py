from itertools import permutations

def compare_id(u, p):
    if p == []:
        return True
    
    if len(p) == len(u):
        for c in range(len(p)):
            if p[c] == u[c] or p[c] == '*':
                continue
            else:
                return False
    else:
        return False
    return True

def solution(user_id, banned_id):
    result = 0
    
    ban = [b for b in banned_id]
    for _ in range(len(user_id) - len(banned_id)):
        ban.append([])
    
    temp = list(permutations(ban, len(ban)))
    possible_id = [] 
    for p in temp:
        if p not in possible_id:
            possible_id.append(p)
    
    for p in possible_id:
        cnt = 0
        for i in range(len(p)):
            if compare_id(user_id[i], p[i]):
                cnt += 1
        if cnt == len(user_id):
            result += 1
    
    return result

user_id = list(input().split())
# frodo fradi crodo abc123 frodoc

banned_id = list(input().split())
# fr*d* *rodo ****** ******

print(solution(user_id, banned_id))
# 3