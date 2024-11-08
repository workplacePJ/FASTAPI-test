from fastapi import FastAPI
from api.routers import company
import nest_asyncio
nest_asyncio.apply()

app = FastAPI()
app.include_router(company.router)
