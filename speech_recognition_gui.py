import tkinter as tk
import speech_recognition as sr
import webbrowser
import time

class SpeechRecognitionGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Voice2Web")

        # create a label for instructions
        self.instructions_label = tk.Label(self.window, text="Press the button and Ask", font=("Helvetica",20))
        self.instructions_label.pack(pady=10)

        # create a button for starting the speech recognition
        self.recognize_button = tk.Button(self.window, text="Search", command=self.recognize_speech)
        self.recognize_button.config(bg="purple", fg="white",font=("Verdana", 14,"bold"))
        self.recognize_button.pack()

        # create a label for displaying the recognized text
        self.text_label = tk.Label(self.window, text="")
        self.text_label.pack(pady=10)

        self.window.mainloop()

    def recognize_speech(self):
        # initialize the recognizer
        r = sr.Recognizer()

        # record audio from the microphone
        with sr.Microphone() as source:
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            text = r.recognize_google(audio, language='en-US')
            self.text_label.config(pady="10", padx="5")
            self.text_label.config(text="You Spoke : \n" + text, font=("Arial", 12))
            time.sleep(3)

            def google_search(text):
                url = f"https://www.google.com/search?q={text}"
                webbrowser.open(url)

            # call the google_search function with the recognized text
            google_search(text)
        except sr.UnknownValueError:
            self.text_label.config(text="Could not understand audio, please Retry", font=("Arial", 12))
        except sr.RequestError as e:
            self.text_label.config(text="Could not request results from Google Speech Recognition service.\n Please Check Your Internet Connection", font=("Arial", 12))

# create an instance of the SpeechRecognitionGUI class
gui = SpeechRecognitionGUI()