aluno = {
    'Nome': 'Maria',
    'Idade': 29,
    'Curso': 'Análise de Dados'
}


print(aluno)
print(aluno['Curso'])

aluno['Nome'] = 'Pedro'
print(aluno)
aluno['E-mail'] = 'pedro@gmail.com'
print(aluno)

if 'E-mail' in aluno:
    aluno.pop('E-mail')
print(aluno)

# aluno.clear
# print(aluno) - limpa sem apagar da memória 

# del aluno
# print(aluno) - limpa e apaga da memória 

for chave, valor in aluno.items():
    print(chave)