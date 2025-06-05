try:
    try:
        num1 = float(input("Digite um número : "))
    except ValueError:
        print("Digite um número válido")
    try:
        num2 = float(input("Digite outro número : "))
    except ValueError:
        print("Digite um número válido")

    print("qual operação deseja fazer? : +, -, *, / ?")
    operacao = str(input()).lower().strip()
except:
    print("ERRO NO CODIGO")
if operacao == '+':
    resultado_soma = num1 + num2
    print(resultado_soma)
elif operacao == '-':
    resultado_sub = num1 - num2
    print(resultado_sub)
elif operacao == '*':
    resultado_mult = num1 * num2
    print(resultado_mult)
elif operacao == '/':
    resultado_div = num1 / num2
    print(resultado_div)
else : print("Digite uma operação válida")

        
