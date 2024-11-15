 #(Filtro de Números Pares em uma Lista) Receba uma lista de inteiros e filtre apenas os números pares.
print(f"***FILTRO DE NÚMEROS PARES***")
def filtrar_num_pares(lista):
    return [num for num in lista if num % 2 == 0]

lista = list(map(int, input("Digite uma lista de números inteiros separados por espaço: ").split()))

pares = filtrar_num_pares(lista)

print("Números pares:{pares}")