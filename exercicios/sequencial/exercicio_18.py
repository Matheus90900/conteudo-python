tamanho_arquivo = float(input("Informe o tamanho do arquivo (em MB): "))
velocidade_internet = float(input("Informe a velocidade da internet (em Mbps): "))
velocidade_MBps = velocidade_internet / 8
tempo_segundos = tamanho_arquivo / velocidade_MBps
tempo_minutos = tempo_segundos / 60
print("Tempo aproximado de download: ",tempo_minutos,"minutos")