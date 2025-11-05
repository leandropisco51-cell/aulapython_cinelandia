''' Desenvolva um código python que leia um 
valor e verifica se é positivo, negativo ou 0 '''
v=float(input("Digite um valor"))
if (v > 0):
    print(f"{v} é um valor positivo")
elif (v < 0):
    print(f"{v} é um valor negativo")
else:
    print(f"{v} é um valor 0")
