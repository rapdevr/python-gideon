from subprocess import Popen
import pyautogui
import time

def Open():
    Popen('C:\\Users\\rishi\\AppData\\Roaming\\Spotify\\Spotify.exe')

def Play(text, type):
    Open()
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)
    pyautogui.write(text, interval = 0.1)

    if type == "playlist":
        for key in ['enter', 'tab', 'enter', 'tab', 'tab', 'enter']:
            time.sleep(1)
            pyautogui.press(key)
    elif type == "song":
        for key in ['enter', 'tab', 'enter', 'enter']:
            time.sleep(1)
            pyautogui.press(key)
    pyautogui.hotkey('alt', 'tab')

