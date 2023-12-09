



with open("./input.txt") as file:
    histories = [list(map(int, history)) for history in map(str.split, file.read().splitlines())]


predictions = []
for history in histories:
    sequences = [history]
    while any(last_sequence := sequences[-1]):
        new_sequence = []
        for i in range(len(last_sequence) - 1):
            new_sequence.append(last_sequence[i+1] - last_sequence[i])

        sequences.append(new_sequence)
    
    last_sequence.insert(0, 0)
    for seq_i in range(len(sequences) - 2, -1, -1):
        sequences[seq_i].insert(0, sequences[seq_i][0] - sequences[seq_i + 1][0])

    predictions.append(sequences[0][0])

print(sum(predictions))
