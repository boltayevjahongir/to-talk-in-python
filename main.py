import speech_recognition as sr
import pyttsx3

mic = sr.Microphone()


# list_mic = sp.Microphone.list_microphone_names()
# for i in range (0, len(list_mic)):
#     print(i, list_mic[i])



r = sr.Recognizer()

while True:
    with mic as source:
        pyttsx3.speak("Son kiriting!")
        print("A=")
        audio = r.listen(source)
    try:

            a = r.recognize_google(audio, language="en-EN")
            try:
                a=int(a)
                break
            except:
                print("Siz son kiritmadingiz. Qaytadan kiriting")
                pyttsx3.speak("Siz son kiritmadingiz. Qaytadan kiriting")
            print("Out::" + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        pyttsx3.speak("men sizni tushunmadim. Iltimos qaytadan gapiring!")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

while True:
    with mic as source:
        pyttsx3.speak("Kiyingi Sonni kiriting")
        print("B=")
        audio = r.listen(source)
    try:
        b = r.recognize_google(audio, language="en-EN")
        try:
            b = int(b)
            break
        except:
            print("Siz son kiritmadingiz. Qaytadan kiriting")
            pyttsx3.speak("Siz son kiritmadingiz. Qaytadan kiriting")
        print("Out::" + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        pyttsx3.speak("men sizni tushunmadim. Iltimos qaytadan gapiring!")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

pyttsx3.speak(f"Natija: {a+b}")
print("A+B=", a+b)
