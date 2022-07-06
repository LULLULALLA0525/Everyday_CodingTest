from itertools import permutations
from math import perm
from operator import ne

def compare_id(u, b):
    if b == []:
        return True
    
    if len(b) == len(u):
        for c in range(len(b)):
            if b[c] == u[c] or b[c] == '*':
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
    
    print(ban)
    
    possible_id = list(permutations(ban, len(ban)))
    new_possible_id = [] 
    for p in possible_id:
        if p not in new_possible_id:
            new_possible_id.append(p)
    
    print(new_possible_id)
    
    return result

user_id = list(input().split())
# frodo fradi crodo abc123 frodoc

banned_id = list(input().split())
# fr*d* *rodo ****** ******

print(solution(user_id, banned_id))
# 3