'''2 – Dado o vetor do exemplo anterior implemente o procedimento que
 calcule a soma dos elementos do vetor.'''

soma = 0
cont = 0
for c in range(1,8):
    num = int(input('Prencha o {} vetor: '.format(c)))
    soma = soma + num
    cont = cont + 1
print('A soma dos elementos do vetor são: {}'.format(soma))
