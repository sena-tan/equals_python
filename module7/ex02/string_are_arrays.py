#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 2:
 print("none")
else:
 print("".join(re.findall("z",sys.argv[1])) or "none") #leave empty, so it'll be zzzzz
