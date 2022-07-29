listed = ['Rossiya', 'AQSH', 'Xitoy', 'Kanada', "O'zbekiston", 'Braziliya', 'Italiya', 'Fransiya']
print(listed)

print(len(listed))

print(sorted(listed))

print(sorted(listed, reverse = True))

print(listed)

listed.reverse()
print(listed)

listed.sort()
print(listed)
listed.sort(reverse = True)
print(listed)

sonlar = list(range(120,1200,2))
print(sonlar)

print(sum(sonlar))

print(max(sonlar) - min(sonlar))

print(len(sonlar))

print(sonlar[:21])
print(sonlar[-20:])
print(sonlar[520:550])

taomlar = ['palov','manti','shashlik',"sho'rva",'chuchvara']
nonushta = taomlar[:]
nonushta.remove('chuchvara')
nonushta.remove("sho'rva")
print(nonushta)
nonushta.append("qahva")
nonushta.append('tuxum')
print(nonushta)
print('taomlar: ', taomlar, ' va ', 'nonushta: ', nonushta)

nonushta =tuple(nonushta)
nonushta[0] = "qaymoq va non"