import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def Speak(command):

    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while(1):
    print("listening...")

    try:
        with sr.Microphone() as smic:

            r.adjust_for_ambient_noise(smic, duration=1)

            audio2 = r.listen(smic)

            MyText = r.recognize_google(audio2)
            MyText = MyText.lower() # type: ignore

            print("Heard: ", MyText)
            Speak(MyText)

    except sr.RequestError as e:
        print("Couldn't request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Unknown error occured...")

