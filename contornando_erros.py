try:
    nome = input("Digite seu nome :")
    idade = int(input("Digite sua idade : "))
except: 
    print("Acho que voce digitou sua idade errada")
finally : 
    profissao = str(input("Qual sua profissão? ")).upper()
    print(f"Olá senhor(a) {nome}, sua idade é {idade} e sua profissão é {profissao}")
