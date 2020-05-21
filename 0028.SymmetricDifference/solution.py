m = int(input())
setM = set(map(int,input().split()))
n = int(input())
setN = set(map(int,input().split()))

union = setM.union(setN)
result = union.difference(setM.intersection(setN))

res = sorted(list(result))

for elem in res: print(elem)