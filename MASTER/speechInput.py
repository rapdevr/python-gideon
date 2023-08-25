# import statements for code
import speech_recognition as sr

# setup a recognizer instance
r = sr.Recognizer()

def Processor():
    r = sr.Recognizer()
    try:
        print('listening.')
        with sr.Microphone() as smic:
            # adjusts for environment background noise 
            r.adjust_for_ambient_noise(smic, duration=1)
            # listens to the mic
            audio2 = r.listen(smic)
            # sends audio packet to google servers for transcription
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower() # type: ignore
            print(MyText)
            return MyText
    
    # error handling if request wasn't sent to google properly
    except sr.RequestError as e:
        print("Couldn't request results; {0}".format(e))
        return False
    # error handling if audio packet has unintelligible audio
    except sr.UnknownValueError:
        return False