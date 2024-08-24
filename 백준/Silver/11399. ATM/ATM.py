import sys
input = sys.stdin.readline

answer = 0
N = int(input())
P = [*map(int, input().split())]
P.sort()

sum=0
for i in P:
    sum += i
    answer += sum

print(answer)