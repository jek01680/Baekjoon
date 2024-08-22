N = int(input())

min = 0
for i in range(N, 0, -1):
    res = sum(int(digit) for digit in str(i))
    if res+i == N:
        min = i

print(min)