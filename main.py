import time
import winsound
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newVoiceRate = 150  # change this number to change speed of voice. 200 is default
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', newVoiceRate)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def sound():
    winsound.PlaySound('alarm.wav', winsound.SND_ASYNC)


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    sound()
    time.sleep(1)
    speak("Countdown completed")
    print("Countdown completed!")
    time.sleep(5)


t = input("Enter the time for countdown in seconds: ")

countdown(int(t))
