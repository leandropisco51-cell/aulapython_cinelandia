''' Desenvolva um código python que leia 3 valores
e mostre qual o maior
lógica
a > b and a > c
a é o maior
b > a and b > c
b é maior
senao
c é maior '''
v1=float(input("Digite um valor => "))
v2=float(input("Digite um valor => "))
v3=float(input("Digite um valor => "))
if (v1 > v2 and v1 > v3):
    print(f"{v1} é o maior valor")
elif (v2 > v1 and v2 > v3):
    print(f"{v2} é o maior valor")
else:
    print(f"{v3} é o maior valor")


