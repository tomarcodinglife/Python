import pyttsx3
word = "i am Sujit Kumar Singh from Aurangabad Bihar 'Thank You So Much'"
textToSpeech = pyttsx3.init()
textToSpeech.say(word)
textToSpeech.runAndWait()