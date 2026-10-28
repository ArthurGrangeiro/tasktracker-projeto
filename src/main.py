"""
TaskTracker - Gerenciador de Tarefas em Linha de Comando (CLI)
Bootcamp II - Fase 2 (Entrega Intermediária)

Versão inicial: estrutura do menu e loop principal.
As validações de título e prioridade serão adicionadas no próximo commit.
"""

STATUS_INICIAL = "Pendente"


def cadastrar_tarefa(tarefas):
    print("\n--- CADASTRAR NOVA TAREFA ---")
    titulo = input("Título: ").strip()
    descricao = input("Descrição: ").strip()
    prioridade = input("Prioridade (Alta / Média / Baixa): ").strip()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": STATUS_INICIAL,
    }
    tarefas.append(tarefa)
    print(f"\n[OK] Tarefa \"{titulo}\" cadastrada com sucesso!")


def listar_tarefas(tarefas):
    print("\n--- TAREFAS CADASTRADAS ---")
    if not tarefas:
        print("Não existem tarefas cadastradas no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa #{numero}")
        print(f"  Título.......: {tarefa['titulo']}")
        print(f"  Descrição....: {tarefa['descricao']}")
        print(f"  Prioridade...: {tarefa['prioridade']}")
        print(f"  Data limite..: {tarefa['data_limite']}")
        print(f"  Status.......: {tarefa['status']}")


def exibir_menu():
    print("\n==============================")
    print("         TASKTRACKER")
    print("==============================")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


def main():
    tarefas = []

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
