from abc import ABC, abstractmethod
from typing import List

class Prompt(ABC):
    def __init__(self, prompt: str, key: str):
        self._prompt = prompt
        self._key = key

    @abstractmethod
    def get_prompt(self) -> str:
        pass

    @abstractmethod
    def get_key(self) -> str:
        pass


class CodeOverviewPrompt(Prompt):
    def __init__(self):
        super().__init__(
            "Give a short overview of the program.",
            "code_overview"
        )

    def get_prompt(self):
        return self._prompt

    def get_key(self):
        return self._key


class NamingConventionPrompt(Prompt):
    def __init__(self):
        super().__init__(
            "Check whether naming conventions and good variable/method names are followed. For refering a suggestion for any name return in key value pair with key havinig that variabale",
            "naming_convention_review"
        )

    def get_prompt(self):
        return self._prompt

    def get_key(self):
        return self._key


class TimeComplexityPrompt(Prompt):
    def __init__(self):
        super().__init__(
            "Analyze the time complexity of the given code. give Time Complexity first then give short explanation in nested json object",
            "time_complexity"
        )

    def get_prompt(self):
        return self._prompt

    def get_key(self):
        return self._key


class SpaceComplexityPrompt(Prompt):
    def __init__(self):
        super().__init__(
            "Analyze the space complexity of the given code. give Space Complexity first then give short explanation in nested json object",
            "space_complexity"
        )

    def get_prompt(self):
        return self._prompt

    def get_key(self):
        return self._key


class OptimizationPrompt(Prompt):
    def __init__(self):
        super().__init__(
            (
                "If the given code is already optimized, respond with:\n\n"
                '{ "optimization": "Well Done! Buddy for writing Optimized Code" }\n\n'
                "Otherwise, respond with:\n\n"
                '{ "optimization": "Your code can be optimized by ... (explanation), '
                'Expected Time Complexity: O(...), Expected Space Complexity: O(...)" }\n\n'
                "Respond ONLY in valid JSON format."
            ),
            "optimization"
        )

    def get_prompt(self):
        return self._prompt

    def get_key(self):
        return self._key


class CompositePrompt:
    def __init__(self):
        self.prompts: List[Prompt] = [
            CodeOverviewPrompt(),
            NamingConventionPrompt(),
            TimeComplexityPrompt(),
            SpaceComplexityPrompt(),
            OptimizationPrompt()
        ]

    def get_prompt(self) -> List[str]:
        return [prompt.get_prompt() for prompt in self.prompts]

    def get_keys(self) -> List[str]:
        return [prompt.get_key() for prompt in self.prompts]

    def add_prompt(self, prompt: Prompt):
        self.prompts.append(prompt)
