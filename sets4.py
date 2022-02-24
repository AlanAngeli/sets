"""

add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

***diferentes da listas e tuplas, os sets só suportam elementos únicos!

"""

#difference -
set1 = {1,2,3,4,5,10,11,12}
set2 = {4,5,6,7,8,9}
set3 = set1 - set2 #vai mostrar apenas a diferença qe tem no set da esquerda, no caso o set1

print(set3)
print()

#symmetric_difference ^
set4 = {1,2,3,4,5,10,11,12}
set5 = {4,5,6,7,8,9}
set6 = set4 ^ set5 #excluiu os items iguais

print(set6)