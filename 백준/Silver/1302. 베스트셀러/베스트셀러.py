d = dict()
for _ in range(int(input())):
    book = input()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

m = max(d.values())
result = []
for k, v in d.items():
    if v == m:
        result.append(k)

result.sort()
print(result[0])