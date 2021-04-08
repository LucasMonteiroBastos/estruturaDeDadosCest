'''1 – Dado o seguinte vetor [1,2,4,16,32,64,-128]
implemente um procedimento que indique
o menor e o maior elemento do vetor.'''


lista = []
maior = 0
menor = 0

for c in range(0,7):
    lista.append(int(input(f'Preencha o vetor: {c}:')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'O Maior valor dentro do vetor é {maior}')
print(f'O Menor valor dentro do vetor é {menor}')