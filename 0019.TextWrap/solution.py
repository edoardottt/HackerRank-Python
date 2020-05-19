def wrap(string, max_width):
    res = ""
    i = 0
    while i < len(string):
        if i+max_width < len(string):
            res += string[i:i+max_width] + "\n"
            i = i+max_width
        else: 
            res += string[i:len(string)]
            i = len(string) + 2
    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)