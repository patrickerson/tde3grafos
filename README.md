# TDE 3

Membros da equipe que participaram na criação deste TDE:

- Patrickerson dos Santos Veiga

O código estará localizado em um repositório privado no github até que seja realizado a data de entrega. Após isso, estaremos disponibilizando o código em modo público.

---

## Instruções de instalação

1. Criar a pasta data
2. Realizar o download do [dataset][link_dataset]
3. Extrair os arquivos do .zip
4. Inserir os arquivos na pasta **data**
5. Executar o comando python3 pip install -r requirements.txt

A hierarquia dos arquivos em data ficará com a seguinte estrutura:


./data<br/>
├── dirty_data<br/>
│   ├── brawner-s<br/>
│   ├── carson-m<br/>
│   ├── cuilla-m<br/>
│   ├── derrick-j<br/>
│   ├── donoho-l<br/>
│   ├── fossum-d<br/>
│   └── giron-d<br/>
└── preprocessing_data<br/>

[link_dataset]:https://drive.google.com/file/d/15vrDNLSYLvS4cvA0GILzeqx7SB4Mn6ud/view?usp=sharing

---

## Notas técnicas

Ambiente desenvolvimento: Python 3.11.0


### Teste em produção

1. docker build -t app
2. docker run app

---

## Padrão para pré processamento
Arquivo: json
```yaml

{
    id: Message-ID(exemplo: <12774027.1075842491487.JavaMail.evans@thyme>),
    date: datetime,
    emailFrom: String,
    fromTo: Lista de string,
}
```
---

## To do:
 - [x] 1) A partir das mensagens de e-mail da base, gere um grafo  direcionado considerando o remetente e o(s) destinatários de cada mensagem. O  grafo deve ser ponderado, considerando a frequência com que um remetente envia  uma mensagem para um destinatário. O grafo também deve ser rotulado,  considerando como rótulo o e-mail de cada usuário.
    - [ ] Dar replace em emails fora do padrão: "trading<.williams@enron.com >"
    - [x] Verifica ocorrências de nós sem saída
 - [ ] 2) Implemente métodos/funções para extrair as seguintes  informações gerais do grafo construído: 
    - [x] a. O número de vértices do grafo; 
    - [x] b. O número de arestas do grafo; 
    - [x] c. Os 20 indivíduos que possuem maior grau de saída e o valor correspondente; 
    - [x] d. Os 20 indivíduos que possuem maior grau de entrada e o valor  correspondente;  Implemente um método/função que encontre qual é o maior caminho mínimo entre qualquer par de vértices do grafo (i.e., diâmetro do grafo), retornando o valor e o caminho encontrado.
    - [ ] e. Se o grafo é Euleriano (true) ou não (false).
 - [x] 3) Implemente um método/função que percorre o grafo em  PROFUNDIDADE e verifica se um indivíduo X pode alcançar um indivíduo Y retornando e mostrando o caminho percorrido (vértices visitados) em uma lista e o  tempo necessário para realizar a operação. 
 - [x] 4) Implemente um método/função que percorre o grafo em  LARGURA e verifica se um indivíduo X pode alcançar um indivíduo Y retornando  e mostrando o caminho percorrido (vértices visitados) em uma lista e o tempo  necessário para realizar a operação. 
 - [x] 5) Implemente um método/função que retorne uma lista com os  vértices que estão a uma distância de D arestas de um nó N. Considere que uma  ligação entre os nós X e Y corresponde a uma distância 1 entre X e Y. 
 - [x] 6) Implemente um método/função que encontre qual é o maior  caminho mínimo entre qualquer par de vértices do grafo (i.e., diâmetro do grafo),  retornando o valor e o caminho encontrado.
    