produto=input("Digite o nome do produto").upper()
if (produto=="MOUSE"):
    preco=10
elif (produto=="TECLADO"):
    preco=20
elif (produto=="MEMORIA"):
    preco=100
else:
    preco=0
    print("Produto não existe")
qtd = int(input("Digite a quantidade"))
total = preco * qtd
if (qtd > 10):
    imposto=total*0.05
else:
    imposto=total*0.1
vf = total + imposto
print(f"Produto => {produto}")
print(f"Preco => {preco}")
print(f"Quatidade => {qtd}")
print(f"Imposto => {imposto}")
print(f"Valor Final => {vf}")

