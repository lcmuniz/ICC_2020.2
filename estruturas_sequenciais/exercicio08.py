# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
# Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
# = Salário Liquido : R$

# 1 - Solicitar o valor da hora trabalhada e armazenar na variável valor_hora.
valor_hora = input("Digite o valor da hora trabalhada: ")
valor_hora = float(valor_hora)

# 2 - Solicitar o número de horas trabalhadas e armazenar na variável horas_trabalhadas.
horas_trabalhadas = input("Digite o número de horas trabalhadas: ")
horas_trabalhadas = float(horas_trabalhadas)


# 3 - Calcular o valor do salário bruto e armazenar em salario_bruto 
salario_bruto = valor_hora * horas_trabalhadas

# 4 - Calcular o valor do IR pago e armazenar em imposto_renda 
imposto_renda = (11/100) * salario_bruto

# 5 - Calcular o valor do INSS pago e armazenar em inss 
inss = (8/100) * salario_bruto

# 6 - Calcular o valor pago ao sindicato e armazenar em valor_sindicato 
valor_sindicato = (5/100) * salario_bruto

# 7 - Calcular o valor do salário líquido e armazenar em salario_liquido

descontos = imposto_renda + inss + valor_sindicato

salario_liquido = salario_bruto - descontos

# 8 - Mostrar os valores calculados 
print("-------------------------------")
print("Salário Bruto   : R$", salario_bruto)
print("IR (11%)        : R$", imposto_renda)
print("INSS (8%)       : R$", inss)
print("Sindicato ( 5%) : R$", valor_sindicato)
print("-------------------------------")
print("Salário Liquido : R$", salario_liquido)
print("-------------------------------")


