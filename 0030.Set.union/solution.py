n = int(input())

Sn = input().split()

m = int(input())

Sm = input().split()

Setn = set(Sn)

Setm = set(Sm)

print(len(Setn.union(Setm)))