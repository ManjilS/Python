import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# Capture the audio from the microphone
with sr.Microphone() as source:
    print("Please say something:")
    audio = recognizer.listen(source)

    try:
        # Recognize speech using Google's Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
