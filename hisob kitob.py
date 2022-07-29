# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:25:48 2022

@author: BOBOYOR
"""


table=8
for i in range(1,11):
     print(table,'x',i,'=?')
     pup=input()
     if pup=='bilmayman':
         break
     res=table*i
     if int(pup)==res:
         print('Barakalla!')
     else:
         print("Noto'gri, to'gri javob:",res)
         print('Tugadi')
         
                 
                   
    
