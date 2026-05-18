from fastapi import FastAPI

app = FastAPI(title="Multi-Tenant SaaS Backend")

@app.get("/")
def root():
    return {"message": "SaaS backend scaffold"}
