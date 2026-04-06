from __future__ import annotations

import logging
import os
from typing import Any

import requests

logger = logging.getLogger(__name__)


class BaseAgent:
    name: str
    version: str
    ollama_url: str
    model: str

    def __init__(
        self,
        *,
        name: str,
        version: str,
        ollama_url: str | None = None,
        model: str | None = None,
    ) -> None:
        self.name = name
        self.version = version
        self.ollama_url = (ollama_url or os.getenv("OLLAMA_API_URL") or "http://localhost:11434").rstrip("/")
        self.model = model or os.getenv("MODEL_NAME") or "llama3.1"

    def generate(self, prompt: str, *, timeout_s: int = 300) -> str:
        url = f"{self.ollama_url}/api/generate"
        payload: dict[str, Any] = {"model": self.model, "prompt": prompt, "stream": False}

        try:
            resp = requests.post(url, json=payload, timeout=timeout_s)
            resp.raise_for_status()
            data = resp.json()
            return str(data.get("response", "")).strip()
        except requests.RequestException as e:
            logger.error("Ollama request failed url=%s model=%s err=%s", url, self.model, e, exc_info=True)
            raise RuntimeError(f"Ollama request failed: {e}") from e