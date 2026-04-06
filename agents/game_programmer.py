import logging
from typing import TypedDict

from agents.base import BaseAgent

logger = logging.getLogger(__name__)


class CodeResult(TypedDict):
    code: str


class GameProgrammerAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(name="GameProgrammer", version="1.0.0")

    def generate_code(self, design: str) -> CodeResult:
        logger.info("%s generating code from design (len=%d)", self.name, len(design))

        prompt = f"""You are an expert Godot 4 developer.
Write a single-file, runnable GDScript 4.0 prototype that implements this game design:

{design}

Rules:
- Output ONLY code (no Markdown).
- Use Godot 4 / GDScript 2.0 syntax.
- Keep it minimal but playable.
- Include _ready() and either _process() or _physics_process().
- Avoid external assets; use simple shapes / placeholder logic where needed.
"""
        code = self.generate(prompt)
        return {"code": code}