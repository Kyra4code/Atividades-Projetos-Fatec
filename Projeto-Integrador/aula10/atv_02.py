import os

# Vetores (listas) vazios: os dados são preenchidos pelo menu
nomes = []
situacoes = []   # "efetivo" ou "estagiário"
idades = []

SITUACOES_VALIDAS = {
    "efetivo": "efetivo",
    "estagiario": "estagiário",
    "estagiário": "estagiário",
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione Enter para continuar...")


def ler_inteiro(mensagem, minimo=None):
    """Repete a pergunta até o usuário digitar um inteiro válido."""
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
            continue
        if minimo is not None and valor < minimo:
            print(f"O valor deve ser maior ou igual a {minimo}.")
            continue
        return valor


def controle():
    clear()
    print("O que você gostaria de fazer?\n")

    try:
        response = int(input(
            "1. Adicionar funcionário\n"
            "2. Exibir somente os nomes dos estagiários\n"
            "3. Exibir somente os nomes dos efetivos\n"
            "4. Exibir os funcionários menores de idade\n"
            "5. Sair\n"
            "R: "
        ))
    except ValueError:
        response = None

    return response


def adicionar_funcionario():
    clear()
    print("=== Adicionar funcionário ===\n")

    nome = ""
    while not nome:
        nome = input("Nome: ").strip()

    while True:
        entrada = input("Situação (efetivo/estagiário): ").strip().lower()
        if entrada in SITUACOES_VALIDAS:
            situacao = SITUACOES_VALIDAS[entrada]
            break
        print("Situação inválida. Digite 'efetivo' ou 'estagiário'.")

    idade = ler_inteiro("Idade: ", minimo=0)

    nomes.append(nome)
    situacoes.append(situacao)
    idades.append(idade)

    print(f"\n{nome} foi cadastrado(a) com sucesso!")
    pausar()


def exibir_nomes_por_situacao(situacao):
    clear()
    print(f"=== Nomes dos {situacao}s ===\n")

    encontrados = [n for n, s in zip(nomes, situacoes) if s == situacao]

    if encontrados:
        for nome in encontrados:
            print(f"- {nome}")
    else:
        print(f"Nenhum {situacao} cadastrado.")
    pausar()


def exibir_menores_de_idade():
    clear()
    print("=== Funcionários menores de idade ===\n")

    achou = False
    for nome, situacao, idade in zip(nomes, situacoes, idades):
        if idade < 18:
            print(f"- {nome} ({situacao}, {idade} anos)")
            achou = True

    if not achou:
        print("Nenhum funcionário menor de idade cadastrado.")
    pausar()


def main():
    while True:
        opcao = controle()

        if opcao == 1:
            adicionar_funcionario()
        elif opcao == 2:
            exibir_nomes_por_situacao("estagiário")
        elif opcao == 3:
            exibir_nomes_por_situacao("efetivo")
        elif opcao == 4:
            exibir_menores_de_idade()
        elif opcao == 5:
            print("Encerrando...")
            break
        else:
            print("\nOpção inválida!")
            pausar()

main()