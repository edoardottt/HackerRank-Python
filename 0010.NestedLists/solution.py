if __name__ == '__main__':
    dictio = {}
    lend = 0
    for _ in range(int(input())):
        lend += 1
        name = input()
        score = float(input())
        dictio[name] = score
    minimum = min(list(dictio.values()))
    results = []
    result = 10000
    for key in dictio.keys():
        if dictio[key] < result and dictio[key] > minimum:
            result = dictio[key]
    for key in dictio.keys():
        if dictio[key] == result:
            results.append(key)
    results.sort()
    for item in results:
        print(item)
