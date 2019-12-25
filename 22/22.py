from collections import deque
deck = deque()
deck_size = 119315717514047
desk_space = [-1 for x in range(deck_size)]
for i in range(deck_size):
    deck.append(i)
_input = open('22.in').read().split('\n')[:-1]
_input *= 101741582076661
techniques = {
    "deal into new": 1,
    "cut": 2,
    "deal with increment": 3
}

for i in _input:
    func = " ".join(i.split()[:-1])
    param = i.split()[-1]
    deal = techniques[func]

    if deal == 1:
        deck.reverse()
    elif deal == 2:
        deck.rotate(-1 * int(param))
    else:
        index = 0
        increment = int(param)
        while deck:
            card = deck.popleft()
            desk_space[index] = card
            index = (index + increment) % deck_size
        for card in desk_space:
            deck.append(card)
print(deck.index(2019))

