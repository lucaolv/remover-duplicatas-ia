def remover_duplicados(arr):
    return list(dict.fromkeys(arr))


# Exemplo de uso:
lista = [1, 2, 2, 3, 4, 4, 5]
nomes = ["Ana", "João", "Ana", "Maria", "João"]
racas = ["Labrador", "Poodle", "Labrador", "Bulldog", "Poodle"]
letras = ["a", "b", "a", "c", "b"]
nulo = []

print(remover_duplicados(lista))   # Saída: [1, 2, 3, 4, 5]
print(remover_duplicados(nomes))   # Saída: ['Ana', 'João', 'Maria']
print(remover_duplicados(racas))   # Saída: ['Labrador', 'Poodle', 'Bulldog']
print(remover_duplicados(letras))  # Saída: ['a', 'b', 'c']
print(remover_duplicados(nulo))    # Saída: []