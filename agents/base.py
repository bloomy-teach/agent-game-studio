


import logging
import os
from typing import TypedDict

try:
    import requests
except ImportError:
    requests = None

class AgentConfig(TypedDict):
    ollama_url: str
    model_name: str

class BaseAgent:
    def __init__(self, config: AgentConfig) -> None:
        """
        Initialize the BaseAgent with configuration.

        Args:
            config (AgentConfig): Configuration containing Ollama URL and model name.
        """
        self.ollama_url = config['ollama_url']
        self.model_name = config['model_name']
        self.logger = logging.getLogger(self.__class__.__name__)

    def generate(self, prompt: str) -> str:
        """
        Generate a response from the Ollama API.

        Args:
            prompt (str): The prompt to send to the API.

        Returns:
            str: The API response.

        Raises:
            RuntimeError: If an error occurs while calling the API.
        """
        try:
            response = requests.post(f"{self.ollama_url}/generate", json={'model': self.model_name, 'prompt': prompt})
            response.raise_for_status()
            return response.json().get('response', '')
        except requests.RequestException as e:
            self.logger.error(f"Error calling Ollama API: {e}")
            raise RuntimeError(f"Failed to generate response: {e}")

    def perform_task(self, task: str) -> None:
        """
        Perform a specified task.

        Args:
            task (str): The task to perform.

        Logs the task performance operation.
        """
        self.logger.info(f"Performing task: {task}")

    def __repr__(self) -> str:
        return f"<BaseAgent(ollama_url='{self.ollama_url}', model_name='{self.model_name}')>"

    def __str__(self) -> str:
        return f"BaseAgent with model '{self.model_name}' at '{self.ollama_url}'"