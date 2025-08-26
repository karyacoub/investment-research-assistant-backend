from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controllers.BusinessInsightsController import BusinessInsightsController
from src.controllers.LLMAgentController import LLMAgentController

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(LLMAgentController().router)
app.include_router(BusinessInsightsController().router)