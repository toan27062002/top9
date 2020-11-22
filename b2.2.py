# -*- coding: utf-8 -*-
"""

Created on Sun Nov 22 16:35:22 2020

@author: Suboy
"""
n=int(input("so lan lap: "))

i=0
while n>0 :
    i+=1
    print('lan lap thu ',i )
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

        