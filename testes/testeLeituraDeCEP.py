print('Importando libs')
import pandas as pd
import pycep_correios as pycep
import os.path


# Váriaveis soltas
endereços = []
cidades = []


#A linha a baixo encontra o arquivo na pasta em que ele está, indepente do computador
arquivo = os.path.abspath('').replace('testes', 'Bancos_de_Dados\\CNES_01_04_2020_banco_estab.xlsx')

print('Lendo xlsx')
ceps = pd.read_excel(arquivo, usecols = 'I')  #Só descomentar essa linha caso queira realmente carregar o xlsx na memória, pois demora um tempinho

amostras = ceps.sample(10)
chaves = amostras.CO_CEP.keys()


# O loop a baixo pega os endereços de cada cep e os guarda
for chave in chaves:
    cep = str(amostras.CO_CEP.get(chave))
    while len(cep) < 8:
        cep = '0' + cep
    endereços.append(pycep.get_address_from_cep(cep))


# O loop a baixo pega as cidades de cada endereço e as guarda
for endereço in endereços:
    cidades.append(endereço['cidade'])

print(cidades)
