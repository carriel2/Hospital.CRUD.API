# Hospital CRUD API Backend

Este repositório contém o backend de um sistema hospitalar desenvolvido com **FastAPI** e **PostgreSQL**. A API implementa operações CRUD para gerenciar entidades essenciais do sistema, como **Pacientes**, **Médicos**, **Agendamentos** e **Tratamentos**.

## Índice

- [Visão Geral](#visão-geral)
- [Recursos](#recursos)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação e Configuração](#instalação-e-configuração)
- [Modelos de Dados](#modelos-de-dados)
- [Endpoints da API](#endpoints-da-api)
- [Testes](#testes)
- [Deploy](#deploy)
- [Contribuição](#contribuição)

## Visão Geral

O objetivo deste projeto é fornecer uma API RESTful para um sistema hospitalar, permitindo a criação, leitura, atualização e exclusão (CRUD) de dados relacionados a pacientes, médicos, agendamentos e tratamentos. A API foi construída com FastAPI, aproveitando seus recursos de desempenho e geração automática de documentação (Swagger e Redoc). O banco de dados utilizado é o PostgreSQL, com interação feita por meio do SQLAlchemy (modo assíncrono).

## Recursos

- **Pacientes:** Gerenciamento de pacientes com informações como nome, data de nascimento e gênero.
- **Médicos:** Cadastro de médicos com dados como nome e especialidade.
- **Agendamentos:** Registro de agendamentos, relacionando pacientes e médicos.
- **Tratamentos:** Gerenciamento de tratamentos realizados durante um agendamento.

## Tecnologias Utilizadas

- **Python 3.11+**
- **FastAPI** – Framework web moderno, rápido e assíncrono.
- **PostgreSQL** – Banco de dados relacional robusto.
- **SQLAlchemy (Async)** – ORM para interação com o PostgreSQL de forma assíncrona.
- **Pydantic** – Validação e serialização dos dados.
- **python-decouple** – Gerenciamento de variáveis de ambiente.

## Estrutura do Projeto

Hospital.CRUD.API/
├── app/
│   ├── __init__.py
│   ├── main.py              # Arquivo principal da API, configuração de endpoints e middleware
│   ├── models.py            # Definição dos modelos: Paciente, Medico, Agendamento e Tratamento
│   ├── crud.py              # Funções para operações CRUD com o banco de dados
│   └── database.py          # Configuração do SQLAlchemy, engine assíncrono e sessão
├── .env                     # Variáveis de ambiente (não incluído no controle de versão)
├── requirements.txt         # Lista de dependências do projeto
└── README.md                # Este arquivo

## Instalação e Configuração

### Pré-requisitos

**Python 3.11+**
**PostgreSQL** instalado e configurado (ou use Docker para subir um container)

### Passos para Instalar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/Hospital.CRUD.API.git
cd Hospital.CRUD.API
```

2. **Crie e ative um ambiente virtual**

```bash
python -m venv venv
```

# No Windows:

```bash
venv\Scripts\activate
```

# No Linux/Mac:

```bash
source venv/bin/activate
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**

Crie um arquivo .env na raiz do projeto com a seguinte variável (ajuste conforme suas credenciais):

```bash
PG_URL = postgresql+asyncpg://postgres:1234@127.0.0.1:5432/HospitalBD
```

***Observação: É recomendado usar 127.0.0.1 em vez de localhost para evitar problemas de resolução de nomes no Windows.***

5. **Configure o Banco de Dados**

Certifique-se de que o banco de dados HospitalBD existe. Caso contrário, crie-o utilizando o pgAdminou via linha de comando

```bash
CREATE DATABASE Hospital_BD;
```
## Modelos de Dados

**Paciente**

 - id: Identificador único (Serial)
 - nome: Nome do paciente
 - data_nascimento: Data de nascimento
 - genero: Gênero
 - agendamentos: Relação com os agendamentos

**Medico**

- id: Identificador único
- nome: Nome do médico
- especialidade: Especialidade médica
- agendamentos: Relação com os agendamentos

**Agendamento**

- id: Identificador único (chave primária simples).
- data: Data do agendamento (coluna comum).
- paciente_id: Referência ao paciente (ForeignKey).
- medico_id: Referência ao médico (ForeignKey).
- tratamentos: Relação com tratamentos.

**Tratamento**

- id: Identificador único.
- descricao: Descrição do tratamento.
- agendamento_id: Chave estrangeira para agendamentos.


***Observação: Certifique-se de que as chaves estrangeiras estejam configuradas para referenciar colunas únicas (por isso a alteração na tabela Agendamento para ter chave primária simples).***

## Endpoints da API

Endpoints da API
A API gera automaticamente a documentação via Swagger e Redoc. Após iniciar o servidor, acesse:

Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

Alguns exemplos de endpoints:
- GET /pacientes/ – Lista todos os pacientes.
- GET /pacientes/{id} – Detalhes de um paciente.
- POST /pacientes/ – Criação de um novo paciente.
- PUT /pacientes/{id} – Atualização de um paciente.
- DELETE /pacientes/{id} – Remoção de um paciente.

Endpoints semelhantes existem para médicos, agendamentos e tratamentos.

## Executando a Aplicação

Para rodar a API durante o desenvolvimento, utilize:

```bash
uvicorn app.main:app --reload
```
A opção --reload permite que o servidor reinicie automaticamente ao salvar alterações

## Testes

Utilize ferramentas como Postman ou Insomnia para testar os endpoints.
A documentação interativa (Swagger) também facilita a verificação dos comportamentos esperados.

## Deploy

Para deploy, você pode considerar:

Heroku
DigitalOcean
AWS
Outros provedores de cloud.

Recomenda-se dockerizar a aplicação para facilitar o deploy. Crie um Dockerfile e configure um docker-compose se desejar juntar a API com o PostgreSQL.

# Contribuição

Contribuições são bem-vindas!

Faça um fork do repositório.
Crie uma branch para a nova funcionalidade ou correção.
Envie um Pull Request com suas alterações.