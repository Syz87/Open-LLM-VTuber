
from llm import talkToLLM, getMemory
from text2speech import speak 
from speech2text import launchContinuousSpeech2TextService, speech2TextOnce

def textInteractionMode():
    '''
    interact with the llm in text mode, but with speech output
    '''
    while True:
        callLLM(input(">> "))

def speechInteractionMode():
    '''
    Lauch the speech to text service and interact with the llm in speech mode.
    The function callbackToLLM is the callback function when a sentence is recognized.
    '''
    # The commented code below is for continuous speech to text service.
    # The recognizer will listen to you even when the llm is talking (so it can hear itself...)
    # Not recommended if you are using the speaker
    # recognitionResult = launchContinuousSpeech2TextService(callLLM)

    while True:
        recognitionResult = speech2TextOnce()
        if(recognitionResult != ""):
            print("\n>> Recognized: \n" + recognitionResult + "\n")
            callLLM(recognitionResult)
            print("\n======\n")
    


def callLLM(text, verbose=False):
        '''
        Call the llm with text and print the result.
        text: str
            the text that is recognized
        '''
        result = talkToLLM(text)
        if verbose:
            print(">> Results: \n")
            print(result)
        speak(result)
        print("\n")


# =======

if __name__ == "__main__":
    speechInteractionMode()
    #  textInteractionMode()

    
