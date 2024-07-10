# FastAPI do Zero

Esse é o repositório do material sobre FastAPI disponível em: [fastapidozero.dunossauro.com](https://fastapidozero.dunossauro.com), criado por Eduardo Mendes e está gratuito
no [canal do Youtube](https://www.youtube.com/playlist?list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP).

O objetivo desse projeto é ensinar FastAPI para pessoas que queiram ter o seu primeiro contato com o mesmo. A ideia padrão é construir uma aplicação pequena e simples, mas executando todos os passos até o deploy.

As Aulas estão dividas em:

0. [Apresentação do curso](https://fastapidozero.dunossauro.com/)
1. [Configurando o Ambiente de Desenvolvimento](https://fastapidozero.dunossauro.com/01/)
2. [Introdução ao desenvolvimento WEB](https://fastapidozero.dunossauro.com/02/)
3. [Estruturando seu Projeto e Criando Rotas CRUD](https://fastapidozero.dunossauro.com/03/)
4. [Configurando Banco de Dados e Gerenciando Migrações com Alembic](https://fastapidozero.dunossauro.com/04/)
5. [Integrando Banco de Dados a API](https://fastapidozero.dunossauro.com/05/)
6. [Autenticação e Autorização](https://fastapidozero.dunossauro.com/06/)
7. [Refatorando a Estrutura do Projeto](https://fastapidozero.dunossauro.com/07/)
8. [Tornando o sistema de autenticação robusto](https://fastapidozero.dunossauro.com/08/)
9. [Criando Rotas CRUD para Tarefas](https://fastapidozero.dunossauro.com/09/)
10. [Dockerizando a aplicação](https://fastapidozero.dunossauro.com/10/)
11. [Automatizando os testes com integração contínua](https://fastapidozero.dunossauro.com/11/)
12. [Fazendo o deploy no fly.io](https://fastapidozero.dunossauro.com/12/)
13. [Despedida](https://fastapidozero.dunossauro.com/13/)

---

### Caso precise reconstruir o ambiente para as páginas

#### Sobre o ambiente

Todo esse projeto é gerenciado pelo Poetry, a versão usada durante o momento da escrita é `1.8.3`:

```bash
pipx install poetry==1.8.3
```

A versão usada do python é a versão 3.12.4:

```
pyenv local 3.12.4
```

para configurar todo o ambiente basta executar:

```bash
poetry install
```

#### Sobre os comandos

Os comandos para executar funções como deploy, servidor local, geração de slides, etc. Estão todas sendo feitas pelo `taskipy`:

```bash
task --list
lint       # Executa o Ruff para listar os problemas de lint
format     # Executa o Ruff e corrige os problema de lint e formatação do código
run        # Inicia a API via FastApi
pre_test   # Executa a task de lint
test       # Executa o pytest para rodar os testes desenvolvidos
post_test  # Executa o coverage para gerar a cobertura de testes
```

Para executar qualquer comando, basta usar: `task <comando>`
