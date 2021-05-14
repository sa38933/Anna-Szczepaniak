# -*- coding: utf-8 -*-
"""
Created on Sun May  9 14:38:10 2021

@author: Ania
"""


ciag=[4,3,5,2,1]
n=5
maksimum=ciag[0]
imax=0
i=1


while i<n:
    if ciag[i]>maksimum:
        maksimum=ciag[i]
        imax=i
    i=i+1
        
        
print(maksimum,imax)
        
        