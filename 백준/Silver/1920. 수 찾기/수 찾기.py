N = int(input())
arrN = set(map(int, input().split()))
M = int(input())
arrM = list(map(int, input().split()))

for i in arrM:
    print(1) if i in arrN else print(0)