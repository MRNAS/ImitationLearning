# Import Flappy Bird from games library in
# Python Learning Environment (PLE)
from ple.games.flappybird import FlappyBird 
 
# Import PyGame Learning Environment
from ple import PLE 
 
# Create a game instance
game = FlappyBird() 
 
# Pass the game instance to the PLE
p = PLE(game, fps=30, display_screen=True, force_fps=False)
 
# Initialize the environment
p.init()
 
 
actions = p.getActionSet()
print(actions) # 119 to flap wings, or None to do nothing
action_dict = {0: actions[1], 1:actions[0]}
 
reward = 0.0
 
for i in range(10000):
  if p.game_over():
    p.reset_game()
 
  state = p.getScreenRGB()
  action = 1
  reward = p.act(action_dict[action])