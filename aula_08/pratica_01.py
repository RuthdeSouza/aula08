# Crie uma tupla com 5 estados brasileiros e imprima todos em uma única linha separados por vírgula

estados = ('Minas Gerais', 'Bahia', 'São Paulo', 'Acre', 'Amazonas')

print(estados)

# Dada a tupla:
# Imprima apenas nomes e cargos:
dados = ('João', 'Analista', 4000.00,'Pedro', 'Vendedor', 2500.00)
print(dados[0], dados[1])
print(dados[3], dados[4])

# Prática 2:
# Crie um dicionário de nome produto representando com as seguintes informações:

produto = {
    'nome': 'Notebook',
    'preco': 3500.00,
    'estoque': 15
}

produto.pop('estoque')
print(produto)

produto['preco'] = 4000

print(f"{produto['nome']}: R$ {produto['preco']}")






