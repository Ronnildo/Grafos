# Teoria dos Grafos
- Trabalho prático da disciplina de Teoria dos Grafos.

## Implementações
- grafos carrregar arquivo.json //deve carregar os grafos contidos no arquivo .json
- grafos multigrafos //deve informar quais grafos do arquivo carregado são multigrafos
- grafos pseudografos //deve informar quais grafos do arquivo carregado são pseudografos
- grafos desconexos //deve informar quais grafos do arquivo carregado são desconexos
- grafos completos //deve informar quais grafos do arquivo carregado são completos
- grafos graus id=1 //deve informar quais os graus dos vértices do grafo de id=1
- grafos grau id=1 vertice="A"  //deve informar o grau do vértice=A do grafo id=1 
- grafos alcancaveis partida="A"  //deve informar quais vértices do grafo são alcançáveis a partir do vértice = A
- grafos inalcancaveis partida="A" //deve informar quais vértices do grafo são inalcançáveis a partir do vértice = A
- grafos bfs partida="A" chegada="B" //deve informar o caminho partindo do vértice = A até chegar no vértice=B usando o algoritmo BFS.
- grafos dfs partida="A" chegada="B"
- grafos sair // finaliza a execução da ferramenta
  
## Funções
- As funções de implementação dos grafos estão na pasta functions
- Cada função tem um pasta e arquivo com seu respectivo nome e implementação em um arquivo `.py`
- Na pasta lib no arquivo statement, chama cada função de acordo com a sequência de entrada do usuário
- Na pasta lib tem o arquivo menu que é apenas um print com cada uma das específicação a ser executada.
- O arquivo principal main.py onde fica a parte de chamada para execução e onde ler o arquivo
- Na função que mostra os graus de um grafo tem duas, uma verifica apenas um vértice do grafo passado `degrees_vertices_input.py`
- E a outra verifica o grau de todos os vértices `degrees_vertices.py`
## Execução
- A execução pode ser feita de duas formas
- Primeira diretamente executando o arquivo com python   
 `python3 main.py`
- Segundo adicionando o arquivo ao path de execução com o comando `alias graphs="Diretório onde está o arquivo"`
- Depois basta chamar a execução no terminal com o nome "graphs"
- Obs: Para executar o arquivo que contém os grafos ser lido é necessário está no mesmo diretório da onde está sendo realizada a execução
  
