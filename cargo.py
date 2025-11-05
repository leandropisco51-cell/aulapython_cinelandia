''' Desenvolv um código python que leia um cargo de 
funcionário, de acordo com o cargo mostre o saláro
vide tabela abaixo.
caixa-1500
vendedor-2400
gerente-4000
de acordo com os salários acima , calcule:
inss = 12% sobre o salário
irrf se o salário for maior que 2000 o irrf será de 14% 
sobre o salário senão será de 8%
salário fina = salario - irrf - inss
'''
cargo=input("Digite um cargo ").upper()
if (cargo=="CAIXA"):
    sal=1500
elif (cargo=="VENDEDOR"):
    sal=2400
elif (cargo=="GERENTE"):
    sal=4000
else:
    sal=0
    print("Cargo não exite")
inss = sal * 0.12
if (sal > 2000):
    irrf = sal * 0.14
else:
    irrf = sal * 0.08
salfinal = sal - irrf - inss
print(f" seu salário é {sal}")
print(f" inss {inss}")
print(f" irrf {irrf}")
print(f" salário final é {salfinal}")
