#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

def YCbCr_int_to_rgb(YCbCr, n):
    Y = (YCbCr[0] - (16 * 2**(n - 8))) / (219 * 2**(n - 8))
    Cb = (YCbCr[1] - (128 * 2**(n - 8))) / (224 * 2**(n - 8))
    Cr = (YCbCr[2] - (128 * 2**(n - 8))) / (224 * 2**(n - 8))
    r = 1.5748*Cr + Y
    b = 1.8556*Cb + Y
    g = (Y - 0.2126*r - 0.0722*b)/0.7152
    return r, g, b

def illegal(x):
    if x > 1.0 or x < 0.0:
        return True
    else:
        return False

legalTotal = 0
illegalTotal = 0

for Y in range(256):
    legalCount = 0
    illegalCount = 0
    for Cb in range(256):
        for Cr in range(256):
            r, g, b = YCbCr_int_to_rgb([Y, Cb, Cr], 8)
            if illegal(r) or illegal(g) or illegal(b):
                illegalCount += 1
            else:
                legalCount += 1
    print( "Y' = %d, legal = %d, illegal = %d" % (Y, legalCount, illegalCount) )
    legalTotal += legalCount
    illegalTotal += illegalCount

print( "\nLegal: %d\nIllegal: %d" % (legalTotal, illegalTotal) )
print( "\n%.1f%% of the 8-bit Y'CbCr code values represent legal RGB values\n" % (100 * legalTotal / (illegalTotal + legalTotal)) )
