if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    maximum = max(arr)
    result = min(arr)
    for i in range(1,n):
        if arr[i] > result and arr[i]!= maximum:
            result = arr[i]
    print (result)
