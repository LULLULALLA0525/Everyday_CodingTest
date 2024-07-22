def solution(levels, k):
    answer = 0
    
    levels = sorted(levels, reverse=True)
    maxLevel = levels[0]
    
    maxLevelCharacterCount = 0
    remainItems = k
    # 최대레벨 캐릭터의 최대 개수(maxLevelCharacterCount) 계산
    for level in levels:
        requiredItems = maxLevel - level
        if requiredItems <= remainItems:
            maxLevelCharacterCount += 1
            remainItems -= requiredItems
        else:
            break
    # 마지막 캐릭터는 필수적으로 포함될 캐릭터가 아니므로 제
    remainItems += maxLevel - levels[maxLevelCharacterCount - 1]
    
    for i in range(maxLevelCharacterCount - 1, len(levels)):
        if maxLevel > remainItems + levels[i]:
            answer = len(levels) - i
            break
            
    return answer

TEST_LEVELS_1 = [7, 1, 2, 4, 3]
TEST_K_1 = 8
print(solution(TEST_LEVELS_1, TEST_K_1))    # 1

TEST_LEVELS_2 = [100, 99, 1, 1]
TEST_K_2 = 99
print(solution(TEST_LEVELS_2, TEST_K_2))    # 0