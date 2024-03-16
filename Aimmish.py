import onnxruntime as ort
import numpy as np
from time import sleep
import win32api
import pandas as pd
from utils.general import (non_max_suppression, xyxy2xywh)
import torch
from keyboard import is_pressed, press, release
import os
from math import sqrt
from config import *
from utils.gameSelection import gameSelection
from colorama import Fore, Style

def getMouse():
    try:
        from utils.hidmouse import MouseInstruct, DeviceNotFoundError
        mouse = MouseInstruct.getMouse()
        print("[+] Thermometer connected properly! Now loading thermometer app... ")
        sleep(2)
    except DeviceNotFoundError as e:
        print("[-] Thermometer not connected... see the error below: ")
        print(e)
        sleep(2)
        camera.stop()
        exit()
    return mouse

def banner():
    os.system('cls')
    print(Style.BRIGHT + Fore.CYAN + """ ENABLED! """ + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.YELLOW + "Press " + str(holdAimBind) + " to use the thermometer" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.YELLOW + "Press " + str(holdTrigBind) + " to change the temperature" + Style.RESET_ALL)
    # idk too lazy to do all the banner shit and have it be fancy

def useMouse(xx, yy, inputType, m):
    if inputType == 0 and xx != 0 and yy != 0:
        m.move(xx, yy)
    if inputType == 1:
        m.press()
    if inputType == 2:
        m.release()

def main():
    camera, cWidth, cHeight, game = gameSelection(autoSelectGame)
    os.system('cls')
    m = getMouse()
    banner()

    onnxProvider = ""
    if onnxChoice == 1:
        onnxProvider = "CPUExecutionProvider"
    elif onnxChoice == 2:
        onnxProvider = "DmlExecutionProvider"
    elif onnxChoice == 3:
        import cupy as cp
        onnxProvider = "CUDAExecutionProvider"

    so = ort.SessionOptions()
    so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
    mdir = os.path.dirname(os.path.abspath(__file__))
    if game == "Fortnite":
        opath = os.path.join(mdir, 'models\\fortnite.onnx')
    elif game == "Apex Legends":
        opath = os.path.join(mdir, 'models\\apex.onnx')
    else:
        opath = os.path.join(mdir, 'models\\best.onnx')
    ort_sess = ort.InferenceSession(opath, sess_options=so, providers=[onnxProvider])


    last_mid_coord = None
    while True:
        while win32api.GetKeyState(holdAimBind) < 0 or win32api.GetKeyState(holdTrigBind) < 0:

            npImg = np.array(camera.get_latest_frame())

            if useMask:
                npImg[-maskHeight:, :maskWidth, :] = 0

            if onnxChoice == 3:
                im = torch.from_numpy(npImg).to('cuda')
                if im.shape[2] == 4:
                    im = im[:, :, :3,]

                im = torch.movedim(im, 2, 0)
                im = im.half()
                im /= 255
                if len(im.shape) == 3:
                    im = im[None]
            else:
                im = np.array([npImg])
                if im.shape[3] == 4:
                    im = im[:, :, :, :3]
                im = im / 255
                im = im.astype(np.half) #np.float32 with ow2
                im = np.moveaxis(im, 3, 1)

            if onnxChoice == 3:
                outputs = ort_sess.run(None, {'images': cp.asnumpy(im)})
            else:
                outputs = ort_sess.run(None, {'images': np.array(im)})

            im = torch.from_numpy(outputs[0]).to('cpu')

            pred = non_max_suppression(
                im, confidence, confidence, 0, False, max_det=10)

            targets = []
            for i, det in enumerate(pred):
                s = ""
                gn = torch.tensor(im.shape)[[0, 0, 0, 0]]
                if len(det):
                    for c in det[:, -1].unique():
                        n = (det[:, -1] == c).sum()
                        s += f"{n} {int(c)}, "

                    for *xyxy, conf, cls in reversed(det):
                        targets.append((xyxy2xywh(torch.tensor(xyxy).view(
                            1, 4)) / gn).view(-1).tolist() + [float(conf)])

            targets = pd.DataFrame(
                targets, columns=['current_mid_x', 'current_mid_y', 'width', "height", "confidence"])

            center_screen = [cWidth, cHeight]

            if len(targets) > 0:
                if (centerOfScreen):
                    targets["dist_from_center"] = np.sqrt((targets.current_mid_x - center_screen[0])**2 + (targets.current_mid_y - center_screen[1])**2)
                    targets = targets.sort_values("dist_from_center")
                if last_mid_coord:
                    targets['last_mid_x'] = last_mid_coord[0]
                    targets['last_mid_y'] = last_mid_coord[1]
                    targets['dist'] = np.linalg.norm(
                        targets.iloc[:, [0, 1]].values - targets.iloc[:, [4, 5]], axis=1)
                    targets.sort_values(by="dist", ascending=False)

                xMid = targets.iloc[0].current_mid_x
                yMid = targets.iloc[0].current_mid_y

                box_height = targets.iloc[0].height
                headshot_offset = box_height * Y_Offset

                mouseMove = [xMid - cWidth, (yMid - headshot_offset) - cHeight]
                
                isAimKeyPressed = win32api.GetKeyState(holdAimBind) < 0
                isTrigKeyPressed = win32api.GetKeyState(holdTrigBind) < 0

                dist_from_center = sqrt(mouseMove[0]**2 + mouseMove[1]**2)
                if dist_from_center <= fovCircleSize:
                    if isAimKeyPressed or (isTrigKeyPressed and trigAim):
                        x2 = int(mouseMove[0] * aimSpeed)
                        y2 = int(mouseMove[1] * aimSpeed)
                        useMouse(x2, y2, 0, m)
                    
                    if isTrigKeyPressed and (not trigAim or dist_from_center <= trigDistance):
                        useMouse(0, 0, 1, m)
                        useMouse(0, 0, 2, m)

                    last_mid_coord = [xMid, yMid]

            else:
                last_mid_coord = None

        if is_pressed(close_aimbot_key):
            camera.stop()
            exit()
        sleep(0.03)


if __name__ == "__main__":
    try:
        main()
    except NameError:
        print("[-] Error: Set your game to Windowed Fullscreen instead of Fullscreen...  ")
    except Exception as e:
        print(str(e))
        print("[-] An error occurred, read the log above... ")
