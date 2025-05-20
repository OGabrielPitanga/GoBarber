from fastapi import FastAPI
from app.routes.produtos import router as produtos_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GoBarber API está no ar!"}

app.include_router(produtos_router)