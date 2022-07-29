cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())

login = input("Loginni kiriting: ")
if login == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login}!")
    
son_1 = float(input("1-sonni kiriting: "))
son_2 = float(input("2-sonni kiriting: "))
if son_1==son_2:
    print("Sonlar teng ekan!!!")

son = float(input("Istalgan sonni kiriting: "))
if son > 0:
    print("Musbat son")
if son < 0:
    print("Manfiy son")

Son = float(input("Son kiriting: "))
Son_1 = float(input("Musbat son kiriting: ")) 
if Son > 0:
    print(Son**(1/2))
if Son < 0:
    Son_1
    if Son_1 > 0:
        print(Son_1**(1/2))
        