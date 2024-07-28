# Sorting algorithm by character frequency
Esse repositório armazena o código para o desafio proposto do processo seletivo da Gama.
### Descrição do Desafio
Você receberá uma lista de palavras e um caractere específico. Sua tarefa é ordenar a lista
de palavras com base na frequência do caractere fornecido. Implemente um código em
Python que resolva a tarefa de forma otimizada e eficiente.
Requisitos:
- Escrever o código em Python (.py ou .ipynb) que ordene um array de palavras com
base na frequência de um caracter específico.

### Código
Primeiramente, fiz dois inputs que vão receber do usuário a lista de palavras e o caracter a ser contado. Entende-se implicitamente que o usuário irá passar as informações corretamente (por exemplo, apenas 1 caracter e a lista separada de maneira correta).

![image](https://github.com/user-attachments/assets/45c53395-98ec-4e32-bcd7-0610c4a0dfa6)

Depois, um for percorre para cada palavra do array de palavras digitado pelo usuário e utilizando o método `.count()` e passando o caracter que queremos, obtemos a quantidade de caracteres para cada palavra correspondente. Essas informações são então armazenadas em um dicionário.

![image](https://github.com/user-attachments/assets/b2e3b769-fdc3-40c8-a287-aa05fd8fdfbb)

Após isso, pegamos as informações de valores dos dicionários e colocamos em uma lista de valores e então é utilizado o método `.sort()`, que vai pegar os valores e organizar de maneira decrescente.

![image](https://github.com/user-attachments/assets/a3d086fc-b696-4a46-a996-0ac2fd68ff83)

Por último, temos um for que percorre a lista de valores já organizados e um outro for que percorre novamente o dicionário, e dentro temos um if que verifica se o valor do dicionário corresponde ao valor da lista organizada, e caso essa condição seja verdadeira e se a palavra ainda não está na lista de palavras organizadas, então ela é adicionada utilizando `.append()` na `listaPalavra`. Depois de tudo, a lista organizada é printada no terminal.

![image](https://github.com/user-attachments/assets/a182340d-249d-4f3d-8917-dc3d3837518f)
