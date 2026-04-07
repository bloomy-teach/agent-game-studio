```gd
# Pixel Pursuit Prototype (Godot 4)

extends Node

var player = preload("res://Player.tscn")
var level_nodes = []
var current_level = 0
var health = 3
var score = 0
var lives = 3
var level_time = 60.0

func _ready():
    # Initialize UI nodes
    var health_ui = $HealthUI
    var score_ui = $ScoreUI
    var lives_ui = $LivesUI
    
    # Connect signals to update UI
    player.connect("health_changed", self, "_on_health_changed")
    player.connect("score_changed", self, "_on_score_changed")
    
    # Create initial level
    create_level(1)

func _process(delta):
    # Update level time
    if current_level < len(level_nodes) and is_instance_valid(level_nodes[current_level]):
        var level_node = level_nodes[current_level]
        level_time -= delta
        
        # Check for win/lose conditions
        if level_time <= 0:
            handle_win_or_lose()
        
func create_level(level_number):
    # Load level layout from resources
    var level_layout = load("res://Levels/Level%d.tscn".format([level_number]))
    
    # Create a new LevelNode and add it to the scene tree
    var level_node = level_layout.instance()
    add_child(level_node)
    
    # Initialize player position
    player.instance().position = Vector2(50, 50)
    level_node.add_child(player.instance())
    
    # Set up entity components for enemies and obstacles
    for enemy in level_layout.get_node("Enemies").get_children():
        var bloopers = []
        for child in enemy.get_children():
            if child.is_class("Bloopers"):
                bloopers.append(child)
            elif child.is_class("Spikers"):
                child.connect("hit_player", self, "_on_spiker_hit")
        
        # Create an entity component for the bloopers
        var bloopers_component = Component.new()
        bloopers_component.set_script(preload("res://BloopersComponent.gd"))
        level_node.add_component(bloopers_component)
    
    # Store the newly created LevelNode in our list of levels
    level_nodes.append(level_node)

func _on_health_changed(amount):
    health += amount

func _on_score_changed(amount):
    score += amount

func handle_win_or_lose():
    if current_level < len(level_nodes) and is_instance_valid(level_nodes[current_level]):
        var level_node = level_nodes[current_level]
        
        # Check for win condition
        var all_pixels_collected = true
        for child in level_node.get_children():
            if not child.is_class("Pixel"):
                all_pixels_collected = false
                break
        
        if all_pixels_collected:
            # Win condition met; proceed to next level
            current_level += 1
            create_level(current_level)
            score += 1000
        else:
            # Lose condition met; reset game state
            lives -= 1
            health = 3
            player.instance().position = Vector2(50, 50)

func _on_spiker_hit():
    health -= 1

# Placeholder for animation and audio assets
class AnimationTree extends Node {
    func play(animation_name):
        # Implement animation playback logic here
        pass
    
    func stop(animation_name):
        # Implement animation stopping logic here
        pass
}

class AudioPlayer extends Node {
    func play_sound(sound_name):
        # Implement sound playing logic here
        pass
}
```

Please note that this code is a minimal implementation to get you started. You'll need to flesh out the game mechanics, add more levels, and implement the missing features (animation, audio) for it to be a fully playable game.

Also, keep in mind that Godot 4 uses GDScript 2.0 syntax by default. If you're not familiar with this version of the script language, make sure to check out the official documentation for more information on its new features and changes from previous versions.

Lastly, as always, remember to add your own assets (images, audio files) to replace the placeholder logic used in this prototype. Happy coding!