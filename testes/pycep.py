import pycep_correios as pycep
print('O CEP não pode ter hífen e nem ponto.')
cep = input('Insira um CEP válido: ')
endereco = endereco = pycep.get_address_from_cep(cep)
##print(endereco['uf'])
##print(endereco['end'])
##print(endereco['bairro'])
##print(endereco['cidade'])
##print(endereco['complemento'])
##print(endereco['complemento2'])
##print(endereco['uf'])
##print(endereco['cep'])
## https://imasters.com.br/back-end/python-consulta-de-cep-com-pycepcorreios
