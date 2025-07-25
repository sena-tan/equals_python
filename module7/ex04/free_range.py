#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
 print("none")
else:
 if sys.argv[1] >= sys.argv[2]:
  print("First number should be smaller than the second.")
 else:
  print(list(range(int(sys.argv[1]),int(sys.argv[2])+1))) #+1 to add the bigger num too!!