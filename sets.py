"""

add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

***diferentes da listas e tuplas, os sets só suportam elementos únicos!

"""

s1 = {1,2,3,4,5} #sets não tem índice!

for v in s1:
    print(v)
print()

#outra maneira de criar set

s2 = set()
s2.add(1)
s2.add(2)
s2.add(3)
s2.add((4,5,6,"Alan")) #tupla
print(s2)
print()

#remover um valor do set

s2.discard((4,5,6,"Alan"))
print(s2)
print()

#Sets ficam fora de ordem
s2.update("Python") #intera letra por letra usando o .update
print(s2)
print()

##Sets não mostram itens duplicados, ex:

s2.update([1,2,3,4,5], {5,6,7,8}) #não aparecerá o valor 5 duas vezes
print(s2)

