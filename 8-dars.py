son = float(input("Juft son kiriting: "))
if son%2:
    print("Bu son juft emas")
else:
    print("Rahmat!")

yosh = int(input("Muzeyga xush kelibsiz!!!\n Yoshingizni kiriting: "))
if yosh <= 4 or yosh >= 60:
    print("Chipta bepul")
elif yosh < 18:
    print("Chipta narxi 10000 so'm")
else:
    print("Chipta narxi 20000 so'm")

x, y = float(input("1-sonni kiriting: ")),float(input("2-sonni kiriting: "))
if x>y:
    print(x,'>',y)
elif x<y:
    print(x,'<',y)
else:
    print(x,'=',y)

mahsulotlar = ["non", "tuz", "sovun", "soda", "kartoshka", "piyoz", "go'sht", "sochiq", "kitob", "ruchka"]
savat = []
bor_mahsulotlar = []
mavjud_emas = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot not in mahsulotlar:
       mavjud_emas.append(mahsulot)
    else:
       bor_mahsulotlar.append(mahsulot)

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q: ")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
foydalanuvchilar = ['admin', 'Ozod', 'Umid', 'Farrux', 'operator']
login = input("Yangi login kiriting: ")
if login in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {login.title()}!")
        
son = int(input('Butun son kiriting: '))
for raqam in range(2,11):
    if not son % raqam:
        print(f"{son} soni {raqam} ga qoldiqsiz bo'linadi")    
    