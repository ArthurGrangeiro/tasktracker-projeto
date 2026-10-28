# TaskTracker

Aplicação de linha de comando (CLI) em Python para cadastro e visualização de tarefas, desenvolvida no **Bootcamp II — Fase 2 (Entrega Intermediária)** do curso de Análise e Desenvolvimento de Sistemas (UniCEUB).

## Descrição funcional

O TaskTracker oferece um menu contínuo no terminal com três opções:

1. **Cadastrar nova tarefa** — coleta título, descrição, prioridade e data limite.
2. **Visualizar tarefas cadastradas** — lista todas as tarefas com suas propriedades.
3. **Sair da aplicação** — encerra o programa.

### Regras de negócio

| Campo | Tipo | Regra |
|---|---|---|
| Título | String | Obrigatório. Entradas vazias ou só com espaços são rejeitadas e o prompt se repete. |
| Descrição | String | Texto livre. |
| Prioridade | String | Aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa` (sem diferenciar maiúsculas/minúsculas). Qualquer outro valor gera erro e repete o prompt. |
| Data limite | String | Formato livre, sugerido `DD/MM/AAAA`. |
| Status | String | Definido automaticamente como `Pendente` no cadastro. |

Quando não há tarefas cadastradas, a listagem informa que não existem registros no momento.

## Tecnologias utilizadas

- Python 3 (somente biblioteca padrão, sem dependências externas)
- Git e GitHub para versionamento

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Instalação e execução

Pré-requisito: Python 3.8 ou superior instalado.

```bash
git clone https://github.com/SEU-USUARIO/tasktracker-projeto.git
cd tasktracker-projeto
python src/main.py
```

> No Windows, se `python` não for reconhecido, use `py src/main.py`.

## Próximos passos (Fase 3)

- Empacotamento da aplicação
- Containerização com Docker
- Testes automatizados e deploy

## Autor

Arthur Grangeiro Botelho — Análise e Desenvolvimento de Sistemas, UniCEUB
