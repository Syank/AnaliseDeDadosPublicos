print('Importando libs...')
import pandas as pd
import pycep_correios as pycep
import os.path
from matplotlib import pyplot as plt


#A linha a baixo encontra o arquivo na pasta em que ele está, indepente do computador
arquivo = os.path.abspath('').replace('testes', 'Bancos_de_dados\CNES_01_04_2020_banco_estab.xlsx')

print('Lendo xlsx...')
ceps = pd.read_excel(arquivo, usecols = ['CO_CEP'])  # Atenção, pode demorar algum tempo para ler tudo


# A função a baixo recebe um numero de amostras para analisar e retorna um dicionário que contêm as UFs e a quantia de estabelecimentos nela
def coletarAmostraEstabsPorUF(numeroDeAmostras, fonte):
    amostras = fonte.sample(numeroDeAmostras)
    chaves = amostras.CO_CEP.keys()
    ufs = {}
    
    # O loop a baixo pega os endereços de cada cep e os guarda
    for chave in chaves:
        cep = str(amostras.CO_CEP.get(chave))
        while len(cep) < 8:  # CEPs antigos tem menos digitos, esse loop corrige isso atualizando eles para 8 digitos
            cep = '0' + cep
        try:
            ufDoEstabelecimento = pycep.get_address_from_cep(cep)['uf']  # Acessando os dados do CEP e retornado seu estado
        except:
            print(cep)
        # A condicional a seguir avalia se o estado já existe nas ufs, caso não exista, ele adiciona, caso exista, soma mais um estabelecimento no estado
        if ufDoEstabelecimento not in ufs:
            ufs[ufDoEstabelecimento] = 1
        else:
            ufs[ufDoEstabelecimento] += 1

    return ufs


amostragem = coletarAmostraEstabsPorUF(10, ceps)

print(amostragem)
