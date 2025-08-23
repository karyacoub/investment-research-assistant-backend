from pydantic import BaseModel

class LLMPrompt(BaseModel):
    prompt: str