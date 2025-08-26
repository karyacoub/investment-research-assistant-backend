from pydantic import BaseModel

class LLMPrompt(BaseModel):
    prompt: str
    mock: bool = False

class LLMResponse():
    def __init__(self, content: str, model_name: str):
        self.content = content
        self.model_name = model_name