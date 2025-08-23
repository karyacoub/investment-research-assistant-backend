from fastapi import FastAPI

from src.controllers.BusinessInsightsController import BusinessInsightsController
from src.controllers.LLMController import LLMController

app = FastAPI()

app.include_router(LLMController().router)
app.include_router(BusinessInsightsController().router)