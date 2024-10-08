from fastapi import APIRouter, HTTPException
from app.utils.data_ingestion import main
from app.routers import routes

app = APIRouter()
app.include_router(routes.router)

@app.on_event("startup")
async def startup_event():
    main()