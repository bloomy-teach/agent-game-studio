import logging
import os
from datetime import datetime
from typing import TypedDict

from agents.game_designer import GameDesignerAgent
from agents.game_programmer import GameProgrammerAgent
from agents.qa_agent import QAAgent

logger = logging.getLogger(__name__)


class GameStudioResult(TypedDict):
    """Result structure from the complete game studio workflow."""
    timestamp: str
    concept: str
    design: str
    design_review: str
    code: str
    code_review: str
    output_dir: str


class GameWorkflow:
    """Orchestrates the complete game development workflow.

    This workflow follows Domain-Driven Design principles and coordinates
    three specialized agents to design, code, and review games autonomously.

    Architecture:
        - Service layer: GameWorkflow (this class)
        - Domain layer: GameDesignerAgent, GameProgrammerAgent, QAAgent
        - Core layer: BaseAgent (with Ollama integration)

    Attributes:
        output_dir (str): Directory where artifacts are saved.
        designer (GameDesignerAgent): Agent responsible for game design.
        programmer (GameProgrammerAgent): Agent responsible for code generation.
        qa_agent (QAAgent): Agent responsible for reviews.
    """

    output_dir: str
    designer: GameDesignerAgent
    programmer: GameProgrammerAgent
    qa_agent: QAAgent

    def __init__(self, output_dir: str = "output") -> None:
        """Initialize the GameWorkflow.

        Args:
            output_dir: Directory where generated artifacts will be saved.
        """
        self.output_dir = output_dir
        self.designer = GameDesignerAgent()
        self.programmer = GameProgrammerAgent()
        self.qa_agent = QAAgent()

    def run(self, game_concept: str) -> GameStudioResult:
        """Execute the complete game development workflow.

        This method orchestrates the full pipeline:
        1. GameDesigner creates a design document
        2. GameProgrammer generates GDScript code
        3. QAAgent reviews both design and code
        4. All artifacts are saved to timestamped directory

        Args:
            game_concept: A high-level description of the game concept.

        Returns:
            A GameStudioResult containing all generated artifacts and their locations.

        Raises:
            RuntimeError: If any critical stage fails (Ollama unavailable, etc).
        """
        logger.info(f"Starting game development workflow for: {game_concept}")

        try:
            # Stage 1: Design
            logger.info("Stage 1: Game Design")
            design_result = self.designer.design_game(game_concept)
            design = design_result["design"]

            # Stage 2: Code Generation
            logger.info("Stage 2: Code Generation")
            code_result = self.programmer.generate_code(design)
            code = code_result["code"]

            # Stage 3: Design Review
            logger.info("Stage 3: Design Review")
            design_review_result = self.qa_agent.review_design(design)
            design_review = design_review_result["review"]

            # Stage 4: Code Review
            logger.info("Stage 4: Code Review")
            code_review_result = self.qa_agent.review_code(code)
            code_review = code_review_result["review"]

            # Stage 5: Persist Results
            logger.info("Stage 5: Persisting Results")
            run_dir = self._create_output_dir()
            self._persist_results(
                run_dir,
                game_concept,
                design,
                code,
                design_review,
                code_review,
            )

            logger.info(f"Game development workflow completed. Output: {run_dir}")

            return GameStudioResult(
                timestamp=datetime.now().isoformat(),
                concept=game_concept,
                design=design,
                design_review=design_review,
                code=code,
                code_review=code_review,
                output_dir=run_dir,
            )

        except RuntimeError as e:
            logger.error(
                f"Workflow failed at critical stage: {e}",
                exc_info=True,
            )
            raise

    def _create_output_dir(self) -> str:
        """Create a timestamped output directory for this run.

        Returns:
            Path to the created directory.
        """
        timestamp = datetime.now().isoformat().replace(":", "-").split(".")[0]
        run_dir = os.path.join(self.output_dir, timestamp)
        os.makedirs(run_dir, exist_ok=True)
        logger.debug(f"Created output directory: {run_dir}")
        return run_dir

    def _persist_results(
        self,
        run_dir: str,
        concept: str,
        design: str,
        code: str,
        design_review: str,
        code_review: str,
    ) -> None:
        """Save all workflow artifacts to disk.

        Args:
            run_dir: Directory to save artifacts.
            concept: The original game concept.
            design: Generated game design document.
            code: Generated GDScript code.
            design_review: Design review from QAAgent.
            code_review: Code review from QAAgent.

        Side effects:
            - Creates files in run_dir: concept.txt, design.md, code.gd, design_review.md, code_review.md
        """
        files_to_write = {
            "concept.txt": concept,
            "design.md": design,
            "code.gd": code,
            "design_review.md": design_review,
            "code_review.md": code_review,
        }

        for filename, content in files_to_write.items():
            filepath = os.path.join(run_dir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            logger.debug(f"Persisted artifact: {filepath}")
