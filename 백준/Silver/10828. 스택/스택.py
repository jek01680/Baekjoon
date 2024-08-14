import sys

stk = []
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stk.append(command[1])
    elif command[0] == 'pop':
        print(stk.pop() if stk else -1)
    elif command[0] == 'size':
        print(len(stk))
    elif command[0] == 'empty':
        print(0 if stk else 1)
    elif command[0] == 'top':
        print(stk[-1] if stk else -1)