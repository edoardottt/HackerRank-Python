n = int(input())

array = []

for i in range(n):
    array.append(input())
print(len(set(array)))