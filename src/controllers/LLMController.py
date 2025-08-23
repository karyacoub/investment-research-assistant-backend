from fastapi import APIRouter

from src.models.LLMModels import LLMPrompt
from src.services.LLMService import LLMService

class LLMController:

    def __init__(self):
        self.router = APIRouter()

        self.router.add_api_route("/chat", self.chat, methods=["POST"])

        self.service = LLMService()

    """
    FastAPI routes are async by default, submitPrompt() must follow that as well
    since we ideally don't want to block other API calls from coming in in a prod
    environment
    """
    async def chat(self, prompt: LLMPrompt):
        response = await self.service.submit_prompt(prompt)
        return {"answer": response}
