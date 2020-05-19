#!/usr/bin/env python3

def count_substring(string, sub_string):
    count = 0
    for i in range(1,len(string)+1):
        for j in range(i):
            print(j,i,string[j:i],sub_string)
            if string[j:i] != "" and string[j:i] == sub_string: count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)