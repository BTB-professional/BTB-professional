# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 13:49:33 2022

@author: BOBOYOR
"""

table=8
for i in range(1,11):
    print(table,'x',i,'=?')
    pup=input()
    if pup=='bilmayman':
        break
    if pup=='keyingisi':
        print('Keyingi savol')
        continue
    res=table*i
    if int(pup)==res:
        print('Barakalla!')
    else:
        print('Xato!')
        print('Tugadi')
    