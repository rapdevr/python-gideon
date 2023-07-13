# import statements for code
import speech_recognition as sr
import pyttsx3
import pygame

# setup a recognizer instance

r = sr.Recognizer()

# function to speak whatever has been heard
def Speak(command):

    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def Processor():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as smic:
            # adjusts for environment background noise 
            r.adjust_for_ambient_noise(smic, duration=1)
            # listens to the mic
            audio2 = r.listen(smic)
            # sends audio packet to google servers for transcription
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower() # type: ignore
            return MyText

    # error handling if request was sent to google properly
    except sr.RequestError as e:
        print("Couldn't request results; {0}".format(e))
        return "Couldn't request results; {0}".format(e)
    # error handling if audio packet has unintelligible audio
    except sr.UnknownValueError:
        print("Unknown error occured...")
        return "Unknown error occured..."

# while loop so computer doesn't stop waiting for keyword
while(1):
    print('active...')
    if "computer" in Processor():
        print('listening...')
        pygame.mixer.init(44100)
        pygame.mixer.music.load("speechRec_gen1\ping.mp3") # type: ignore
        pygame.mixer.music.play()
