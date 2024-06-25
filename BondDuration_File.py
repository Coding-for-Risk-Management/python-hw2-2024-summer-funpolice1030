#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:10:48 2024

@author: xiaomao
"""

import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    t=np.arange(1,ppy*m+1)
    cpn=couponRate*face/ppy
    df=(1/(1+y/ppy))
    dft=[df**i for i in t]
    bondPrice=cpn*sum(dft)+dft[-1]*face
    bondDuration=(cpn*sum(dft*t)+m*dft[-1]*face)/bondPrice
    return(bondDuration)


# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy= 1

getBondDuration(y, face, couponRate, m, ppy=1)