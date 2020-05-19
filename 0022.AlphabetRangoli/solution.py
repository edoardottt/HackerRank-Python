#!/usr/bin/env python3

import string

def print_rangoli(n):
    alphabet = string.ascii_lowercase
    rangoli = []
    for i in range(n):
        row = "-".join(alphabet[i:n])
        rangoli.append((row[::-1]+row[1:]).center(4*n-3, "-"))
    print('\n'.join(rangoli[:0:-1]+rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)