sp = float(67836.43)
rj = float(36678.66)
mg = float(29229.88)
es = float(27165.48)
outros = float(19849.53)

total = float(sp + rj + mg + es + outros)
print(total)
total2 = total *100
print(total2)

sp = ((sp/total)*100)
rj = ((rj/total)*100)
mg = ((mg/total)*100)
es = ((es/total)*100)
outros = ((outros/total)*100)

print(f'sp: {sp}')
print(f'rj: {rj}')
print(f'mg: {mg}')
print(f'es: {es}')
print(f'outros: {outros}')
