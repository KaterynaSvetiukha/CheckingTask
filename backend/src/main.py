from fastapi import FastAPI
from src.modules.task.router import router as task_router
from src.modules.user.router import router as user_router

app = FastAPI(title='Checking Task API')

app.include_router(task_router, prefix='/api')
app.include_router(user_router, prefix='/api')

@app.get("/")
async def root():
    return {"message": "This api is works"}