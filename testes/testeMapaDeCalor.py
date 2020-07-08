import pandas as pd
from matplotlib import pyplot as plt
import os.path


#A linha a baixo encontra o arquivo na pasta em que ele está, indepente do computador
arquivo = os.path.abspath('').replace('testes', 'Bancos_de_dados\População\\tab1_1.xls')


print('Lendo xls...')
populaçao = pd.read_excel(arquivo)  # Atenção, pode demorar algum tempo para ler tudo



# Função que retorna uma lista com 2 dicionários, um por região e outro por estado
def obterPopulaçoes(populaçao = populaçao):
    'Retorna uma lista com 2 dicionários, um por região e outro por estado'
    'Pode ser chamada sem passar um parâmetro'
    
    # Váriaveis que serão usadas no loop logo a baixo
    pop = {}
    caracteresEspeciais = [' ', '(', ')', '1', '2', '3']
    populaçaoPorRegiao = {}
    populaçaoPorEstado = {}
    regioes = ['Brasil', 'Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste']

    # Loop para ler as populações do Brasil e filtrar/organizar as informações
    for linha in range(0, len(populaçao.index)):

        
        if str(populaçao.loc[linha, 'Unnamed: 4']) == 'nan':  # Verifica se existe a informação inválida 'nan' na chave, caso exista, não adiciona a linha
            continue  # Continue faz o loop pular para a próxima iteração, sem executar o que está abaixo
        else:  # Caso não contenha 'nan', realiza os procedimentos abaixo
            correçao = populaçao.loc[linha, 'Unnamed: 0']  # Pega o nome do estado/região
            for especial in caracteresEspeciais:  # Loop para tirar sujeiras do nome
                correçao = correçao.replace(especial, '')  # Troca a sujeira por ''

            # Depois de limpar a sujeira, adiciona o nome da região/estado a um novo dicionário, com seu valor de população
            pop[correçao] = int(populaçao.loc[linha, 'Unnamed: 4'])

            # Filtra os estados/regiões, adicionando cada um em um respectivo dicionário
            if correçao in regioes:
                populaçaoPorRegiao[correçao] = pop[correçao]
            else:
                if correçao == 'Acre':
                    uf = 'AC'
                elif correçao == 'Alagoas':
                    uf = 'AL'
                elif correçao == 'Amapá':
                    uf = 'AP'
                elif correçao == 'Amazonas':
                    uf = 'AM'
                elif correçao == 'Bahia':
                    uf = 'BA'
                elif correçao == 'Ceará':
                    uf = 'CE'
                elif correçao == 'DistritoFederal':
                    uf = 'DF'
                elif correçao == 'EspíritoSanto':
                    uf = 'ES'
                elif correçao == 'Goiás':
                    uf = 'GO'
                elif correçao == 'Maranhão':
                    uf = 'MA'
                elif correçao == 'MatoGrosso':
                    uf = 'MT'
                elif correçao == 'MatoGrossodoSul':
                    uf = 'MS'
                elif correçao == 'MinasGerais':
                    uf = 'MG'
                elif correçao == 'Paraná':
                    uf = 'PA'
                elif correçao == 'Paraíba':
                    uf = 'PB'
                elif correçao == 'Pará':
                    uf = 'PR'
                elif correçao == 'Pernambuco':
                    uf = 'PE'
                elif correçao == 'Piauí':
                    uf = 'PI'
                elif correçao == 'RioGrandedoNorte':
                    uf = 'RN'
                elif correçao == 'RioGrandedoSul':
                    uf = 'RS'
                elif correçao == 'RiodeJaneiro':
                    uf = 'RJ'
                elif correçao == 'Rondônia':
                    uf = 'RO'
                elif correçao == 'Roraima':
                    uf = 'RR'
                elif correçao == 'SantaCatarina':
                    uf = 'SC'
                elif correçao == 'Sergipe':
                    uf = 'SE'
                elif correçao == 'SãoPaulo':
                    uf = 'SP'
                elif correçao == 'Tocantins':
                    uf = 'TO'
                    
                populaçaoPorEstado[uf] = pop[correçao]

    return [populaçaoPorRegiao, populaçaoPorEstado]



def organizarPorMaiorPop(dicionarioComPop):
    uf = []
    inversao = {v: k for k, v in populaçao[1].items()}
    populaçoes = sorted(inversao)
    for total in populaçoes:
        uf.append(inversao[total])

    return [uf, populaçoes]

populaçao = obterPopulaçoes()
dadosOrganizados = organizarPorMaiorPop(populaçao)
plt.barh(dadosOrganizados[0], dadosOrganizados[1])
plt.show()
