input = open("7.txt").read()
test = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

hands = [hand.split() for hand in input.split("\n")]
strengths = {
    "J":0,
    "2":1,
    "3":2,
    "4":3,
    "5":4,
    "6":5,
    "7":6,
    "8":7,
    "9":8,
    "T":9,
    "Q":10,
    "K":11,
    "A":12
}

def hand_strength(hand):
    counts = get_counts(hand)
    if is_n_of_a_kind(counts, 5) or hand == "JJJJJ":
        return 6
    if is_n_of_a_kind(counts, 4):
        return 5
    if is_full_house(hand, counts):
        return 4
    if is_n_of_a_kind(counts, 3):
        return 3
    if is_double_pair(hand, counts):
        return 2
    if is_n_of_a_kind(counts, 2):
        return 1
    return 0

def is_full_house(hand, counts):
    js = hand.count("J")
    if js == 0:
        return is_n_of_a_kind(counts, 3) and is_n_of_a_kind(counts, 2)
    elif js == 1:
        # is double pair
        return len([count for count in counts.values() if count == 3]) == 2 # count == 3 not 2 to account for the 1 joker 
    elif js == 2:
        return is_n_of_a_kind(counts, 4) # 4 not 2 to account for the 2 jokers 
    else:
        print("This shouldn't run since js>2 => 4 of a kind", hand)

def is_double_pair(hand, counts):
    js = hand.count("J")
    if js == 0:
        return len([count for count in counts.values() if count == 2]) == 2
    elif js == 1:
        return is_n_of_a_kind(counts, 3) # 3 not 2 to account for the 1 joker
    else:
        print("This shouldn't run since js>1 => 3 of a kind", hand)

def get_counts(cards):
    counts = {}
    js = 0
    for card in cards:
        if card != "J":
            counts[card] = counts.get(card, 0) + 1
        else:
            js += 1
    for card in counts:
        counts[card] += js
    return counts

def is_n_of_a_kind(counts, n):
    for count in counts.values():
        if count == n:
            return True
    return False

def compare_hands(h1, h2):
    c1 = h1[0]
    c2 = h2[0]
    for i in range(len(c1)):
        s1 = strengths[c1[i]]
        s2 = strengths[c2[i]]
        if s1 < s2:
            return -1
        if s1 > s2:
            return 1
    return 0

hands_by_strength = [[] for _ in range(7)]
for hand in hands:
    strength = hand_strength(hand[0])
    hands_by_strength[strength].append(hand)

import functools

for hands in hands_by_strength:
    hands.sort(key=functools.cmp_to_key(compare_hands))

rank = 1
result = 0
for hands in hands_by_strength:
    for hand in hands:
        result += rank * int(hand[1])
        rank += 1

print(result)
