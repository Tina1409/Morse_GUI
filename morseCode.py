import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import ttk, messagebox
import time

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

LED_PIN = 10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

def blink_morse_code(name):
    name = name.upper()
    for char in name:
        if char in morse_code_dict:
            morse_code = morse_code_dict[char]
            for symbol in morse_code:
                if symbol == '.':
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.2)
                    GPIO.output(LED_PIN, GPIO.LOW)
                    time.sleep(0.2)
                elif symbol == '-':
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.6)
                    GPIO.output(LED_PIN, GPIO.LOW)
                    time.sleep(0.2)
            time.sleep(0.4)
        else:
            time.sleep(0.8)

def start_blinking():
    name = entry.get()
    if len(name) <= 12:
        blink_morse_code(name)
    else:
        messagebox.showerror("Error", "You cannot enter more than 12 letters")

root = tk.Tk()
root.title("Name to Morse Code LED Blinker")

frame = ttk.Frame(root, padding=(20, 20), style="My.TFrame")
frame.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

name_label = ttk.Label(root, text="Tina", font=("Courier", 20), foreground="pink")
name_label.grid(column=0, row=0, columnspan=2, pady=(20, 10))

entry = ttk.Entry(frame, width=20, font=("Courier", 20), background="pink")
entry.grid(column=0, row=0, columnspan=2, pady=(0, 20))

button = ttk.Button(frame, text="Start  ", command=start_blinking, style="TButton")
button.grid(column=0, row=1, columnspan=2, pady=(0, 20))

style = ttk.Style()
style.configure("TButton", background="pink", foreground="white", font=("Times New Roman", 20))
style.configure("My.TFrame", background="pink")

# Revert the frame size to normal
frame.config(padding=(20, 20))

root.mainloop()

GPIO.cleanup()