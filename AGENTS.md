# Agent Game Studio - Development Guidelines

This document outlines best practices for developing autonomous game-building agents, based on Dify's production-level standards.

## Architecture Overview

The system follows **Domain-Driven Design (DDD)** and **Clean Architecture** principles:

```
GameWorkflow (Service Layer)
    ↓
    ├─ GameDesignerAgent (Domain)
    ├─ GameProgrammerAgent (Domain)
    └─ QAAgent (Domain)
         ↓
    BaseAgent (Core)
         ↓
    Ollama (External Service)
```

## Code Standards

### Type Safety

- All functions and class attributes must have explicit type annotations
- Use `TypedDict` for structured data (e.g., `GameResult`)
- Avoid `Any` type unless absolutely necessary
- Prefer modern typing (e.g., `str | None` over `Optional[str]`)

Example:
```python
class GameResult(TypedDict):
    timestamp: str
    design: str
    code: str
```

### Documentation

Every class and function must have:

1. **Module docstring**: Purpose, architecture, key invariants
2. **Class docstring**: Responsibility, lifecycle, attributes
3. **Function docstring**: Behavioral contract, args, returns, raises, side effects

Example:
```python
def generate_code(self, game_design: str) -> str:
    """Generate GDScript code from game design document.

    Behavioral contract:
        - Input: game design document
        - Output: production-ready GDScript code
        - Side effects: logs code generation progress

    Args:
        game_design: The game design document.

    Returns:
        GDScript code implementing the game mechanics.
    """
``` 

### Naming Conventions

- Classes: `PascalCase` (e.g., `GameDesignerAgent`)
- Functions/methods: `snake_case` (e.g., `design_game`)
- Constants: `UPPER_CASE` (e.g., `DEFAULT_TIMEOUT`)
- Private: prefix with `_` (e.g., `_persist_results`)

### Class Layout

Declare all attributes at the top of the class:

```python
class GameWorkflow:
    designer: GameDesignerAgent
    programmer: GameProgrammerAgent
    qa_agent: QAAgent
    output_dir: str

    def __init__(self, output_dir: str = "output") -> None:
        self.output_dir = output_dir
        self.designer = GameDesignerAgent()
```

## Logging & Error Handling

### Logging

- Never use `print` for logging
- Use `logger = logging.getLogger(__name__)` at module level
- Include context (agent name, stage, key identifiers)

```python
logger.info(f"{self.name} designing game based on concept: {concept}")
logger.error(f"Failed to call Ollama at {self.ollama_url}: {e}", exc_info=True)
```

### Error Handling

- Define domain-specific exceptions
- Use `raise ... from e` to preserve tracebacks
- Log errors with `exc_info=True` for full stack traces

```python
except requests.exceptions.RequestException as e:
    logger.error(f"Ollama unavailable: {e}", exc_info=True)
    raise RuntimeError(f"Service error: {e}") from e
```

## Agent Development

### Creating a New Agent

1. Extend `BaseAgent`
2. Implement agent-specific methods with clear contracts
3. Add comprehensive docstrings
4. Use type hints throughout
5. Handle errors gracefully

```python
class MyAgent(BaseAgent):
    """Agent for [domain]. [Responsibility]."""

    def my_task(self, input_data: str) -> str:
        """Do something with input.

        Args:
            input_data: The input.

        Returns:
            The result.
        """
        logger.info(f"{self.name} performing task")
        result = self.generate(prompt)
        logger.info(f"{self.name} completed task")
        return result
```

### BaseAgent Interface

All agents have access to:

- `self.generate(prompt: str) -> str`: Call Ollama with a prompt
- `self.name`: Agent name
- `self.model`: LLM model
- `self.ollama_url`: Ollama service URL

## Testing

Follow Arrange-Act-Assert (AAA) pattern:

```python
def test_agent_generation():
    # Arrange
    agent = GameDesignerAgent()
    concept = "A simple puzzle game"

    # Act
    result = agent.design_game(concept)

    # Assert
    assert isinstance(result, str)
    assert len(result) > 0
```

## Workflow Orchestration

The `GameWorkflow` class coordinates agents:

1. Each stage is independent and can fail gracefully
2. Results are structured (typed) for reliability
3. All outputs are persisted to disk with timestamps
4. Errors bubble up to main.py for handling

## File Organization

```
agent-game-studio/
├── agents/
│   ├── __init__.py
│   ├── base.py            # BaseAgent class
│   ├── game_designer.py   # GameDesignerAgent
│   ├── game_programmer.py # GameProgrammerAgent
│   └── qa_agent.py        # QAAgent
├── workflow.py            # GameWorkflow orchestration
├── main.py                # Entry point
├── requirements.txt       # Python dependencies
└── output/                # Generated artifacts
```

## Common Patterns

### Error Recovery

```python
try:
    # Do something
    pass
except SpecificError as e:
    logger.warning(f"Retryable error: {e}")
    # Retry logic
except FatalError as e:
    logger.error(f"Fatal error: {e}", exc_info=True)
    raise
```

### Environment Configuration

```python
self.ollama_url = ollama_url or os.getenv("OLLAMA_API_URL", "http://localhost:11434")
self.model = model or os.getenv("MODEL_NAME", "llama2")
```

### Timestamped Output

```python
timestamp = datetime.now().isoformat()
run_dir = os.path.join(output_dir, timestamp.replace(":", "-").split(".")[0])
os.makedirs(run_dir, exist_ok=True)
```

## Next Steps

1. Add more specialized agents (UI/UX Designer, Sound Designer, etc.)
2. Implement retry logic with exponential backoff
3. Add support for multiple LLM providers (not just Ollama)
4. Create comprehensive test suite
5. Add performance monitoring and profiling
