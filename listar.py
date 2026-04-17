from cadastro import equipamentos

def listar ():
    if len(equipamentos) == 0:
        print("Nenhum equipamento cadastrado.")
        return
    
    else:

     for equipamento in equipamentos:
        print("==================================")
        print(f"Nome: {equipamento['nome']}")
        print(f"Marca: {equipamento['marca']}")
        print(f"Modelo: {equipamento['modelo']}")
        print(f"Número de Série: {equipamento['numero']}")
        print(f"Registro Anvisa: {equipamento['registro']}")
        print(f"Setor: {equipamento['setor']}")
        print(f"Status: {equipamento['status']}")
        print(f"Última Manutenção: {equipamento['ultima_manutencao']}")
        print("==================================")