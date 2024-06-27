# Pair of gloves
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of 
# pair of gloves you can constitute from the gloves you have in your drawer.

# Given an array describing the color of each glove, return the number of pairs you can constitute, 
# assuming that only gloves of the same color can form pairs.

# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2 (1 red pair + 1 blue pair)

# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)



def solution(gloves): # O(n)
    glove_count = {} # O(1)
    for color in gloves: # O(n)
        if color in glove_count: # O(1)
            glove_count[color] += 1 # O(1)
        else:
            glove_count[color] = 1 # O(1)
    pair_count = 0 # O(1)
    for color, count in glove_count.items(): # O(n)
        pair_count += count // 2 #O(1)
    return pair_count # O(1)

def solution(gloves): # O(n**2)
    unique_gloves = set(gloves)
    pair_count = 0
    for glove in unique_gloves:
        pair_count += gloves.count(glove) // 2
    return pair_count

def solution2(gloves):
    singles = set()
    count = 0
    for glove in gloves:
        if glove in singles:
            count += 1
            singles.remove(glove)
        else:
            singles.add(glove)
    return count