import bardEngine
from localDetection import WakeListener
import speechInput
from spotifyHandler import Play
import tts
import asyncio

async def main():
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
                # start the timer
                input_text = None

                async def input_checker():
                    nonlocal input_text
                    await asyncio.sleep(5)  # Wait for 5 seconds
                    if input_text is not None:
                        response = bardEngine.request(input_text)
                        tts.Speak(response,1)

                input_task = asyncio.create_task(input_checker())

                # listen for query
                input_text = str(speechInput.Processor())

                # Cancel the input_checker task if input is received before 5 seconds
                input_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())
