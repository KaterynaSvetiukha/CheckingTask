from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.modules.task.router import router as task_router
from src.modules.tag.router import router as tag_router
from src.modules.user.router import router as user_router
from src.modules.dashboard.router import router as dashboard_router
from src.modules.column.router import router as column_router

app = FastAPI(title='Checking Task API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router, prefix='/api')
app.include_router(tag_router, prefix='/api')
app.include_router(user_router, prefix='/api')
app.include_router(dashboard_router, prefix='/api')
app.include_router(column_router, prefix='/api')

@app.get("/")
async def root():
    return {"message": "This api is works"}