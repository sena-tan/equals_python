#!/usr/bin/env python
import sys

def shrink(word):
    print(word[:8])
def enlarge(word):
    word = word +"Z" * (8)
#    while len(word) < 8:
#        word+="Z"
    print(word)

words=sys.argv[1:]
for word in words:
    if len(word)>8:
        shrink(word)
    elif len(word)<8:
        enlarge(word)
    else: print(word)