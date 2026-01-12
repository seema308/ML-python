import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")

    try:
        print("Text: " + r.recognize_google(audio_text))
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
