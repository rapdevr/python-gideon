from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import pvporcupine
from pvrecorder import PvRecorder

ACCESS_KEY = '6oaIXs0zF7dKyrOLvEN10umgya4a1LRcJKXLy+CZfIpR0A8jpyLEpg=='
KEYWORD_1 = 'all\wake_words\Gideon_en_windows_v2_2_0.ppn'# type: ignore
KEYWORD_2 = 'all\wake_words\Hey-Gideon_en_windows_v2_2_0.ppn' # type: ignore

def WakeListener():
    porcupine = pvporcupine.create(access_key=ACCESS_KEY, keyword_paths=[KEYWORD_1, KEYWORD_2])
    recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    print('listening for wake word!')
    try:
        recorder.start()

        while True:
            keyword_index = porcupine.process(recorder.read())
            if keyword_index >= 0:
                print('heard wake word.')
                pygame.mixer.init(44100)
                sound = pygame.mixer.Sound('all\ping.mp3') # type: ignore
                sound.play()
                return True
    finally:
        porcupine.delete()
        recorder.delete()