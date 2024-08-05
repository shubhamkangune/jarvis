import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()

def processCommand(c):
  if "open google" in c.lower():
    webbrowser.open("https://google.com")
  elif "open youtube" in c.lower():
    webbrowser.open("https://youtube.com")
  elif "open facebook" in c.lower():
    webbrowser.open("https://facebook.com")
  elif "open linkedin" in c.lower():
    webbrowser.open("https://linkedin.com")
  elif c.lower().startswith("play"):
    song = c.lower().split(" ")[1]
    link = musicLibrary.music[song]
    webbrowser.open(link)
  
  elif "news" in c.lower():
    r = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={"bf4815d2000f4d17aa40c9e5b4ebc565"}')
    if r.status_code == 200:
      data = r.json()

      articles = data.get('articles',[])


      for article in articles:
        speak(article['title'])
  



if __name__ == "__main__":

  speak("Initializing Jarvis...")
  while True:

    #Listen for the wake word "jarvis" 
    # obtain audio from the microphone

    r = sr.Recognizer()
    print("recognizing...")
    # recognizing speech using sphinx
    try:
      
      with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source,timeout=2,phrase_time_limit=1)

      word  = r.recognize_google(audio)
      if(word.lower() == "jarvis"):
        speak("Ya")
        # listen for command
        with sr.Microphone() as source:
          print("Jarvis active...")
          audio = r.listen(source)
          command = r.recognize_google(audio)

          processCommand(command)
    
    except Exception as e:
      print("Error; {0}".format(e))