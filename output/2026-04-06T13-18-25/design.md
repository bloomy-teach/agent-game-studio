**Game Design Document**
=========================

**Title**
--------

* **Project Name:** Pixel Pioneers
* **Genre:** Endless Runner

**Core Loop**
-------------

The core loop of the game revolves around guiding a pixelated character through increasingly difficult terrain, collecting power-ups and avoiding obstacles while running at high speeds.

### Main Goal:

Collect 100 points to progress to the next level and unlock new characters.

### Core Gameplay Elements:

* **Character Movement:** The player can move left or right using the arrow keys.
* **Power-Ups:** Collect coins to earn bonus points, temporary speed boosts, or shields for increased health.
* **Obstacles:** Avoid enemies (enemies/obstacles), like stationary and moving obstacles that decrease the player's score if hit.

**Player Controls**
-----------------

| Control | Description |
| --- | --- |
| Arrow Keys (Left/Right) | Move character left/right |

**Enemies/Observes**
-------------------

* **Stationary Enemies:** Represented by blocks on the ground, these enemies will reduce points if collided with.
* **Moving Obstacles:**

    * **Small Moving Blocks:** Small moving obstacles that also decrease points upon collision.

### Enemy/Obstacle Patterns:

For simplicity, we'll use a repeating pattern of enemy placements. As players progress to new levels, more and more elements are added.

**Progression**
-------------

* **Leveling System:** Each time the player reaches 100 points, they level up, earning access to new characters.
* **Character Unlocking:** After each level-up, the player is unlocked to select from a growing list of unique characters with their own stats and abilities.

### Progression Mechanics:

| Level | Points Required |
| --- | --- |
| Level 1 | 100 points |
| Level 2 | 200 points |
| Level 3 | 300 points |

**Win/Lose Conditions**
----------------------

* **Game Over:** The player's character dies (runs off-screen or collides with an enemy), reducing their score to zero. The game then resets.
* **Level Complete:** Reaching the end of a level without losing all health.

### Win/Lose Logic:

For simplicity, we'll track lives and reset them when lost.

**Level Structure**
-----------------

To keep things simple for our prototype, we'll start with three levels on each side of the screen. Each subsequent level increases in difficulty by adding new obstacles or decreasing the time to next platform.

### Level Layout:

The game starts at Level 1 and adds two more levels on each side (left and right) as the player progresses through the game.

**UI**
-----

* **Score Display:** Displays current score.
* **Lives Display:** Tracks remaining lives.

### UI Logic:

For simplicity, we'll display only basic information. In future updates, additional UI elements can be added to enhance gameplay experience.

**Audio**
---------

For our prototype, we will use simple background music and sound effects for movement/enemy collision events.

### Audio Implementation:

We will create a playlist for the main menu and in-game loop tracks. Sound effects will be triggered by player movement/enemy collisions.

**Technical Notes (Godot 4)**
---------------------------

* **Game Engine:** Godot 4
* **Target Platforms:** PC, Android, iOS
* **Resolution:** 1920x1080
* **FPS Cap:** 60 FPS

### Project Settings:

Project settings will be set to use the recommended settings for the target platforms.