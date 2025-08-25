import json

from fastapi import APIRouter

from src.models.LLMModels import LLMPrompt
from src.services.LLMAgentService import LLMAgentService

class LLMAgentController:

    def __init__(self):
        self.router = APIRouter()

        self.router.add_api_route("/prompt", self.prompt, methods=["POST"])

        self.service = LLMAgentService()

    """
    FastAPI routes are async by default, submitPrompt() must follow that as well
    since we ideally don't want to block other API calls from coming in in a prod
    environment
    """
    async def prompt(self, prompt: LLMPrompt):
        response = await self.service.submit_prompt(prompt)

        try:
            return json.loads(response)
        except json.JSONDecodeError as e:
            return { "raw": response, "parsing_error": e }
