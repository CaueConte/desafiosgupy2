import json

file = open('exercicio3dados.json')
data = json.load(file)

tirar_zero = [data2 for data2 in data if data2['valor'] !=0.0]
maior = 0
menor = float("inf")
soma = 0

for i in tirar_zero:
    valor = i['valor']
    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor
    
    soma += valor

media = soma/len(tirar_zero)
maior_que_media = [data2 for data2 in data if data2['valor'] > media]
print('numero de dias que rendeu mais que a media mensal: ')
print(len(maior_que_media))

print(f'menor {menor}')
print(f'maior {maior}')
print(f'media {media}')