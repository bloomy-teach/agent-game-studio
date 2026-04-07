**Game Design Document**
=========================

### Game Title
----------------

**Pixel Pursuit**

A simple, fast-paced platformer where the player controls a small character who must navigate through increasingly challenging levels to rescue as many pixels as possible.

### Core Loop
-------------

* The player controls the character, moving left and right.
* The player collects pixels while avoiding obstacles.
* Time-based progression: the level gets harder and faster over time.
* Players can lose lives if they hit an enemy or fall off the screen. When all lives are lost, the game is over.

### Player Controls
-------------------

* Movement: `A`/`D` keys or left and right arrow keys.
* Jumping: Space bar or up arrow key.
* Pixel collection: No direct control; pixels automatically collect when under them.

### Enemies/Obstacles
----------------------

* **Bloopers**: Slow-moving, round enemies that move randomly. They kill the player on contact.
* **Spikers**: Fast-moving, spiked obstacles that kill the player on touch.
* **Ledges**: Platforms with gaps in between; players must time jumps carefully to cross.

### Progression
--------------

* Each level introduces new enemies and/or faster movement speed for existing ones.
* Levels have a fixed duration (60 seconds). If the player survives, they progress to the next level. Otherwise, the game resets at level 1.

### Win/Lose Conditions
------------------------

* **Win Condition**: The player rescues all pixels in a level before time runs out.
* **Lose Condition**: The player loses all lives by hitting an enemy or falling off-screen.

### Level Structure
-------------------

* Levels are procedurally generated, with increasing difficulty as the player progresses.
* Each level is contained within a single screen, with wrap-around scrolling to create the illusion of larger levels.
* Power-ups and secrets can be hidden throughout levels to provide additional challenges and rewards.

### UI
-----

* **Health**: Displayed at the top left corner of the screen; decreases when the player takes damage.
* **Score**: Displayed at the top right corner of the screen; increases for each pixel collected.
* **Lives**: Number displayed below the health counter.
* **Level**: Level number displayed below the lives counter.

### Audio
--------

* Background music: upbeat, energetic tune that accelerates with level progression.
* Sound effects:
	+ Jumping: a quick "whoosh" sound.
	+ Pixel collection: a gentle "ding" sound.
	+ Enemy collision: a loud "thud" or "bump" sound.

### Technical Notes (Godot 4)
---------------------------

* **Scene structure**: Use a `LevelScene` as the main scene, with each level contained within a separate `LevelNode`.
* **Entity management**: Utilize Godot's built-in entity component system for efficient handling of player, enemies, and obstacles.
* **Collision detection**: Employ BoxCast2D for fast collision detection between entities.
* **Animation**: Use Godot's AnimationTree to create smooth animations for the player character.

### Prototype Scope
-------------------

To keep this a small prototype, focus on implementing:

1. A basic level structure with 5-10 levels.
2. Essential player controls (movement, jumping).
3. Basic enemy behavior (Bloopers and Spikers).
4. Pixel collection mechanics.
5. Health and score tracking.

Avoid implementing complex features like procedural generation or advanced enemy AI for this initial prototype.