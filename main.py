import pywhatkit
import speech_recognition as sr
import pyttsx3 as ttx


listener = sr.Recognizer() # Ecoute sur les peripheriques
engine = ttx.init() # Permet à la machine de répondre
voice = engine.getProperty('voices') #
engine.setProperty('voice', 'french') # configurer la voix de la machine en anglais

def parler(text):
    engine.say(text)  # Machine prononce la commande enregistrée
    engine.runAndWait()


def ecouter():
    # On utilise Try Except pour gérer les erreurs
    try:
        with sr.Microphone() as source: # Branchement du programme sur micro
            print("Merci de parler maintenant")
            voix = listener.listen(source) # Enregistrement de la Voix
            command = listener.recognize_google(voix, language="fr-FR") # Interpretation de la Voix
            return command
    except:
        pass


def lancer_assistant():
    command = ecouter()
    print(command)
    if 'jouer le morceau de' in command:
        chanteur = command.replace('jouer le morceau de', '') # Ne conserver que le nom du chanteur dans la command
        print(chanteur)
        pywhatkit.playonyt(chanteur)


    elif 'heure'
lancer_assistant()