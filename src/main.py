"""
TaskTracker - Gerenciador de Tarefas em Linha de Comando (CLI)
Bootcamp II - Fase 2 (Entrega Intermediária)

Traduz para Python o algoritmo definido no planejamento lógico da Fase 1
(docs/planejamento_logico.pdf).
"""

# ---------------------------------------------------------------------------
# Constantes de regra de negócio
# ---------------------------------------------------------------------------

# Mapeia cada entrada aceita (em minúsculas) para o valor padronizado gravado.
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}

STATUS_INICIAL = "Pendente"


# ---------------------------------------------------------------------------
# Funções de validação
# ---------------------------------------------------------------------------

def ler_titulo():
    """Solicita o título até que um valor não vazio seja informado."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("[ERRO] O título é obrigatório e não pode ficar vazio. Tente novamente.\n")


def ler_prioridade():
    """Solicita a prioridade até que seja Alta, Média (ou Media) ou Baixa."""
    while True:
        entrada = input("Prioridade (Alta / Média / Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("[ERRO] Prioridade inválida. Digite apenas: Alta, Média (ou Media) ou Baixa.\n")


# ---------------------------------------------------------------------------
# Funcionalidades do menu
# ---------------------------------------------------------------------------

def cadastrar_tarefa(tarefas):
    """Coleta os dados, aplica as validações e adiciona a tarefa à lista."""
    print("\n--- CADASTRAR NOVA TAREFA ---")
    titulo = ler_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = ler_prioridade()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": STATUS_INICIAL,
    }
    tarefas.append(tarefa)
    print(f"\n[OK] Tarefa \"{titulo}\" cadastrada com sucesso! Status: {STATUS_INICIAL}.")


def listar_tarefas(tarefas):
    """Exibe todas as tarefas ou avisa que a lista está vazia."""
    print("\n--- TAREFAS CADASTRADAS ---")
    if not tarefas:
        print("Não existem tarefas cadastradas no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa #{numero}")
        print(f"  Título.......: {tarefa['titulo']}")
        print(f"  Descrição....: {tarefa['descricao'] or '(sem descrição)'}")
        print(f"  Prioridade...: {tarefa['prioridade']}")
        print(f"  Data limite..: {tarefa['data_limite'] or '(não informada)'}")
        print(f"  Status.......: {tarefa['status']}")
    print(f"\nTotal: {len(tarefas)} tarefa(s).")


def exibir_menu():
    print("\n==============================")
    print("         TASKTRACKER")
    print("==============================")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


# ---------------------------------------------------------------------------
# Loop principal
# ---------------------------------------------------------------------------

def main():
    tarefas = []  # Lista de dicionários mantida em memória durante a execução

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
