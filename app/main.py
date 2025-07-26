from fastapi import FastAPI
from app.routes import auth  


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de login/register"}

app.include_router(auth.router)
