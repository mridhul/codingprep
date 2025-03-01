def find_duplicates(lst):
    seen = list()
    dupe = list()
    for item in lst:
       if item in seen:
           if item not in dupe:
               dupe.append(item)
       seen.append(item)
    return dupe



#tests
print(find_duplicates([1, 2, 3, 2, 1, 5, 6, 5, 5, 5]))
