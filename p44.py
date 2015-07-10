from __future__ import division
import math
 
def main(n):
    p = set(i * ((3 * i) - 1) / 2 for i in range(2, n))
    for i in p:
        for j in p:
            if i + j in p and j - i in p:
                x = i - j
            else:
                continue
    print "Answer = ", math.fabs(x)

main(4000)