import sys
import threading

import speech_recognition
import time

class Listener:

    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()

        threading.Thread(target=self.listener).start()

    def listener(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic,duration=2)
                    audio = self.recognizer.listen(mic)

                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()

                    if "test" in text:
                        print("listening...")
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()
                        if text == "terminate program":
                            print("exiting...")
                            sys.exit()
                        else:
                            if text is not None: 
                                print("listener heard: " + text)
                            print("stopped listening...")
                    else:
                        time.sleep(5)
                        sys.exit()
            except:
                continue   

Listener()