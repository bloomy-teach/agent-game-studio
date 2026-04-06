import logging
from typing import TypedDict

from agents.base import BaseAgent

logger = logging.getLogger(__name__)


class ReviewResult(TypedDict):
    review: str


class QAAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(name="QAAgent", version="1.0.0")

    def review_design(self, design: str) -> ReviewResult:
        logger.info("%s reviewing design (len=%d)", self.name, len(design))

        prompt = f"""You are a QA reviewer for game design documents.
Review the design below and provide:

- Overall assessment (Good/Fair/Needs work)
- Top 5 risks / missing details
- 5 concrete improvements (actionable)
- A short checklist for implementation

Return in Markdown.

DESIGN:
{design}
"""
        review = self.generate(prompt)
        return {"review": review}

    def review_code(self, code: str) -> ReviewResult:
        logger.info("%s reviewing code (len=%d)", self.name, len(code))

        prompt = f"""You are a senior Godot 4 / GDScript reviewer.
Review the code below and provide:

- Overall assessment
- Critical issues that could break at runtime
- Godot best-practice improvements
- Performance concerns (if any)
- Suggested refactors (with small code snippets if helpful)

Return in Markdown.

CODE:
{code}
"""
        review = self.generate(prompt)
        return {"review": review}