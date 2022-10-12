import speech_recognition as sr

listener = sr.Recognizer()
engine = ttx.init()

voice =


try:
    with sr.Microphone() as source:
        print("Merci de parler maintenant")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)

except:
    pass

