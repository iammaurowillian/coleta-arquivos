# Script de Coleta de Arquivos de Página Web com Token CSRF
Este é um script Python que permite baixar arquivos de uma página da web. Ele foi projetado para fazer solicitações HTTP utilizando a biblioteca requests e para analisar o HTML da página  com a biblioteca BeautifulSoup.

O código também demonstra como criar pastas, fazer download de arquivos utilizando o token.

## Pré-requisitos
Antes de executar o script, você precisará ter o Python instalado em seu sistema. Você também precisará instalar as seguintes bibliotecas Python:

- `requests`
- `BeautifulSoup`
- `os`

## Resultados
O script acessará a página utilizando o metodo POST e utilizara um código especifico e um token CSRF.Após isso, irá analisar a estrutura HTML e coletar os arquivos da página. 

Por fim, imprimirá mensagens informando se o download de cada arquivo foi bem-sucedido ou se houve falha. Os arquivos baixados serão armazenados na pasta especificada(pasta_arquivo).
