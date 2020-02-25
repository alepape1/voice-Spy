import speech_recognition as sr
import subprocess
import webbrowser

keyWords=["comprar","vender","necesito","viajar","quiero","viaje"]

r=sr.Recognizer()

#Search by google the input terms
def searchByGoogle(terms):
    # ... construct your list of search terms ...
    url = "https://www.google.com.tr/search?q={}".format(terms)
    webbrowser.open_new_tab(url)

#Record from the Microphone, check the charasteristics for recordin in record.py
def recordMicrophone():
    subprocess.call(['python', 'record.py'])

#Find the keyWords in the transcription of audio and search them on Google
def findKeyWords(transcription,keyWords):

    wordSucces=0;

    for keyWord in keyWords:

        if (transcription.find(keyWord)!=-1):
            print("The key word "+keyWord+" exist, finding on google")
            searchWords=keyWord+transcription.split(keyWord,1)[1]
            print (searchWords)
            searchByGoogle(searchWords)
            wordSucces += 1
        else:
            print("The key word doesn't exist")

    return (wordSucces)



recordMicrophone()

with sr.WavFile("output.wav") as source:              # use "output.wav" as the audio source
     audio = r.record(source)                        # extract audio data from the file

try:
    transcription=r.recognize_google(audio, language="es-ES")
    # transcription="Quiero comprar un burro"
    print("Transcription: " + transcription)   # recognize speech using Google Speech Recognition
    findKeyWords(transcription,keyWords)

except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")
