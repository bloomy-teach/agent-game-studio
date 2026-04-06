Here is the code for the game:
```gdscript
extends KinematicBody2D

# Game Variables
var score = 0 setget set_score
var lives = 3 setget set_lives
var level = 1
var character_speed = 300
var coin_speed = 200

# Power-up variables
enum POWERUP {COIN, SPEED_BOOST, SHIELD}
var powerups = []

# Enemy variables
enum ENEMY_TYPE {STATIONARY, MOVING_BLOCK}
var enemy_type = ENEMY_TYPE.STATIONARY
var enemy_spawns = []
var enemy_speeds = []

func _ready():
    # Initialize game settings
    $ScoreDisplay.text = "Score: 0"
    $LivesDisplay.text = "Lives: 3"

    # Initialize level layout
    for i in range(6):
        var x = (i % 2) * 100
        enemy_spawns.append([x, rand_range(-200, 200)])
        if i < 3:
            enemy_speeds.append(character_speed)
        else:
            enemy_speeds.append(rand_range(character_speed - 50, character_speed + 50))

    # Initialize player controls
    Input.connect("mouse_button_left", self, "_on_player_input")

func _process(delta):
    # Update score display
    $ScoreDisplay.text = "Score: %d" % score

    # Check for win/lose conditions
    if lives <= 0:
        game_over()
    elif score >= (level * 100) and level < 10:
        level += 1
        $LivesDisplay.text = "Lives: 3"
        character_speed *= 1.2

func _physics_process(delta):
    # Move player based on input
    var movement = Vector2(0, 0)
    if Input.is_key_pressed(KEY_LEFT):
        movement.x -= 1
    elif Input.is_key_pressed(KEY_RIGHT):
        movement.x += 1
    move_and_slide(movement)

    # Check for collisions with enemies
    for enemy in get_overlapping_areas():
        if enemy.enemy_type == ENEMY_TYPE.STATIONARY:
            score -= 10
            lives -= 1
            $LivesDisplay.text = "Lives: %d" % lives
        elif enemy.enemy_type == ENEMY_TYPE.MOVING_BLOCK:
            score -= 20
            lives -= 1
            $LivesDisplay.text = "Lives: %d" % lives

    # Check for power-up collection
    for powerup in get_overlapping_areas():
        if powerup.is_powerup == true:
            var picked_up_powerup = POWERUP[powerup.powerup_type]
            match picked_up_powerup:
                POWERUP.COIN:
                    score += 10
                POWERUP.SPEED_BOOST:
                    character_speed *= 1.5
                    yield(get_tree().create_timer(2), "timeout")
                    character_speed /= 1.5
                POWERUP.SHIELD:
                    lives += 1

func _on_player_input():
    # Collect coins when player clicks on them
    for coin in get_overlapping_areas():
        if coin.is_coin == true:
            score += 10
            coin.queue_free()

func set_score(value):
    score = value
    $ScoreDisplay.text = "Score: %d" % score

func set_lives(value):
    lives = value
    $LivesDisplay.text = "Lives: %d" % lives

func game_over():
    # Reset level and score when player dies
    level = 1
    score = 0
    character_speed = 300
    lives = 3
```
This script uses the built-in `KinematicBody2D` node for movement and collision detection. It also includes a basic power-up system, enemy spawning, and leveling mechanics.

Note: This is a simplified version of the game design document, focusing on core gameplay elements. Additional features like UI logic, audio implementation, and character customization can be added as separate scripts or extensions to this script.