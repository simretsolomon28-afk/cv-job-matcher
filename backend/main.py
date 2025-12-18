from fastapi import FastAPI
from api.match import router as match_router

app = FastAPI()

app.include_router(match_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "CV Job Matcher API is running"}
