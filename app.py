from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Finance Predictor Running 🚀"}

@app.get("/predict/loan")
def loan():
    return {"loan_approval": random.choice(["Approved", "Rejected"])}
