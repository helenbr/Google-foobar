from itertools import combinations

def solution(num_buns, num_required):
    bunnies = [[] for i in range(num_buns)]
    key = 0
    comb = combinations(bunnies, num_buns - num_required + 1)
    for i in comb:
        [item.append(key) for item in i]
        key += 1
    return bunnies