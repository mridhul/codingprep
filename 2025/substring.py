from itertools import combinations

def substring(s):
    result = list()
    for i in range(1, len(s)+1):
        for combo in combinations(range(len(s)),i):
            substring = ''.join(s[j] for j in combo)
            result.append(substring)
    return result
            
def combo(s):
    result = []
    #a = combinations(s,len(s))
    #b = combinations(s,len(s)-1)
    #c = combinations(s,len(s)-2)
    #y = [''.join(j) for j in a]
    #result.append(y)
    #y = [''.join(j) for j in b]
    #result.append(y)
    #y = [''.join(j) for j in c]
    #result.append(y)
    
    for i in range(1, len(s)+1):
        combo = combinations(s,i)
        subs = [''.join(j) for j in combo]
        result.append(subs)
    return result
    
    
#round
str="xyz"
print(substring(str))
print(combo(str))
