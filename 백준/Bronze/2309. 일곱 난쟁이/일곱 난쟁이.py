from itertools import combinations;

heights = [int(input()) for _ in range(9)]
for C in combinations(heights,7):
    if sum(C) == 100 :
        for height in sorted(C):
            print(height)
            
        break