from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Simple FastAPI API", version="1.0.0")

# CORS (permisivo para uso rápido)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
def ping():
    return {"ok": True, "message": "pong"}


@app.post("/echo")
def echo(payload: dict):
    # Devuelve el JSON tal cual
    return {"received": payload}

