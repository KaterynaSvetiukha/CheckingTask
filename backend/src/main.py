from fastapi import FastAPI

app = FastAPI(title='Checking Task API')

@app.get("/")
async def root():
    return {"message": "This api is works"}