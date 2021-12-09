#!/usr/bin/env python
import sys
# [Define group level master information]
def reset():
    #[Logic to reset master info for every new group]
    pass

 # Run for end of every group
def flush():
    # [Write the output]
    pass

# input comes from STDIN
for line in sys.stdin:
    # [parse the input we got from mapper and update the master info]

    # [detect key changes]

    if current_vin != vin:
        if current_vin != None:
# write result to STDOUT
            flush()
        reset()
# [update more master info after the key change handling]
    current_vin = vin
# do not forget to output the last group if needed!
flush()