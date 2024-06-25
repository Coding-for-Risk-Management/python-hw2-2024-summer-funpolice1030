#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:34:14 2024

@author: xiaomao
"""
import numpy as np


def FizzBuzz(start, finish):
    fbRange=np.arange(start, finish+1)
    mod3=np.mod(fbRange, 3)
    mod5=np.mod(fbRange, 5)
    
    fizzbuzz= np.array(fbRange, dtype=object)
    fizzbuzz[(mod3 == 0) & (mod5 == 0)] = "fizzbuzz"
    fizzbuzz[(mod3 == 0) & (mod5 != 0)] = "fizz"
    fizzbuzz[(mod5 == 0) & (mod3 != 0)] = "buzz"
    
    return fizzbuzz.tolist()
    



    
