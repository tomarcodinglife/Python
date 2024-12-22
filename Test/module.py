import pyttsx3

word = "i am Sujit Kumar Singh from Aurangabad Bihar 'Thank You So Much'"
print(word)
textToSpeech = pyttsx3.init()
textToSpeech.say(word)
textToSpeech.runAndWait()