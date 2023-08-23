import gtts
import pygame

sound = None  # Define sound at a higher scope

def Speak(text, num):
    global sound  # Declare sound as a global variable to modify it within the function

    if num == 1:
        tts = gtts.gTTS(text)
        tts.save("speech.mp3")
        pygame.mixer.init(44100)
        sound = pygame.mixer.Sound('speech.mp3')
        sound.play()
    elif num == 0:
        if sound:
            sound.stop()
    else:
        print("expected type identifier value")