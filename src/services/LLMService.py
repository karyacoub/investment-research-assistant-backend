from langchain.chains import LLMChain
from langchain_ollama import ChatOllama

from src.models.LLMModels import LLMPrompt


class LLMService:

    def __init__(self):
        self.model = ChatOllama(model="gemma3:12b", validate_model_on_init=True)

    async def submit_prompt(self, prompt: LLMPrompt):
        try:
            llm_response = await self.model.ainvoke(prompt.prompt)
            return getattr(llm_response, "content", str(llm_response))
        except Exception as e:
            return f"LLM call failed: {str(e)}"
