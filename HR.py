
mylist = [1,2,3,4]
pattern = [2 ,2]

# def getmatch(mylist, pattern):
#     found = []
#     for i in range(len(mylist)):
#         if mylist[i] == pattern[0] and mylist[i:i+len(pattern)] == pattern:
#             print i
#             found.append(pattern)
#     return found
#
# print getmatch(mylist,pattern)

def getmatch(mylist, pattern):
    found = []
    for i in range(len(mylist)):
        if mylist[i] == pattern[0] and mylist[i:i+len(pattern)] == pattern:
            return i
        else:
            return -1

print getmatch(mylist,pattern)