from google_trans_new import google_translator  
#Speech recognition API
import speech_recognition as sr
import pyttsx3

#Initiate Text to Speech
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

count = 0
lang = ""
langSet = False
while True:
    #string stores user's input
    string = ""
    #initiate the Speech recognition API setttings
    r = sr.Recognizer()
    r.pause_threshold = 0.5      


    #activate microphone and record
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1) 
        engine.say("Microphone listening for other person")
        engine.runAndWait()
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        #recognize_google can take a key but for development I will use the default API
        string = r.recognize_google(audio)
        string = string.lower()
        print("Google Speech Recognition thinks they said " + string)
        translator  = google_translator()
        if langSet == False:
            lang = translator.detect(string)
            lang = lang[0]
            langSet = True
        print(lang)
        print("f")
        engine.say(translator.translate(string))
        engine.runAndWait()
        count = 0
            #string stores user's input
        string = ""
        #initiate the Speech recognition API setttings
        r = sr.Recognizer()
        r.pause_threshold = 0.5      


        #activate microphone and record
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1) 
            engine.say("What do you want to translate to them?")
            engine.runAndWait()
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            #recognize_google can take a key but for development I will use the default API
            string = r.recognize_google(audio)
            string = string.lower()
            print("Google Speech Recognition thinks you said " + string)
            translator  = google_translator()
            engine.say(translator.translate(str(string), lang_tgt=lang))
            engine.runAndWait()
            count = 0
        except sr.UnknownValueError:
            if not count == 1:                
                engine.say("Try again")
                engine.runAndWait()
                count += 1
        except sr.RequestError as e:
            engine.say("No internet connection")
            engine.runAndWait()
            
    except sr.UnknownValueError:
        if not count == 1:
            engine.say("Try again")
            engine.runAndWait()
            count += 1
    except sr.RequestError as e:
            engine.say("No internet connection")
            engine.runAndWait()
   

