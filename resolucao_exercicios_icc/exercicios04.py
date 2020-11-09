anos_fumando = int(input('A quantos anos você fuma? '))

cigarros_dia = int(input('Quantos cigarros por dia? '))

minutos_perdidos_dia = cigarros_dia * 10;

dias_fumando = anos_fumando * 365

total_minutos_perdidos = dias_fumando * minutos_perdidos_dia

anos_perdidos = total_minutos_perdidos / (365 * 24 * 60)

#print('Minutos perdidos por dia:', minutos_perdidos_dia)
#print('Dias fumando:', dias_fumando)
#print('Minutos perdidos:', total_minutos_perdidos )
print('Anos de vida perdidos:', anos_perdidos )