import tkinter as tk
import speech_recognition as spr
from tkinter import messagebox

def recognize_speech():
    r = spr.Recognizer()
    try:
        with spr.Microphone() as source:
            print("Adjusting for ambient noise...")
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source, timeout=4)
    except spr.WaitTimeoutError:
        messagebox.showwarning("Speech Recognizer", "No speech detected. Please try again.")
        return

    languages = ("en-IN", "ta-IN", "te-IN")
    longest_text = ""
    longest_language = ""
    for language in languages:
        try:
            text = r.recognize_google(audio, language=language)
            if len(text) > len(longest_text):
                longest_text = text
                longest_language = language
        except spr.UnknownValueError:
            print(f"Could not understand audio in {language}.")
        except spr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition API; {e}")

    if longest_language:
        result_text.set(f"You said in {longest_language}: {longest_text}")
    else:
        result_text.set("No speech was recognized.")

# Initialize the root window
root = tk.Tk()
root.title("Speech Recognizer")

# Create a source object

# Create a stringvar to display the result
result_text = tk.StringVar()

# Create a label to display the result
ttk.Label(root, textvariable=result_text).grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Create a button to trigger speech recognition
ttk.Button(root, text="Record", command=recognize_speech).grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Start the mainloop
root.mainloop()
