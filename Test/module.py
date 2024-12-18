import pyttsx3

word = "i am Sujit Tomar from Aurangabad Bihar 'Thank You So Much'"
speech = pyttsx3.init()
speech.say(word)
speech.runAndWait()