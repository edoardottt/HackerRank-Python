n = int(input())
s = set(map(int, input().split()))

commands = int(input())

while commands != 0:
    command = str(input())
    command = command.split()
    if command[0] == "pop":s.pop()
    else:
        op, elem = command[0],command[1]

        if op == "discard": s.discard(int(elem))

        else: s.remove(int(elem))

    commands -= 1

print(sum(s))