numero = int(input("Digite o numero? "))
n1 = 0
n2 = 1
n3 = 0

if numero == 1:
   print(n1)

else:
   while n3 < numero:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       n3 += 1
if numero == 0 or numero == 1:
    print('faz parte')
elif numero == n3:
    print('faz parte')
else:
    print('nao faz parte')

print(n3)

