# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:45:40 2020

@author: Suboy
"""
n=int(input("so lan lap: "))


for i in range(n):
    
    print('lan lap thu ',i+1 )
    print("ax + b = c")
    a=float(input("a = "))
    b=float(input("b = "))
    c=float(input("c = "))
    if a==0 and b==c:
        print("phuong trinh vo so nghiem")
    elif a==0 and b!=c:
        print("phuong trinh vo nghiem")
    else:
        print("x = ",(c-b)/a)
    n-=1
print(" ket thuc")

    
        



