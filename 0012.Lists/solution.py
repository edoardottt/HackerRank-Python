if __name__ == '__main__':
    N = int(input())

li = []
for c in range(N):
    i = input()
    if i[:6]=='insert':
        a = i.split()
        index = int(a[1])
        value = int(a[2])
        li.insert(index,value)
    elif i[:5]=='print':
        print(li)
    elif i[:6]=='remove':
        a = i.split()
        li.remove(int(a[1]))
    elif i[:6]=='append':
        a = i.split()
        li.append(int(a[1]))
    elif i[:4]=='sort':
        li.sort()
    elif i=='pop':
        li.pop()
    elif i=='reverse':
        li.reverse()
