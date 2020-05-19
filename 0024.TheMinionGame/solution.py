def minion_game(string):
    k,s = 0,0
    vowels = 'AEIOU'
    for i in range(len(string)):
        if string[i] in vowels:
            k += (len(string)-i)
        else:
            s += (len(string)-i)

    if k > s:
        print("Kevin {}".format(k))
    elif k < s:
        print ("Stuart {}".format(s))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)