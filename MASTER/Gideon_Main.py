import bardEngine
from localDetection import WakeListener
import speechInput
from spotifyHandler import Play
import tts

while True:
    # listen for the wake word
    if WakeListener() is True:
        # pause active audio
        tts.Speak("", 0)
        # listen for query
        inputText = str(speechInput.Processor())
        # process query
        if inputText == "quit" or inputText == "exit":
            exit()
        elif inputText == "False":
            print("I'm sorry, an error has occured!")
            tts.Speak("I'm sorry, an error has occured!",1)
        elif "play" in inputText:
            if "song " in inputText:
                if "by" in inputText:
                    inputText1 = inputText[inputText.index("song")+len("song")+1:inputText.index("by")]
                    inputText2 = inputText.split("by",1)[1]
                    Play(f"{inputText1}{inputText2}","song")
                else:
                    inputText = inputText.split("song",1)[1]
                    Play(inputText, "song")
            elif "playlist" in inputText:
                print("here")
                if "by" in inputText:
                    inputText1 = inputText[inputText.index("playlist")+len("playlist")+1:inputText.index("by")]
                    inputText2 = inputText.split("by",1)[1]
                    Play(f"{inputText1} {inputText2}", "playlist")
                else:
                    inputText = inputText.split("playlist",1)[1]
                    Play(inputText, "playlist")
            else:
                if "by" in inputText:
                    inputText1 = inputText[inputText.index("play")+len("play")+1:inputText.index("by")]
                    inputText2 = inputText.split("by",1)[1]
                    Play(f"{inputText1}{inputText2}","song")
                else:
                    inputText = inputText.split("play",1)[1]
                    Play(inputText, "song")
        else:
            response = bardEngine.request(inputText)
            tts.Speak(response, 1)
            inputText = None
        '''
        # Wait for input or continue after 5 seconds
        timeout_seconds = 5
        start_time = time.time()
        inputText = str(speechInput.Processor())
        while time.time() - start_time < timeout_seconds:
            if inputText != None:
                response = bardEngine.request(inputText)
        
        if inputText is None or inputText == "False" or inputText == " ":
            print("No input received. Continuing code...")
            break  # Exit the inner loop and continue to the outer loop 
        '''

