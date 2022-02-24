"""

add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

***diferentes da listas e tuplas, os sets só suportam elementos únicos!

"""

l1 = [1,2,3,4,5,6,7,7,7,7,7,8,9,9,10, "Alan", "tô com sono kct", "Alan"]
print(l1)
print()

l1 = set(l1) #os itens não se repetem
print(l1)
print()

l1 = list(l1)
print(l1[-1]) #acessar o útlimo item da lista
print()
