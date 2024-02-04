import os
import keyboard as kb
import pyautogui
import configparser
from time import sleep
from win32gui import GetWindowText, GetForegroundWindow

Enabled = True
ClassMode = 0

Ground = "g"
Edge = "h"
Switch = ","
Toggle = "l"

HeavyWep = "3"
AltWep = "1"
Jump = "space"
AirMove = "x"
Super = "f"

# if config/ini exists

if os.path.isfile("./config.ini"):
    config = configparser.ConfigParser()
    config.read("config.ini")
    Ground = config['BINDS']['ground']
    Edge = config['BINDS']['edge']
    Switch = config['BINDS']['switch']
    Toggle = config['BINDS']['toggle']
    HeavyWep = config['GameBinds']['HeavyWep']
    AltWep = config['GameBinds']['AltWep']
    Jump = config['GameBinds']['Jump']
    AirMove = config['GameBinds']['AirMove']
    Super = config['GameBinds']['Super']
else:
    config = configparser.ConfigParser()
    
    config["BINDS"] = {
        "Ground": Ground,
        "Edge": Edge,
        "Switch": Switch,
        "Toggle": Toggle
    }

    config["GameBinds"] = {
        "HeavyWep": HeavyWep,
        "AltWep": AltWep,
        "Jump": Jump,
        "AirMove": AirMove,
        "Super": Super
    }

    with open('./config.ini', 'w') as configfile:
        config.write(configfile)

    k = input("Press Return to Exit")

    exit()


def HunterEdgeSkate():
    print("Hunter EdgeSkate")
    pyautogui.keyDown(HeavyWep, _pause = False)
    sleep(0.01)
    pyautogui.keyUp(HeavyWep, _pause = False)
    sleep(0.500)
    pyautogui.rightClick(_pause = False)
    sleep(0.050)
    pyautogui.keyDown(Jump, _pause = False)
    sleep(0.01)
    pyautogui.keyUp(Jump, _pause = False)
    sleep(0.050)
    pyautogui.keyDown(AirMove, _pause = False)
    sleep(0.01)
    pyautogui.keyUp(AirMove, _pause = False)
    pyautogui.keyDown("2", _pause = False)
    sleep(0.01)
    pyautogui.keyUp("2", _pause = False)

def WarlockEdgeSkate():
    print("Warlock EdgeSkate")
    pyautogui.keyDown(HeavyWep, _pause = False)
    sleep(0.01)
    pyautogui.keyUp(HeavyWep, _pause = False)
    sleep(0.500)
    pyautogui.rightClick(_pause = False)
    sleep(0.050)
    pyautogui.keyDown(Jump, _pause = False)
    pyautogui.keyDown(Super, _pause = False)
    sleep(0.050)
    pyautogui.keyUp(Super, _pause = False)
    pyautogui.keyUp(Jump, _pause = False)

def HunterGroundSkate():
    print("Hunter GroundSkate")
    pyautogui.keyDown(HeavyWep, _pause = False)
    sleep(0.01)
    pyautogui.keyUp(HeavyWep, _pause = False)
    sleep(0.500)
    pyautogui.keyDown(Jump, _pause = False)
    sleep(0.01)
    pyautogui.keyUp(Jump, _pause = False)
    sleep(0.03)
    pyautogui.leftClick(_pause = False)
    sleep(0.025)
    pyautogui.keyDown(Jump, _pause = False)
    sleep(0.01)
    pyautogui.keyUp(Jump, _pause = False)
    sleep(0.025)
    pyautogui.keyDown(AirMove, _pause = False)
    sleep(0.01)
    pyautogui.keyUp(AirMove, _pause = False)
    sleep(0.300)
    pyautogui.keyDown(AltWep, _pause = False)
    sleep(0.01)
    pyautogui.keyUp(AltWep, _pause = False)


def WarlockGroundSkate():
    print("Warlock GroundSkate")
    pyautogui.keyDown(HeavyWep, _pause = False)
    sleep(0.01)
    pyautogui.keyUp(HeavyWep, _pause = False)
    sleep(0.500)
    pyautogui.keyDown(Jump, _pause = False)
    sleep(0.01)
    pyautogui.keyUp(Jump, _pause = False)
    sleep(0.01)
    pyautogui.leftClick(_pause = False)
    sleep(0.025)
    pyautogui.keyDown(Jump, _pause = False)
    sleep(0.01)
    pyautogui.keyUp(Jump, _pause = False)
    sleep(0.025)
    pyautogui.keyDown(Super, _pause = False)
    sleep(0.010)
    pyautogui.keyUp(Super, _pause = False)

def main():
    global Enabled, ClassMode
    print("Sword Skate Script Running...")
    print("")
    print("Mode: Warlock")
    print("")
    print(Toggle.capitalize() + ": Enable Script")
    print(Ground.capitalize() + ": Ground Skate (Slow)")
    print(Edge.capitalize()   + ": Edge Skate (Fast)")
    print(Switch.capitalize() + ": Class (Mode) Swap")
    print("==============================")
    print("")
    while True:
        ActiveProc = GetWindowText(GetForegroundWindow())
        if kb.is_pressed(Edge) and ActiveProc == 'Destiny 2' and Enabled:
            print("'" + Edge.capitalize() + "' pressed!")
            if ClassMode == 0:
                WarlockEdgeSkate()
            else:
                HunterEdgeSkate()
            sleep(1)
        elif kb.is_pressed(Ground) and ActiveProc == 'Destiny 2' and Enabled:
            print("'" + Ground.capitalize() + "' pressed!")
            if ClassMode == 0:
                WarlockGroundSkate()
            else:
                HunterGroundSkate()
            sleep(1)
        elif kb.is_pressed(Toggle):
            print("'" + Toggle.capitalize() + "' pressed!")
            Enabled = not Enabled
            print("Menu Enabled: " + str(Enabled))
            sleep(1)
        elif kb.is_pressed("n"):
            print(ActiveProc)
            sleep(1)
        elif kb.is_pressed(Switch):
            if ClassMode == 0:
                ClassMode = 1
                print("Mode changed to Hunter")
            else:
                ClassMode = 0
                print("Mode changed to Warlock")
            sleep(1)
        sleep(0.025)

if __name__ == "__main__":
    main()