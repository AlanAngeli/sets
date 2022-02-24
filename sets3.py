"""

add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

***diferentes da listas e tuplas, os sets só suportam elementos únicos!

"""

#union os sets (union |)

set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
set3 = set1 | set2

print(set3)
print()

#intersection &

set4 = {1,2,3,4,5,}
set5 = {1,2,3,4,5,6,7,8}
set6 = set4 & set5 #só ficam os item iguais nas duas listas

print(set6)
print()
