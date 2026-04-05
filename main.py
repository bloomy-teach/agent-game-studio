import os
from dotenv import load_dotenv

load_dotenv()

print("🎮 Agent Game Studio - Prototype")
print("================================\n")

game_concept = os.getenv("GAME_CONCEPT", "A simple 2D game")
print(f"Game Concept: {game_concept}\n")

# Placeholder for now
print("✅ Setup complete! Agents coming next...")