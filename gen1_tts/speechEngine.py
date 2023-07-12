# import necessary modules
from gtts import gTTS
from playsound import playsound


def textToSpeech(string):
    # text that needs to be converted to speech
    textString = string

    # Target language
    language = 'en'

    # passing text and language params into engine
    ttsObj = gTTS(text=textString, lang=language, slow=False)

    # save output to mp3 file
    ttsObj.save("test.mp3")
    # play mp3 file
    playsound('test.mp3')