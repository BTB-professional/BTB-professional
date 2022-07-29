ismlar = ["Ali","Vali","Hasan","Husan","Olim"]
for ism in ismlar:
    print(f"Salom {ism}, bugun choyxonaga borasanmi?")
    print(f"Xayr {ism}, ertagacha.\n")

n=len(ismlar)
print(f"Kod {n} marta takrorlandi")

sonlar = list(range(11,101,2))
print(list(range(11,101,2)))
for son in sonlar:
    print(son**3)

kinolar = []
print('5ta eng sevimli kinoingiz qaysi?')
for n in range(5):
    kinolar.append(input(f"{n+1}-eng sevimli kinoingiz:"))
print(kinolar)

odamlar = []
print("bugun nechta kishi bilan suhbat qildingiz?")
for n in range(3):
    odamlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(odamlar)
