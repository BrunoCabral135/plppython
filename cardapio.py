hamburguer = 20
batata = 10
refrigerante = 5

qtdhamburguer = int(input('Hambúrguere: '))
qtdbatata = int(input('Batata: '))
qtdrefrigerante = int(input('Refrigerante: '))

subtotal = (hamburguer * qtdhamburguer) + (batata * qtdbatata) + (refrigerante * qtdrefrigerante)

taxa = subtotal * 0.10
total = subtotal + taxa

gorjeta = input('Quer deixar gorjeta? (sim/nao): ') == 'sim'

if gorjeta:
    total = total + 10

pessoas = int(input('Dividir para quantas pessoas? '))

if pessoas > 4:
    total = total * 0.95

print('\n--- CONTA ---')
print(f'Subtotal: R$ {subtotal:.2f}')
print(f'Taxa: R$ {taxa:.2f}')
print(f'Total: R$ {total:.2f}')
print(f'Por pessoa: R$ {total / pessoas:.2f}')

if total > 200:
    print('\nA conta passou de R$ 200!')