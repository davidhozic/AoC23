
card_powers = {
    "A" : 14,
    "K" : 13,
    "Q" : 12,
    "J" : 1,
    "T" : 10,
}
def convert_card(card: str):
    return card_powers.get(card) or int(card)


with open("./input.txt") as file:
    hands_bids = file.read().splitlines()
    hands_bids = list(map(str.split, hands_bids))
    hands_binds = [(list(map(convert_card, hand)), int(bid)) for hand, bid in hands_bids]


def is_5_of_a_kind(counts: dict):
    for c in counts.values():
        if c == 5:
            return True
    
    return False

def is_4_of_a_kind(counts: dict):
    for c in counts.values():
        if c == 4:
            return True
    
    return False

def is_full_house(counts: dict):
    card_with_3 = None
    for card, count in counts.items():
        if count == 3:
            card_with_3 = card
            break
    else:
        return False

    counts = counts.copy()

    del counts[card_with_3]
    remaining = max(counts.values())
    return remaining == 2

def is_three_of_kind(counts: dict):
    card_with_3 = None
    for card, count in counts.items():
        if count == 3:
            card_with_3 = card
            break
    else:
        return False

    counts = counts.copy()
    del counts[card_with_3]
    return all(count == 1 for count in counts.values())

def is_two_pair(counts: dict):
    counts_2_cnt = 0
    for v in counts.values():
        if v == 2:
            counts_2_cnt += 1

    return counts_2_cnt == 2

def is_one_pair(counts: dict):
    counts_2_cnt = 0
    for v in counts.values():
        if v == 2:
            counts_2_cnt += 1

    return counts_2_cnt == 1

def get_score(hand: list) -> int:
    counts = {card: hand.count(card) for card in set(hand)}
    n_jokers = 0
    if 1 in counts:
        n_jokers = counts[1]
        del counts[1]

    if counts:
        max_k = max(counts, key=lambda k: counts[k])
        counts[max_k] += n_jokers
    else:
        counts[1] = n_jokers

    if is_5_of_a_kind(counts):
        return 7

    if is_4_of_a_kind(counts):
        return 6

    if is_full_house(counts):
        return 5

    if is_three_of_kind(counts):
        return 4

    if is_two_pair(counts):
        return 3

    if is_one_pair(counts):
        return 2

    return 1

handbids_scores = {}
total_winnings = 0

for hand, bid in hands_binds:
    score = get_score(hand)
    handbids_scores[score] = handbids_scores.get(score, [])
    handbids_scores[score].append((hand, bid))


rank = 1
for score in range(1, 8):
    hands: list = handbids_scores.get(score)
    if hands is None:
        continue
        
    hands = sorted(hands, key=lambda hand_bid: hand_bid[0])
    for hand, bid in hands:
        total_winnings += rank * bid
        rank += 1


print(total_winnings)
