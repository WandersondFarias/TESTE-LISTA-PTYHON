#Exercício - Unir Listas
 # Crie uma função zipper
  # o trabalho desse função sera unir duas lista na ordem

  # Use todos os valores da menor lista

  # Exemplo

   #'salvador','Ubatuba', 'Belo Horizonte '
   
      #['BA','SP','MG','RJ']
  # Usa a função zip para unir as listas até o comprimento da menor
  
def zipper(list1, list2):
    # Usa a função zip para unir as listas até o comprimento da menor
    return list(zip(list1, list2))

# Exemplo de uso
list1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list2 = ['BA', 'SP', 'MG', 'RJ']

resultado = zipper(list1, list2)
print(resultado)

