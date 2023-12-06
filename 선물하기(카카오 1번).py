from itertools import combinations

def solution(friends, gifts):
    # 다음 달에 받을 선물의 개수
    precise = {friend: 0 for friend in friends}

    # 선물 지수
    gift_score = {friend: 0 for friend in friends}
    for gift in gifts:
        gift_from, gift_to = list(gift.split())
        gift_score[gift_from] += 1
        gift_score[gift_to] -= 1

    pairs = list(combinations(friends, 2))
    for pair in pairs:
        left_to_right = gifts.count("{} {}".format(pair[0], pair[1]))
        right_to_left = gifts.count("{} {}".format(pair[1], pair[0]))
        if left_to_right > right_to_left:
            precise[pair[0]] += 1
        elif left_to_right < right_to_left:
            precise[pair[1]] += 1
        else:
            if gift_score[pair[0]] > gift_score[pair[1]]:
                precise[pair[0]] += 1
            elif gift_score[pair[0]] < gift_score[pair[1]]:
                precise[pair[1]] += 1
            else:
                continue
    
    return max(precise.values())