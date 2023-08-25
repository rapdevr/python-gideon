import requests
import pygame
import time
KEY = '3b645b3b0625da4ad957f96c384bf6e5'
# pfdEKIo0P7AgYDGAw20x - theresa key

sound = None

def Speak(text, num):
    global sound  # Declare sound as a global variable to modify it within the function

    if num == 1:
        CHUNK_SIZE = 1024
        url = "https://api.elevenlabs.io/v1/text-to-speech/pfdEKIo0P7AgYDGAw20x/stream"

        headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": KEY
        }

        data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
        }
        Processing()
        response = requests.post(url, json=data, headers=headers, stream=True)

        with open('all/sounds/output.mp3', 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
        mixer = pygame.mixer

        mixer.init(44100)
        output = mixer.Sound('all\sounds\output.mp3') # type: ignore
        channel = output.play()
        while channel.get_busy():
            pygame.time.wait(100)
            return True
    elif num == 0:
        if sound:
            sound.stop()
    else:
        print("expected type identifier value")

def Processing():
    mixer = pygame.mixer

    mixer.init(44100)
    ping = mixer.Sound('all\sounds\working.mp3') # type: ignore
    channel = ping.play()
    while channel.get_busy():
        pygame.time.wait(100)
        return True
