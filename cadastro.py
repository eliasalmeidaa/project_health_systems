#cadastro de equipamentos hospitalares
equipamentos = []

def cadastro ():
    nome = input("Qual nome do equipamento: ")
    marca = input("Qual marca do equipamento: ")
    modelo = input("Qual o modelo do equipamento: ")
    numerodeserie = input("Qual numero de serie do equipamento: ")
    registroanvisa = input("Qual Registro Anvisa do equipamento: ")
    setor_hospital = input("Qual setor do hospital: ")
    status_equipamento = input("Qual situação do equipamento: ")
    ultima_manu = input("Qual data da ultima manutenção: ")

    equipamento = {
        "nome": nome,
        "marca": marca,
        "modelo":  modelo,
        "numero": numerodeserie,
        "registro": registroanvisa,
        "setor": setor_hospital,
        "status": status_equipamento,
        "ultima_manutencao": ultima_manu,
    }

    equipamentos.append(equipamento)

    

