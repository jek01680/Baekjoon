import sys
input = sys.stdin.readline

answer = 0
str = input().strip()
arr = str.split('-')

answer = sum(map(int, arr[0].split('+')))

for num in arr[1:]:
    answer -= sum(map(int, num.split('+')))

print(answer)