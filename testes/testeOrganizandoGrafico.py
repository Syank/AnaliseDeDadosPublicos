from matplotlib import pyplot as plt

# A função a baixo organiza o dicionario de populações, retornando uma lista com as ufs e populações na ordem crescente
def organizarPorMaiorPop(dicionarioComPop):
    uf = []
    inversao = {v: k for k, v in populaçao[1].items()}  # Inverte as chaves pelos valores
    populaçoes = sorted(inversao)
    for total in populaçoes:
        uf.append(inversao[total])

    return [uf, populaçoes]  # UFs no indice 0 da lista, populações da UF no indice 1, em ordem

populaçao = obterPopulaçoes()
dadosOrganizados = organizarPorMaiorPop(populaçao)
plt.barh(dadosOrganizados[0], dadosOrganizados[1])
plt.show()
