from cadastro import equipamentos

def deletar():
  numerodeserie = input("Digite o número de série do equipamento que deseja deletar: ")

  for equipamento in equipamentos:
        if equipamento["numero"] == numerodeserie:
            equipamentos.remove(equipamento)
            print("Equipamento deletado com sucesso!")
            return

  print("Equipamento não encontrado.")
