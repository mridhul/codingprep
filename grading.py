#!/bin/python

import sys

def solve(grades):
    # Complete this function
    newgrade=[]
    for grade in grades:
        #print "out"
        if grade >= 38:
            rem = grade % 5
            #print rem
            if rem>2:
                grade = grade + (5-rem)
                print grade
            else:
                print grade
        else:
            print grade



n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
#print(result)