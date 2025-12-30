from fastapi import FastAPI
from routers.filmovi import router as filmovi_router

app = FastAPI(title="Filmovi API", version="1.0.0")

app.include_router(filmovi_router)
