from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cadastro import equipamentos, cadastro
from listar import listar
from editar import editar
from deletar import deletar

app = FastAPI(title="Sistema Hospitalar - Equipamentos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensagem": "API funcionando"}

# Cadastrar (via API)
@app.post("/equipamentos")
def api_cadastrar(equipamento: dict):
    equipamentos.append(equipamento)
    return {"status": "cadastrado", "equipamento": equipamento}

# Listar
@app.get("/equipamentos")
def api_listar():
    return equipamentos

# Editar
@app.put("/equipamentos/{numero}")
def api_editar(numero: str, dados: dict):
    for equipamento in equipamentos:
        if equipamento["numero"] == numero:
            equipamento.update(dados)
            return {"status": "editado", "equipamento": equipamento}
    return {"erro": "Equipamento não encontrado"}

# Deletar
@app.delete("/equipamentos/{numero}")
def api_deletar(numero: str):
    for equipamento in equipamentos:
        if equipamento["numero"] == numero:
            equipamentos.remove(equipamento)
            return {"status": "deletado"}
    return {"erro": "Equipamento não encontrado"}