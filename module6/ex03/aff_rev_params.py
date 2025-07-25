#!/usr/bin/env python
import sys

if len(sys.argv) <= 3:
 print("none")
else:
 print("\n".join(list(reversed(sys.argv[1:]))))