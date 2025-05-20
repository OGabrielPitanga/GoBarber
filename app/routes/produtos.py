from fastapi import APIRouter
from app.schemas import Produto

router = APIRouter()

produtos = {
    1: {"item": "corte simples", "preço": 50},
    2: {"item": "barba", "preço": 30},
    3: {"item": "visagismo", "preço": 100},
}
next_id = 4

@router.get("/produtos")
def listar_produtos():
    return produtos

@router.get("/produtos/{id_produto}")
def get_produto(id_produto: int):
    return produtos.get(id_produto, {"erro": "Produto não encontrado"})

@router.post("/produtos")
def add_produto(produto: Produto):
    global next_id
    id_atual = next_id
    produtos[id_atual] = produto.dict()
    next_id += 1
    return{
        "id": id_atual,
        "mensagem": "Produto adicionado com sucesso"
    }
