#!/bin/python

import sys


time = raw_input().strip()

fmt = time[-2::]

if fmt == "AM":
    hr = int(time[:2])
    mins = time[3:5]
    secs = time[6:8]
    if hr ==12:
        hr="00"
        print "{}:{}:{}".format(hr, mins, secs)
    else:
        print time[:-2]
else:
    hr= int(time[:2])
    mins=time[3:5]
    secs=time[6:8]
    if hr==12:
        hr="12"
        print "{}:{}:{}".format(hr, mins, secs)
    else:
        print "{}:{}:{}".format(hr+12,mins,secs)