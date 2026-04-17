from cadastro import cadastro
from listar import listar
from editar import editar
import deletar

while True:
    print("===== Escolha uma das opções: =====")
    print("1- Cadastro Equipamento \n2- Listar \n3- Editar \n4- deletar \n5- Sair ")
    opcao = int(input("Escolha uma das opções: "))
    print("===================================")

    if opcao == 5:
      print("Saindo...\nFinalizado, seus equipamentos foram salvos!")
      break

    elif opcao == 1:
      cadastro()

    elif opcao == 2:
      listar()

    elif opcao == 3:
     editar() 

    elif opcao == 4:
      deletar.deletar()

    else:
        print("Erro, preencha corretamente!")