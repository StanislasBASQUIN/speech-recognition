import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime


listener = sr.Recognizer() # Ecoute sur les peripheriques
engine = pyttsx3.init() # Permet à la machine de répondre
voice = engine.getProperty('voices') # Fetching properties of voices
engine.setProperty('voice', voice[3].id) # configurer la voix de la machine en français


def parler(text):
    engine.say(text)  # Machine prononce la commande enregistrée
    engine.runAndWait()



def ecouter():
    # On utilise Try Except pour gérer les erreurs
    try:
        with sr.Microphone() as source: # Branchement du programme sur micro
            print("Merci de parler maintenant")
            voix = listener.listen(source) # Enregistrement de la Voix
            command = listener.recognize_google(voix, language='fr-FR') # Interpretation de la Voix user
            return command
    except:
        pass




def lancer_assistant():
    command = ecouter()
    print(command)

    # Playing YouTube video with playonyt.
    if 'jouer le morceau de' in command:
        chanteur = command.replace('jouer le morceau de', '') # Ne conserver que le nom du chanteur dans la command
        print(chanteur)
        pywhatkit.playonyt(chanteur)

    # Giving Current Time
    elif 'heure' in command:
        heure = datetime.datetime.now().strftime('%H hour and %M minutes') # Format Time in String.
        parler('It is : '+heure)

    # Salutation
    elif 'bonjour' in command:
        parler('Good Morning, how are you friend?')


    # pywhatkit.search allows searching on Google.
    elif 'Google' in command:
        recherche = command.replace('Hello Google Recherche', '')
        print('Searching...')
        pywhatkit.search(recherche)
        pywhatkit.info(recherche, lines=10)
        print("\nSuccessfully Searched")


# How to target more specific word in the Research Sentence?
# Slicing the String. Target a Specific Word (ex. : 'cherche')
# Create a dictionary of Key words initializing the research.



    else:
        # Printing Error Message
        print("An unknown error occurred")

lancer_assistant()