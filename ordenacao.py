palavras = ["Gama", "Matematica", "Vestibular", "IA"]
caracter = "a"

dicio = {}
listaPalavra = []
listaValor = []

# Percorre o array de palavras, conta a quantidade de letras e coloca em um dicionário
for palavra in palavras:
  palavraLower = palavra.lower()
  qntd = palavraLower.count(caracter)
  dicio.update({palavra: qntd})

# Pega as infos do dicionário e coloca em dois arrays
for palavra, valor in dicio.items():
  listaPalavra.append(palavra)
  listaValor.append(valor)

listaValor.sort(reverse=True) # .sort não retorna o valor da lista, ele modifica o valor original
listaPalavraSorted = []

# Compara o valor sorted com os valores do dicionário. Se o valor não existe na listaPalavraSorted, adiciona ao final do array.
# Como o for vai percorrer na ordem decrescente (ou ordem de maior quantidade de letras), então ele adiciona a palavra correspondente ao valor sem repetição de palavra.
for valorSorted in listaValor:
  for palavra, valor in dicio.items():
    if valor == valorSorted and palavra not in listaPalavraSorted:
      listaPalavraSorted.append(palavra)

print (listaPalavraSorted)