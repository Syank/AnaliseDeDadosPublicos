print('Importando libs...')
import pandas as pd
import pycep_correios as pycep
import os.path
from matplotlib import pyplot as plt


# Váriaveis soltas
enderecos = []
ufs = {}


#A linha a baixo encontra o arquivo na pasta em que ele está, indepente do computador
arquivo = os.path.abspath('').replace('testes', 'Bancos_de_dados\CNES_01_04_2020_banco_estab.xlsx')

print('Lendo xlsx...')
ceps = pd.read_excel(arquivo, usecols = ['CO_CEP'])  # Atenção, pode demorar algum tempo para ler tudo

amostras = ceps.sample(10)
chaves = amostras.CO_CEP.keys()


# O loop a baixo pega os endereços de cada cep e os guarda
for chave in chaves:
    cep = str(amostras.CO_CEP.get(chave))
    while len(cep) < 8:  # CEPs antigos tem menos digitos, esse loop corrige isso atualizando eles para 8 digitos
        cep = '0' + cep
    ufDoEstabelecimento = pycep.get_address_from_cep(cep)['uf']
    if ufDoEstabelecimento not in ufs:
        ufs[ufDoEstabelecimento] = 1
    else:
        ufs[ufDoEstabelecimento] += 1


# O loop a baixo pega as cidades de cada endereço e as guarda


print(ufs)
