import operator

def best_hotels():
    #sorted_hotels = sorted(myDB.items(), key=operator.itemgetter(1))


    sorted_hotels =  sorted(myDB,key=myDB.__getitem__)
    for hotel in sorted_hotels:
        print set(list(hotel))

n = int(raw_input())


myDB = {}
for i in range(n):
    hotels,rating = raw_input().strip().split()
    myDB[hotels]=rating

best_hotels()

