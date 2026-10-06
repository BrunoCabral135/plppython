# Preços
ingresso = 30.00
pipoca = 20.00
refrigerante = 10.00

# Quantidades
qtd_ingresso = int(input("Quantidade de ingressos: "))
qtd_meia = int(input("Quantidade de meias-entradas: "))
qtd_pipoca = int(input("Quantidade de pipocas: "))
qtd_refri = int(input("Quantidade de refrigerantes: "))

# Cálculos
total_ingresso = qtd_ingresso * ingresso
desconto_meia = qtd_meia * (ingresso / 2)

subtotal = total_ingresso - desconto_meia
subtotal += qtd_pipoca * pipoca
subtotal += qtd_refri * refrigerante

# Promoção do combo
if qtd_pipoca >= 1 and qtd_refri >= 1:
    subtotal -= 5

# Taxa de conveniência
taxa = subtotal * 0.05
total = subtotal + taxa

# Divisão
pessoas = int(input("Entre quantas pessoas será dividido? "))
valor_pessoa = total / pessoas

# Verificação do orçamento
passeio_caro = valor_pessoa > 40

# Recibo
print("\n===== RECIBO =====")
print(f"Ingressos: R$ {total_ingresso:.2f}")
print(f"Desconto meia: R$ {desconto_meia:.2f}")
print(f"Pipocas: R$ {qtd_pipoca * pipoca:.2f}")
print(f"Refrigerantes: R$ {qtd_refri * refrigerante:.2f}")
print(f"Taxa (5%): R$ {taxa:.2f}")
print(f"Total: R$ {total:.2f}")
print(f"Por pessoa: R$ {valor_pessoa:.2f}")
print(f"Passeio saiu caro? {passeio_caro}")