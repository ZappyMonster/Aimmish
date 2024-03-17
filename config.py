# Portion of screen to be captured (This forms a square/rectangle around the center of screen)
# If you're using a 320x320 model (like the ones included with this AI aimbot) then keep it at 320 and 320, if you're using a different sized model then do that
screenShotHeight = 320 # DO NOT CHANGE UNLESS YOU KNOW WHAT YOURE DOING OR ARE TOLD TO DO SO
screenShotWidth = 320 # DO NOT CHANGE UNLESS YOU KNOW WHAT YOURE DOING OR ARE TOLD TO DO SO

# For use in games that are 3rd person and character model interferes with the autoaim
# It just hides your character from the AI
useMask = True
maskWidth = 80
maskHeight = 200
# These settings are good for people on 1920x1080 but you might have to fuck with it on other resolutions
# It might not even matter tbh

# Automatically hooks to Fortnite if True. But if this is set to True and you don't have Fortnite open, instead of waiting for you to open Fortnite it just crashes
autoSelectGame = True

# Aim Config
aimSpeed = 0.45

# AI Confidence Level; By default, the aimbot will aim if it's at least 45% sure that it's looking at a player.
confidence = 0.45

# FOV Circle Size; Range it'll aim from
fovCircleSize = 100

# Y Offset; self explanatory
Y_Offset = 0.35

# What key to press to quit and shutdown the autoaim
close_aimbot_key = "ctrl+alt+u"
# MUCH faster than pressing the X on it. Trust me.

# Smarter selection of people
centerOfScreen = True # I think you shouldn't change this

# Aimbot Keybind
holdAimBind = "Right Click" # default is right click which is usually what people use for fortnite
# Triggerbot Keybind
holdTrigBind = "C" # default is the c key
# https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes <-- GO THERE TO CHANGE KEYBINDS


# Triggerbot FOV; Range it'll shoot within
trigDistance = 30

# If True, then it'll also aim while you hold down the triggerbot. Good for shotgun fights.
trigAim = True

# Which model do you want to use? Pick 1 for close range, pick 2 for long range.
modelType = 2

# Screenshot FPS, this also limits the aimbot FPS
limit_fps = 120

# Choose 1 of the 3 below
# 1 - CPU <-- NOT RECOMMENDED
# 2 - AMD
# 3 - NVIDIA
onnxChoice = 2
