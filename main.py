from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()
#Criei esse dicionario, para simular um banco de dados 
jogadores = {
    1: {
        "Nome": "João",
        "idade": 13,
        "Posição": "Atacante"
    },
    2: {
        "Nome": "Fernando",
        "idade": 12,
        "Posição": "Zagueiro"
    },
    3: {
        "Nome": "Victo",
        "idade": 14,
        "Posição": "Goleiro"
    }
}
#Essa parte aqui é o modelo que mostar os dados do dicionario dos joagadores
@app.get("/")
def inicio():
    return jogadores

#Essa parte aqui ele vai está funcionando só quando você coloca o id do jogador
@app.get("/get-jogador/{idjogador}")
def getjogador(idjogador: int):
    if idjogador in jogadores:
        return jogadores[idjogador]

#Essa parte aqui ele vai está buscando a posição do jogador 
@app.get("/get-jogador-posição")
def getJoagadortime(posição: str):
    for idjogador in jogadores:
        if jogadores[idjogador]["Posição"] == posição:
            return jogadores[idjogador]
    return {"Dados": "Não encontrados"}

#Essa parte aqui vai ser usada para está na parte visual para está preechendo
class jogador(BaseModel):
    nome : str
    idade : int
    posição : str

#Essa parte aqui vai ser usada para está na parte visual para está preechendo
class AtualizarJogador(BaseModel):
    nome: str = None
    idade: int = None
    posição: str = None

#Aqui vamos está cadastrando o joagador 
@app.post("/cadastrar-jogador/{idjogador}")
def cadastrarjogador(idjogador: int, jogador: jogador):
    if idjogador in jogadores:
        return {"Erro": "Jogador já existe"}
    jogadores[idjogador] = jogador.dict()
    return jogadores[idjogador]

#Aqui vamos está deletando um joagador 
@app.delete("/excluir-jogador/{idjogador}")
def excluirjogador(idjogador: int):
    if idjogador not in jogadores:
        return {"Erro": "Jogador não existe"}
    del jogadores[idjogador]
    return {"Sucesso": "Jogador excluido"}

#Aqui vamos está atualizando alguma informação jogador 
@app.put("/atualizar-jogador/{idjogador}")
def atualizarjogador(idjogador: int, jogador: AtualizarJogador):
    if idjogador not in jogadores:
        return {"Erro": "Jogador não existe"}
    if jogador.nome is not None:
        jogadores[idjogador]["Nome"] = jogador.nome
    if jogador.idade is not None:
        jogadores[idjogador]["idade"] = jogador.idade
    if jogador.posição is not None:
        jogadores[idjogador]["Posição"] = jogador.posição
    return jogadores[idjogador]

