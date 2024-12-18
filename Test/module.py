import pyttsx3

textToSpeach = "i am Sujit Tomar from Aurangabad Bihar 'Thank You So Much'"
speech = pyttsx3.init()
speech.say(textToSpeach)
speech.runAndWait()