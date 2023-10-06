# Dicionário
meudict = {}

meudict["nome"] = "Lucas"
meudict["idade"] = 28
meudict["sexo"] = "masculino"
print(meudict)

# Dicionários com mais informações
produto = [
    {"nome": "camiseta", "preço": 29.99, "estoque": 100},
    {"nome": "calça", "preço": 59.99, "estoque": 50},
    {"nome": "tênis", "preço": 129.99, "estoque": 25}
]

# Substituir informação
meudict["sexo"] = "feminino"
print(meudict)

# Excluir informação do dicionário
del meudict["sexo"]
print(meudict)

# Contabiliza os valores
print(len(meudict))

# Mostra conteúdo em lista
print(meudict.values())

# Mostra nome das chaves
print(meudict.keys())

# Guardar as chaves dentro de uma variável
for chave in meudict.keys():
    print(chave)

# Guardar os valores dentro de uma variável
for valores in meudict.values():
    print(chave)

# Trabalhando com os valores das variáveis
for valores in meudict.values():
    if valores == 28:
        print("UAU QUE VELHO")

# Devolve os itens em tupla
for var in meudict.items():
    print(var)

# Devolve itens em mais de uma tupla
for minha_chave, meu_valor in meudict.items():
    print(f"a chave e: {minha_chave}, e o valor e: {meu_valor}")

