# Análise de Dados - Sistema de Alunos e Responsáveis

## Descrição
Este projeto realiza análise exploratória de dados de alunos e seus responsáveis, utilizando Python, Pandas e visualizações com Matplotlib/Seaborn.

Projeto da iniciativa de extensão para a Faculdade
### Afins de demonstração academica os dados são de alunos do csv não são reais

## Estrutura do Projeto
```
analise-de-dados/
├── scripts/
│   ├── conexao_postgres.py
│   ├── consultas.py
│   └── exportar_dados.py
├── dados/
│   ├── alunos.csv
│   └── responsavel.csv
└── analise_exploratoria.ipynb
```

## Funcionalidades


### Scripts
- **conexao_postgres.py**: Gerencia conexão com banco PostgreSQL
- **consultas.py**: Contém as queries SQL
- **exportar_dados.py**: Exporta dados do banco para arquivos CSV

### Análise Exploratória
O notebook `analise_exploratoria.ipynb` realiza:
- Análise de distribuição de idades
- Distribuição de graduações
- Relação entre número de alunos e média salarial dos responsáveis
- Visualizações estatísticas

## Requisitos
- Python 3.11+
- pandas
- matplotlib
- seaborn
- psycopg2
- Jupyter Notebook

## Configuração
1. Instale as dependências:
```bash
pip install pandas matplotlib seaborn psycopg2 jupyter
```

2. Configure as credenciais do banco no `conexao_postgres.py`

## Uso
1. Execute o script de exportação:
```bash
python scripts/exportar_dados.py
```

2. Abra o notebook de análise:
```bash
jupyter notebook analise_exploratoria.ipynb
```