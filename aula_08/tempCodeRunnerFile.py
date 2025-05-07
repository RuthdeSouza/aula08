produto = {
    'nome': 'Notebook',
    'preco': 3500.00,
    'estoque': 15
}

produto.pop('estoque')
print(produto)

produto['preco'] = 4000

print(f"{produto['nome']}: R$ {produto['preco']}")