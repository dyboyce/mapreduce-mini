#!/usr/bin/env python
import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
# [derive mapper output key values]
    line = line.strip()
    keys = line.split()
    key = keys[2]
    value = (keys[0]+", "+keys[1]+", "+keys[3]+", "+keys[4]+", "+keys[5]+", "+keys[6]+", "+keys[7])
    print('%s\t%s') % (key, value)