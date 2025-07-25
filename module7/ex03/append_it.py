#!/usr/bin/env python3
import sys
import re

if len(sys.argv) <=1:
 print("none")
else:
 for word in sys.argv[1:]:
    if re.findall("ism",word):
     continue
    else: print(word+"ism")

##try going with endswith() - findall gives 'ism's everywhere, not only at the end! 