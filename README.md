
![postman](https://github.com/0x5FE/postmanDeteckLeaks/assets/65371336/b928a65f-5a45-4c57-b991-5fba64a24954)

- A ferramenta utiliza a API Postman para buscar coleções que correspondam a um determinado termo de pesquisa.
  
- Em seguida, a ferramenta analisa cada coleção para encontrar padrões de informações confidenciais, como 
senhas, chaves API, tokens de acesso e segredos.

# Dependências
 - requests
-  json
-  itertools
-  os

# Configuração

- Antes de executar a ferramenta, é necessário configurar uma chave de ***API Postman.*** Defina a variável de ambiente ***POSTMAN_API_KEY*** com sua chave.

# Possíveis Erros e Soluções

- ***Erro de Autenticação:*** Verifique se a variável de ambiente POSTMAN_API_KEY está definida corretamente.

- ***Erro na API Postman:*** Caso receba erros ao acessar a API Postman, verifique a documentação da API para informações atualizadas.

# Uso

- Para usar a ferramenta, execute o seguinte comando:
 
`python leak_scan.py [TERMO DE PESQUISA]`

- Por exemplo, para procurar coleções Postman que contenham o termo "empresa", execute o seguinte comando:
  
`python leak_scan.py empresa`

# Isenção de responsabilidade: 

- Certifique-se de que que você tem a devida autorização antes de utilizar.
  
- o autor deste script não é responsável por qualquer uso indevido, dano ou atividades ilegais causados pelo uso deste script. 

# Contribuição

- Contribuições são bem-vindas, Sinta-se à vontade.
