import logging
import os
import sys

from dotenv import load_dotenv

from workflow import GameWorkflow

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def display_results(results: dict) -> None:
    logger.info("Displaying results...")
    for key, value in results.items():
        print(f"{key}: {value}")


def main() -> int:
    load_dotenv()

    game_concept = os.getenv("GAME_CONCEPT", "A simple 2D game")

    try:
        logger.info("Starting the game workflow...")
        workflow = GameWorkflow(output_dir="output")

        results = workflow.run(game_concept)

        logger.info("Workflow completed successfully.")
        display_results(results)
        return 0

    except Exception:
        logger.exception("An error occurred")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())