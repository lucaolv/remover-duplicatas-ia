# 🧹 Removendo Duplicatas de uma Lista em Python

Bem-vindo! Aqui você vai aprender de forma simples e prática como remover elementos duplicados de uma lista em Python, mantendo a ordem original dos itens. Ideal para quem está começando ou quer uma solução rápida para esse problema comum!

---

## 🚀 O que essa função faz?

A função `remover_duplicatas` recebe uma lista (de números, letras, palavras, etc.) e devolve uma nova lista, sem repetições e na mesma ordem em que os elementos apareceram pela primeira vez.

---

## 💡 Como funciona?

A lógica é bem simples:

1. **Cria uma lista vazia** para guardar os itens únicos.
2. **Cria um conjunto vazio** para lembrar dos itens já vistos.
3. **Percorre cada elemento** da lista original:
   - Se o elemento ainda não foi visto, ele entra na lista de resultado e é marcado como visto.
   - Se já foi visto, ele é ignorado.
4. **Retorna a lista** só com os elementos únicos!

---

## 📝 Código da função

```python
def remover_duplicatas(array):
    resultado = []
    vistos = set()
    for item in array:
        if item not in vistos:
            resultado.append(item)
            vistos.add(item)
    return resultado


🧪 Exemplos de uso
Veja como é fácil usar a função:

print(remover_duplicatas([1, 2, 2, 3, 4, 4, 5]))
# Saída: [1, 2, 3, 4, 5]

print(remover_duplicatas(["a", "b", "a", "c", "d", "d"]))
# Saída: ['a', 'b', 'c', 'd']

print(remover_duplicatas([1, 1, 1, 1, 1]))
# Saída: [1]

print(remover_duplicatas([]))
# Saída: []

🤔 Dicas
Sempre use print() para ver o resultado na tela!
Funciona com qualquer tipo de elemento que possa ser colocado em um conjunto (números, strings, tuplas, etc).
Não altera a lista original, só devolve uma nova lista sem duplicatas.

📚 Resumo
Com poucas linhas de código, você elimina duplicatas e mantém a ordem dos seus dados. Simples, eficiente e fácil de adaptar para outros projetos!
```
