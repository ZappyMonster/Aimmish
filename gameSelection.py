import pygetwindow
import time
import bettercam
from typing import Union
from os import system
from config import *

def gameSelection(autoSelectGame) -> (bettercam.BetterCam, int, Union[int, None]):
    # Selecting the correct game window
    if not autoSelectGame:
        try:
            videoGameWindows = pygetwindow.getAllWindows()
            print("=== All Windows ===")
            for index, window in enumerate(videoGameWindows):
                # only output the window if it has a meaningful title
                if window.title != "":
                    print("[{}]: {}".format(index, window.title))
            # have the user select the window they want
            try:
                userInput = int(input(
                    "Please pick the number for Fortnite. If it's not open, go open it and reopen the aim tool: "))
            except ValueError:
                print("You didn't enter a valid number. Please try again.")
                return
            # "save" that window as the chosen window for the rest of the script
            videoGameWindow = videoGameWindows[userInput]
        except Exception as e:
            print("Failed to select game window: {}".format(e))
            return None
    else:
        try:
            videoGameWindows = pygetwindow.getAllWindows()
            videoGameWindow = -1
            for index, window in enumerate(videoGameWindows):
                # only output the window if it has a meaningful title
                if "Fortnite" in window.title:
                    videoGameWindow = videoGameWindows[index]
            if videoGameWindow == -1:
                system("cls")
                print("Fortnite isn't open, please open the tool when it is!")
                time.sleep(5)
                exit()

        except Exception as e:
            print("Auto select failure, going to manual selection now...")
            time.sleep(3)
            autoSelectGame = False
            gameSelection()

    # Activate that Window
    activationRetries = 30
    activationSuccess = False
    while (activationRetries > 0):
        try:
            videoGameWindow.activate()
            activationSuccess = True
            break
        except pygetwindow.PyGetWindowException as we:
            print("Failed to activate on Fortnite: {}".format(str(we)))
            print("Tab into Fortnite, and if it's not open then close, open Fortnite, then try it again.")
        except Exception as e:
            print("Failed to activate game window: {}".format(str(e)))
            print("Oh shit oh fuck something's wrong uh oh sorry idk what happened")
            activationSuccess = False
            activationRetries = 0
            break
        # wait a little bit before the next try
        time.sleep(1)
        activationRetries = activationRetries - 1
    # if we failed to activate the window then we'll be unable to send input to it
    # so just exit the script now
    if activationSuccess == False:
        return None
    print("Successfully activated the game window...")

    # Starting screenshoting engine
    left = ((videoGameWindow.left + videoGameWindow.right) // 2) - (screenShotWidth // 2)
    top = videoGameWindow.top + \
        (videoGameWindow.height - screenShotHeight) // 2
    right, bottom = left + screenShotWidth, top + screenShotHeight

    region: tuple = (left, top, right, bottom)

    # Calculating the center Autoaim box
    cWidth: int = screenShotWidth // 2
    cHeight: int = screenShotHeight // 2

    camera = bettercam.create(region=region, output_color="BGRA")
    if camera is None:
        print("Camera bug, ask Seconb")
        return
    camera.start(target_fps=limit_fps, video_mode=True)

    return camera, cWidth, cHeight, game