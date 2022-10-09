# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 08:54:12 2022

@author: Tebogo Moloto
"""


line='X-DSPAM-Confidence:0.8475'
pos1=line.find(':')
number=line[pos1+1:]
number=float(number)
print('Extracted Output:',number)
