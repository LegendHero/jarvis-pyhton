import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import googlesearch
import webbrowser
import smtplib
wikipedia != None 

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
print('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
        
    if hour>=0 and hour<=12:
        speak("good morning")  


    elif hour>=12 and hour<18:
        speak("good after noon")

    else:
        speak("good evening")

    speak('hello iam jarvis. tell me what do you want to see')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


        try:
            print("recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said, {query}\n")


        except Exception as e:
            print(e)
            print("please say that again")
            
        return query 
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls
    server.login("dnkdnk", "*hhdhd")
    server.sendmail("djh", to, content)
    server.close()


if __name__ == "__main__":
    
    wishme()
    if 1:
        query = takeCommand().lower()
        if "wikipedia" in query:
            print("searching wikipedia")

            speak("searching wikipedia")

            query = query.replace("wikipedia", "")

            results = wikipedia.summary(query, sentences=2)

            speak("according to wikipedia")

            speak(results)

            print(results)
            
        elif "open youtube" in query:   
            webbrowser.open("youtube.com")

        elif "open google" in query:   
            webbrowser.open("google.com")

        elif "open firefox" in query:   
            webbrowser.open("firefox.com.com")


        elif "open spotify" in query:   
            webbrowser.open("spotify.com")

        elif "hello jarvis" in query:   
            speak('''hello sir . would u like to have a drink.
            but i cant do that''')  

        elif "hi" in query:   
            speak('''hi, what would u like to see''')    
        
        elif "jarvis show project" in query:   
            speak('''no . i dont have any  projects fucker  ''')    

        elif "ass" in query:
            speak("i need to tell your parents . about your misbehaviouer")    
            

            



        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f"sir. the time is {strTime}")
            print(strTime)

        elif "open code" in query:   
            webbrowser.open("VS Code APK")
        else:
            speak("i could do a google search for")
            webbrowser.open(f"{query}")    

        
            if "quit" in query:
                exit()        

             