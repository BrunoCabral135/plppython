def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b


while True:
    print("\n===== CALCULADORA =====")
    print("[1] Somar")
    print("[2] Subtrair")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print("[5] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Até mais!")
        break

    if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = somar(a, b)
        elif opcao == "2":
            resultado = subtrair(a, b)
        elif opcao == "3":
            resultado = multiplicar(a, b)
        else:
            resultado = dividir(a, b)

            if resultado is None:
                print("Erro: Divisão por zero não é permitida")
                continue

        print("Resultado:", resultado)

    else:
        print("Opção inválida!")
