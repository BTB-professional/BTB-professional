# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 15:33:29 2022

@author: BOBOYOR
"""

ismlar=['Ozodbek','Javohir','Asilbek']
print(f"Salom {ismlar[0]}, Bugun choyxona bormi?")
print(f"{ismlar[1]},choyxonaga boramizmi?")
print(f"{ismlar[2]},yur kettik.")

sonlar=[45,-100,120_450_120,1.5]
print(sonlar[0]+sonlar[1])
sonlar.remove(120_450_120)
print(sonlar)
sonlar.append(-2000)
print(sonlar)
sonlar.insert(2,2.98)
print(sonlar)
del sonlar[2]
print(sonlar)
yangi_son=sonlar.pop(2)
print(yangi_son)

t_shaxslar=['Alisher Navoiy','Bobur Mirzo','Abdulla Avloniy']
z_shaxslar=['Shavkat Mirziyoyev','Bunyod Jumayev','Gulnoza Bobomurodova']
a=t_shaxslar.pop(0)
b=z_shaxslar.pop(0)
print(f"Men tarixiy shaxlardan {a} bilan, zamonaviy shaxslardan esa {b} bilan suhbat qilishni istar edim.")

friends=[]
friends.append('Ozodbek')
friends.append('Javohir')
friends.append('Amirbek')
friends.append('Doston')
friends.append('Shohjahon')
print(friends)

yangi_mehmon=ismlar.pop(2)
friends.append(yangi_mehmon)
print(friends)

print('dars tugadi')




