
import string

t = int(raw_input())
n = int(raw_input())

for testcases in range(0,t):
    for count in range(0,n):
        names = str(raw_input())
        names_list = []
        names_list = list(names)
        output = []

        for i in names_list:
            for j in names:
                if i == j:
                    names_list.remove(i)


print names_list



for item in range(len(list)):
        if list[item] == pattern[0] and list[item:item+len(sublist)] == sublist:
            print i
        else:
            print -1