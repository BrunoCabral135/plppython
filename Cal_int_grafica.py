
import tkinter as tk

def dividir():
    try:
        # Captura os valores digitados
        dividendo = float(entrada_dividendo.get())
        divisor = float(entrada_divisor.get())

        # Realiza a divisão
        resultado = dividendo / divisor

        # Exibe o resultado na tela
        label_resultado.config(
            text=f"Resultado: {resultado:.2f}",
            fg="green"
        )

    except ValueError:
        label_resultado.config(
            text="Erro: digite apenas números!",
            fg="red"
        )

    except ZeroDivisionError:
        label_resultado.config(
            text="Erro: não é possível dividir por zero!",
            fg="red"
        )

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora de Divisão")
janela.geometry("350x300")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="Calculadora de Divisão",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=15)

# Campo do dividendo
tk.Label(janela, text="Digite o dividendo:").pack()
entrada_dividendo = tk.Entry(janela)
entrada_dividendo.pack(pady=5)

# Campo do divisor
tk.Label(janela, text="Digite o divisor:").pack()
entrada_divisor = tk.Entry(janela)
entrada_divisor.pack(pady=5)

# Botão para realizar a divisão
botao_dividir = tk.Button(
    janela,
    text="Dividir",
    command=dividir
)
botao_dividir.pack(pady=10)

# Label para mostrar o resultado ou os erros
label_resultado = tk.Label(
    janela,
    text="Digite os valores e clique em Dividir.",
    font=("Arial", 10),
    wraplength=320
)
label_resultado.pack(pady=10)

# Mantém a janela aberta
janela.mainloop()