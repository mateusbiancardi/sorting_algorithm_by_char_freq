dicio = {}
listaValor = []

palavras = input("Digite as palavras separadas por vírgula e espaço: ")
caracter = input("Digite o caracter: ")
palavras = palavras.split(', ')

# Percorre o array de palavras, conta a quantidade de letras e coloca em um dicionário
for palavra in palavras:
  palavraLower = palavra.lower()
  qntd = palavraLower.count(caracter)
  dicio.update({palavra: qntd})

# Pega as infos do dicionário e coloca em dois arrays
for _, valor in dicio.items():
  listaValor.append(valor)

listaValor.sort(reverse=True) # .sort não retorna o valor da lista, ele modifica o valor original
listaPalavra = []

# Compara o valor sorted com os valores do dicionário. Se o valor não existe na listaPalavraSorted, adiciona ao final do array.
# Como o for vai percorrer na ordem decrescente (ou ordem de maior quantidade de letras), então ele adiciona a palavra correspondente ao valor sem repetição de palavra.
for valorSorted in listaValor:
  for palavra, valor in dicio.items():
    if valor == valorSorted and palavra not in listaPalavra:
      listaPalavra.append(palavra)

print (listaPalavra)