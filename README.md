# TDE 3

Membros da equipe que participaram na criação deste TDE:

- Patrickerson dos Santos Veiga

O código estará localizado em um repositório privado no github até que seja realizado a data de entrega. Após isso, estaremos disponibilizando o código em modo público.

## Instruções de instalação

1. Criar a pasta data
2. Realizar o download do [dataset][link_dataset]
3. Extrair os arquivos do .zip
4. Inserir os arquivos na pasta **data**

A hierarquia dos arquivos em data ficará com a seguinte estrutura:

./data
├── brawner-s
├── carson-m
├── cuilla-m
├── derrick-j
├── donoho-l
├── fossum-d
└── giron-d

[link_dataset]:https://drive.google.com/file/d/15vrDNLSYLvS4cvA0GILzeqx7SB4Mn6ud/view?usp=sharing

## Notas técnicas

Ambiente desenvolvimento: Python 3.11.0

### Teste em produção

1. docker build -t app
2. docker run app
