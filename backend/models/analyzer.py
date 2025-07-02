from abc import ABC, abstractmethod
from models.report import CodeReviewReport
from models.prompt import CompositePrompt
from google import genai
import json

class ICodeAnalyzer(ABC):
    @abstractmethod
    def analyze(self, code) -> CodeReviewReport:
        pass


class GeminiCodeAnalyzer(ICodeAnalyzer):
    def __init__(self, client):
        super().__init__()
        self.client = client

    def analyze(self, code):

        prompt = CompositePrompt()
        prompts = prompt.get_prompt()
        keys = prompt.get_keys()
        structured_prompt = ""

        for key, p in zip(keys, prompts):
            structured_prompt += f"\n\n[{key}]\n{p}"

        content = f"You are an AI Code Reviewer. Analyze the code written in {code.get_language()}:\n\n{code.get_code()}\n"
        full_prompt = content + structured_prompt

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents = full_prompt,
            config={
                "response_mime_type": "application/json",
            },
        )

        result = response.text
        data = json.loads(result)

        return {
            "code_overview":data.get("code_overview", ""),
            "naming_convention_review":data.get("naming_convention_review", ""),
            "time_complexity":data.get("time_complexity", ""),
            "space_complexity":data.get("space_complexity", ""),
            "optimized_code":data.get("optimization", "")
        }