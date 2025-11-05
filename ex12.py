''' Desenvolva um código python que verifique
se digitou m ou f, masculino para m e feminino
para f, caso seja difente de um dos dois, diga
indefinido '''
genero = input("Digite seu genero (M ou f) ").upper()
if (genero == "M"):
    print("masculino")
elif (genero=="F"):
    print("feminino")
else:
    print("Indefinido")
