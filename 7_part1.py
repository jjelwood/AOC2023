input = open("7.txt").read()
test = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

hands = [hand.split() for hand in input.split("\n")]
strengths = {
    "2":0,
    "3":1,
    "4":2,
    "5":3,
    "6":4,
    "7":5,
    "8":6,
    "9":7,
    "T":8,
    "J":9,
    "Q":10,
    "K":11,
    "A":12
}

def hand_strength(hand):
    counts = get_counts(hand)
    if is_n_of_a_kind(counts, 5):
        return 6
    if is_n_of_a_kind(counts, 4):
        return 5
    is_3 = is_n_of_a_kind(counts, 3)
    is_2 = is_n_of_a_kind(counts, 2)
    if is_3 and is_2:
        return 4
    if is_3:
        return 3
    if len([count for count in counts.values() if count == 2]) == 2:
        return 2
    if is_2:
        return 1
    return 0

def get_counts(cards):
    counts = {}
    for card in cards:
        counts[card] = counts.get(card, 0) + 1
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

print(hands_by_strength)

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