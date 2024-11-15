#(Ordenação de Lista com Números Negativos e Positivos) Dada uma lista de números inteiros que incluem positivos e negativos, ordene-os de forma que os negativos fiquem
#antes dos positivos, mantendo a ordem original relativa entre eles.
print(f"***ORDENAÇÃO DE LISTA COM NÚMEROS NEGATIVOS E POSITIVOS***")
def ordenar_lista(numeros):
     positivos= sorted([n for n in numeros if n < 0])
     negativos= sorted([n for n in numeros if n >= 0])
     return negativos + positivos
 
numeros = list(map(int, input("Digite números separados por espaço: ").split()))
print("Lista ordenada:" , ordenar_lista(numeros))
