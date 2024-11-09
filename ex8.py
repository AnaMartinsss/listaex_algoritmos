#(Contagem de Números em uma Lista) Dada uma lista de números, exiba quantos números ela contém
print(f"***CONTAGEM DE NÚMEROS EM UMA LISTA!***")
numeros = [int(n) for n in input("Digite os números separados por espaço: ").split()]
quantidade_numeros = len(numeros)
print(f"A lista contém {quantidade_numeros} números.")
