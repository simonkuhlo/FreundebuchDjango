from fastapi.staticfiles import StaticFiles
import settings
from fastapi import FastAPI
from routes import main_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.app_title, summary=settings.app_summary, description=settings.app_description, version=settings.app_version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.app_origins,        # Allowed origins
    allow_credentials=True,       # Allow cookies and authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)
app.include_router(main_router)
if settings.enable_frontend:
    import frontend as frontend
    app.include_router(frontend.router)
    app.mount("/static", StaticFiles(directory="./frontend/static/"), name="static")
