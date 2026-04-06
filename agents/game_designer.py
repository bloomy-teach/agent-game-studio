import logging
from typing import TypedDict

from agents.base import BaseAgent

logger = logging.getLogger(__name__)


class DesignResult(TypedDict):
    """Return type for GameDesignerAgent.design_game()."""
    design: str


class GameDesignerAgent(BaseAgent):
    """Agent responsible for producing a game design document from a concept."""

    def __init__(self) -> None:
        super().__init__(name="GameDesigner", version="1.0.0")

    def design_game(self, concept: str) -> DesignResult:
        """Generate a comprehensive Markdown design doc from a high-level concept."""
        logger.info("%s designing game concept=%r", self.name, concept)

        prompt = f"""You are an expert game designer.
Create a clear, practical game design document for:

{concept}

Requirements:
- Output in Markdown with headings and bullet points.
- Include: Title, core loop, player controls, enemies/obstacles, progression,
  win/lose conditions, level structure, UI, audio, and technical notes for Godot 4.
- Keep it implementable for a small prototype (avoid huge scope).
"""
        design = self.generate(prompt)
        return {"design": design}