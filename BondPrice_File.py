#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:12:11 2024

@author: xiaomao
"""
import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    t=np.arange(1,ppy*m+1)
    cpn=couponRate*face/ppy
    df=(1/(1+y/ppy))
    dft=[df**i for i in t]
    bondPrice=cpn*sum(dft)+dft[-1]*face
    return(bondPrice)


# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy= 1

getBondPrice(y, face, couponRate, m, ppy=1)