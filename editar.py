from cadastro import equipamentos

def editar():
    numero_de_serie = input("Localize a máquina \nDigite o Número de Série: ")

    for equipamento in equipamentos:
        if equipamento["numero"] == numero_de_serie:
            print("Equipamento Encontrado")
            print("==================================")
            print("\nQual campo deseja alterar?")
            print("1 - Nome")
            print("2 - Marca")
            print("3 - Modelo")
            print("4 - Registro Anvisa")
            print("5 - Setor")
            print("6 - Status")
            print("7 - Última Manutenção")
            opcao = int(input("Escolha uma opção: "))
            print("==================================")

            if opcao == 1:
                equipamento["nome"] = input("Nome novo: ")
            elif opcao == 2:
                equipamento["marca"] = input("Marca nova: ")
            elif opcao == 3:
                equipamento["modelo"] = input("Modelo novo: ")
            elif opcao == 4:
                equipamento["registro"] = input("Registro anvisa novo: ")
            elif opcao == 5:
                equipamento["setor"] = input("Setor novo: ")
            elif opcao == 6:
                equipamento["status"] = input("Status novo: ")
            elif opcao == 7:
                equipamento["ultima_manutencao"] = input("Data de manutenção recente: ")
            else:
                print("Opção inválida!")

            print("Equipamento editado com sucesso!!!")
            return

    print("Equipamento não encontrado. Tente novamente...")