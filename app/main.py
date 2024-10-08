from fastapi import APIRouter, HTTPException
from app.utils.data_ingestion import main

main()

from app.routers import routes
app = APIRouter()
app.include_router(routes.router)