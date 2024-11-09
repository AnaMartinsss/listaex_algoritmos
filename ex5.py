#(Gerador de Tabuada) Receba um número inteiro e exiba a tabuada dele (multiplicações de 1 a 10)
print(f"***GERADOR DE TABUADA!***")
numero = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")