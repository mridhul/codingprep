def number_needed(a, b):
    count = 0
    checklist_a = []
    checklist_b = []
    for i in a:
        if i not in b and i not in checklist_a:
            print "{} not in {}".format(i,b)
            count = count + 1
        else:
            checklist_a.append(i)
            print checklist_a
    for j in b:
        if j not in a and j not in checklist_b:
            print "{} not in {}".format(j, a)
            count = count + 1
        else:
            checklist_b.append(j)
            print checklist_b

    return count

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

'''  this shit works !!
a = input().strip()
b = input().strip()
print(sum(abs(a.count(i) - b.count(i)) for i in 'abcdefghijklmnopqrstuvwxyz'))

'''