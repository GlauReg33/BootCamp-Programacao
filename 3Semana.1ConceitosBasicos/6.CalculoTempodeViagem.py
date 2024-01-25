def calcular_tempo_viagem(distancia, velocidade):
    tempo = distancia / velocidade
    horas = int(tempo)
    minutos = int((tempo - horas) * 60)
    return horas, minutos

distancia = float(input("Digite a distância em km: "))

velocidade_aviao = 600  # km/h
tempo_aviao = calcular_tempo_viagem(distancia, velocidade_aviao)

velocidade_carro = 100  # km/h
tempo_carro = calcular_tempo_viagem(distancia, velocidade_carro)

velocidade_onibus = 80  # km/h
tempo_onibus = calcular_tempo_viagem(distancia, velocidade_onibus)

print("Tempo de viagem de avião: {} horas e {} minutos".format(tempo_aviao[0], tempo_aviao[1]))
print("Tempo de viagem de carro: {} horas e {} minutos".format(tempo_carro[0], tempo_carro[1]))
print("Tempo de viagem de ônibus: {} horas e {} minutos".format(tempo_onibus[0], tempo_onibus[1]))