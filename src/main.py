from fastapi import FastAPI

from src.controllers.BusinessInsightsController import BusinessInsightsController
from src.controllers.LLMAgentController import LLMAgentController

app = FastAPI()

app.include_router(LLMAgentController().router)
app.include_router(BusinessInsightsController().router)