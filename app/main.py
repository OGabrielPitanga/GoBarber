from fastapi import FastAPI
from routes.produtos import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GoBarber API está no ar!"}

app.include_router(router)