from fastapi import APIRouter, HTTPException, FastAPI
from app.utils.data_ingestion import main
from app.middleware.cors import cors_middleware

main()

from app.routers import routes
app = FastAPI()
cors_middleware(app)
app.include_router(routes.router)
