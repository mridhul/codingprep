def insert_star_between_pairs(a_string):
    for i in xrange(len(a_string)):
        for j in xrange(i+1,len(a_string)):
            if a_string[i]==a_string[j]:
                return a_string[:j]+"*"+a_string[j:]
                #print a_string[:j],a_string[j:]
    return a_string

print insert_star_between_pairs("abba")