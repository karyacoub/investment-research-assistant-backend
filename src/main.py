from fastapi import FastAPI

from src.controllers.LLMController import LLMController

app = FastAPI()

app.include_router(LLMController().router)