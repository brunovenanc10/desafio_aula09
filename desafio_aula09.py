numero = int(input('Digite um número:'))
nome_arquivo = 'arquivo.txt'

with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    for m in range (1, 11):
        resultado = numero * m
        arquivo.write(f'{numero} x {m} = {resultado}\n')

print('--- Programa Finalizado! ---')




