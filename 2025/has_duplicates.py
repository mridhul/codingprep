def has_duplicates(lst):
    seen = list()
    for item in lst:
        if item in seen:
            return True
        seen.append(item)
    return False


#Test duplicates
#print(has_duplicates(['10','20','30','40','50']))
#print(has_duplicates(['10','20','30','10','50']))


#Test duplicates
print(has_duplicates(['10','20','30','40','50']))
print("-------------------")
print(has_duplicates(['10','20','30','10','50']))