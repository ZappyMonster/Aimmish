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

# Aim speed config
aimSpeed = 0.45
confidence = 0.45

# FOV Circle Size
fovCircleSize = 100

# Y Offset; self explanatory
Y_Offset = 0.35

# What key to press to quit and shutdown the autoaim
close_aimbot_key = "ctrl+alt+u"

# Smarter selection of people
centerOfScreen = True # I think you shouldn't change this

# Hold Aim Keybind
holdAimBind = 0x02 # default is right click which is usually what people use for fortnite

# Hold Trigger Keybind
holdTrigBind = 0x43 # default is the c key
# ^ if you wanna change these binds then go to https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes and find the right value
trigDistance = 30 #distance of pixels enemy needs to be in to get shot. tweak this.
trigAim = True #if trigger is pressed, itll turn on aim too
# close up for box fights, its better to have low confidence. also note shooting through walls. also its kinda dogshit unless u have the aimbot toggled at the same time, then its good

# Screenshot FPS, this also limits the aimbot FPS
limit_fps = 120

# Choose 1 of the 3 below
# 1 - CPU <-- NOT RECOMMENDED
# 2 - AMD
# 3 - NVIDIA
onnxChoice = 2
