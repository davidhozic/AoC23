





with open("./input.txt") as file:
    cards: list[str] = file.readlines()



total_points = 0
for card in cards:
    card = card.strip()
    card_worth = 0
    winning_n, scratched_n =  ''.join(card.split(': ')[1:]).split('|')
    winning_n = set(map(int, winning_n.strip().split()))
    scratched_n = set(map(int, scratched_n.strip().split()))
    for win_number in winning_n:
        if win_number in scratched_n:
            if card_worth:
                card_worth *= 2
            else:
                card_worth = 1


    total_points += card_worth


print(total_points)
