
def ler_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida! Digite um número válido.")


# Fluxo principal
print("=== CALCULADORA DE DIVISÃO SEGURA ===")

dividendo = ler_numero("Digite o dividendo: ")
divisor = ler_numero("Digite o divisor: ")

try:
    quociente = dividendo / divisor
    print(f"O resultado da divisão é: {quociente}")

except ZeroDivisionError:
    print("Erro: não é possível dividir um número por zero.")