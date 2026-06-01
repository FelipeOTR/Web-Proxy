# Web Proxy com Controle de Conteúdo em Flask

## Dependências
- As bibliotecas utilizadas no código em Python foram:
  - Flask, request, json e urlparse
  - Para rodar o código, é necessário instalar a biblioteca Flask. As outras já são nativas da linguagem Python.
     └── no terminal: pip install Flask

## Tecnologia escolhida

- A tecnologia escolhida para a implementação do Web Proxy foi o Flask. Foi utilizado o Flask por ser de fácil implementação e por dar conta de todos os requisitos da implementação.
 
## Listas de configuração
- O Web Proxy desenvolvido possui duas listas de configuração, de sites bloqueados (blocked.json) e de palavras filtradas (words.json).

## blocked.json
- Para configurá-la, adicione ou remova os sites da lista dentro do dicionário "bloqueados". É possível bloquear o site por inteiro ou apenas páginas específicas.

## words.json
- Para configurá-la, observe que as palavras estão em formado de dicionário. Adicione a palavra bloqueada, que ficará antes dos dois pontos (:), e adione a palavra que substituirá, depois dos dois pontos.

## Execução
- Para executar o Web Proxy localmente, rode o código em python e utilize a o endereço gerado (http://127.0.0.1:5000).
- Após a execução, coloque o site que desejar acessar depois do enderço com uma barra. ex: http://127.0.0.1:5000/site.com.br

## Uso de IA
- O trabalho não foi desenvolvido com uso de ferramentas de IA.
