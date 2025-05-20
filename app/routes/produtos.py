from fastapi import APIRouter

router = APIRouter()

produtos = {
    1: {"item": "corte simples", "preço": 50},
    2: {"item": "barba", "preço": 30},
    3: {"item": "visagismo", "preço": 100},
}

@router.get("/produtos")
def listar_produtos():
    return produtos

@router.get("/produtos/{id_produto}")
def get_produto(id_produto: int):
    return produtos.get(id_produto, {"erro": "Produto não encontrado"})
