# -*- coding: utf-8 -*-
# precisaremos do módulo random para gerar perdas de pacotes aleatóriasimport random
from socket import *
import random   
# Cria um socket UDP
# Note o uso de SOCK_DGRAM para pacotes UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Atribui um endereço IP e um número de porta ao socket
serverSocket.bind(('localhost', 12000))
while True:
# Gera um número aleatório de 0 a 10
    rand = random.randint(0, 10)
# Recebe do cliente o pacote junto com seu endereço de destino
    message, address = serverSocket.recvfrom(1024)
# Escreve a mensagem em letras maiúsculas
    message = message.upper()
    #serverSocket.sendto(message, address)
# Se rand < 4, consideramos que o pacote foi perdido
    if rand < 4: 
        continue
# Caso contrário, o servidor responde
serverSocket.sendto(message, address)