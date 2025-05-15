# This is the main entry point for the FastAPI backend.
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from .simulation import run_simulation

app = FastAPI()

# Allow frontend on localhost:3000 to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Virtual Physics Lab Backend Running"}


@app.post("/simulate")
def simulate(config: dict):
    result = run_simulation(config)
    return result
