#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 08:07:22 2018

@author: fenarius
"""

def trouve_libre(L,n):
    t=len(L)
    libre=list(range(1,t+1))
    for i in range (0,n):
            if L[i] in libre:
                libre.remove(L[i])
            if L[i]+i-n in libre :
                libre.remove(L[i]+i-n)
            if L[i]+n-i in libre :
                libre.remove(L[i]+n-i)
    return libre

def place_reine(L,n,ES):
    if n==len(L):
        ES.append(L.copy())
    else:       
        Plibre=trouve_libre(L,n)
        for i in Plibre:
            L[n]=i
            place_reine(L,n+1,ES)
        L[n]=0
    return ES

te=int(input("Taille de l'échiquier="))
ce=[0]*te
Solutions=place_reine(ce,0,[])
print("Il y a ",len(Solutions)," solutions !",sep='')