
with open("./input.txt") as file:
    cards: list[str] = file.readlines()



i = 0
while i < len(cards):
    card = cards[i]
    card_numbers = card.split(":")
    card_index = int(card_numbers[0].split()[1])
    card_numbers = card_numbers[1]
    winning_n, scratched_n =  ''.join(card_numbers).split('|')
    winning_n = set(map(int, winning_n.strip().split()))
    scratched_n = set(map(int, scratched_n.strip().split()))
    n_winning = 0
    for win_number in winning_n:
        if win_number in scratched_n:
            n_winning += 1
    
    # Since cards start count with 1, the card_index is actually the index of the original next card
    # inside the cards table
    next_cards = cards[card_index: card_index + n_winning]
    cards.extend(next_cards)
    i += 1


print(len(cards))
