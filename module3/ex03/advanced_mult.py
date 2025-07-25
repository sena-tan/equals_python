#!/usr/bin/env python

y = 0
while y <= 10:
    print("Table of",y,": ",end=" ")
    x = 0
    while x <= 10:
        print(y * x, end='\n' if x == 10 else ' ')
        x += 1
    y += 1
