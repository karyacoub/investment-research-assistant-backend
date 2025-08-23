from fastapi import APIRouter

from src.models.LLMPrompt import LLMPrompt
from src.services.LLMService import LLMService

class LLMController:

    def __init__(self):
        self.router = APIRouter()

        self.router.add_api_route("/chat", self.chat, methods=["POST"])

        self.service = LLMService()

    async def chat(self, prompt: LLMPrompt):
        return self.service.submitPrompt(prompt.prompt)
