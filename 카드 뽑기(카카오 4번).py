def convert(n, card):
    if card < (n + 1) / 2:
        return card
    else:
        return n + 1 - card

def solution(coin, cards):
    n = len(cards)
    cards = list(map(lambda card: convert(n, card), cards))
    hand = cards[:(n//3)]
    matched = []
    not_matched = []
    for card in hand:
        if card in not_matched:
            matched.append(card)
            not_matched.remove(card)
        else:
            not_matched.append(card)

    # 초기에 손에 있는 페어의 수만큼 확정적으로 다음 라운드로 넘어갈 수 있음 따라서 해당 라운드부터 시작해도 무관
    current_round = len(matched)
    pickable_cards = cards[(n//3):(n//3)+(2*current_round)]
    while current_round <= n//3:
        current_round += 1
        pickable_cards += cards[(n//3)+(2*(current_round-1)):(n//3)+(2*(current_round-1)) + 2]

        card_match = False

        for card in not_matched:
            if card in pickable_cards and coin >= 1:
                matched.append(card)
                not_matched.remove(card)
                pickable_cards.remove(card)
                coin -= 1
                card_match = True
                break
        
        if card_match:
            continue
            
        for card in pickable_cards:
            if pickable_cards.count(card) == 2 and coin >= 2:
                matched.append(card)
                pickable_cards.remove(card)
                pickable_cards.remove(card)
                coin -= 2
                card_match = True
                break
        
        if not card_match:
            break

    return current_round