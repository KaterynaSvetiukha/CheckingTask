from fastapi import FastAPI
from src.modules.task.router import router as task_router

app = FastAPI(title='Checking Task API')

app.include_router(task_router, prefix='/api')

@app.get("/")
async def root():
    return {"message": "This api is works"}