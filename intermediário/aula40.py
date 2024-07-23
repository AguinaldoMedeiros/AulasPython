# Exercício
# Aumente os preços dos produtos a seguir em 10%
# Gera novos_produtos por deep copy (cópia profunda)
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 2', 'preco': 10.11},
    {'nome': 'Produto 3', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = copy.deepcopy(produtos)

novos_produtos = [{**produto,'preco': round(produto['preco']*1.10)} for produto in novos_produtos]

# Ordene os produtos por nome descrente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = copy.deepcopy(produtos)

produtos_ordenados_por_nome = sorted(
    produtos_ordenados_por_nome, 
    key=lambda item: item['nome'], 
    reverse=True
)


# Ordene os produtos por preco crescente (do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco = sorted(
    produtos_ordenados_por_preco, 
    key=lambda item: item['preco'], 
    reverse=True
)

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
