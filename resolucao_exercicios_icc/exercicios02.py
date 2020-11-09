numero_dias = int(input('Quantos dias vocẽ ficou com o carro? '))

km_percorridos = float(input('Quantos quilômetros você percorreu? '))

valor_dia = 60

valor_km = 0.15

total_dias = numero_dias * valor_dia

total_km = km_percorridos * valor_km

valor_a_pagar = total_dias + total_km

print('Valor a pagar:', valor_a_pagar)

