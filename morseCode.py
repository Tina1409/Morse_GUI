#importing necessary libraries
import RPi.GPIO as GPIO 
import tkinter as tk  
from tkinter import ttk  
import time  

#creating a cutsom morse code
morse_code_dic = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'  
}

# Setting up the GPIO pins
led_pin = 7 
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(led_pin, GPIO.OUT)  

#function for led to blink corresponding to the morse code generated
def custom_blink_morse_code(text):
    for char in text.upper():
        if char in morse_code_dic:
            morse_code = morse_code_dic[char]
            for character in morse_code:
                if character == '.':
                    GPIO.output(led_pin, GPIO.HIGH)
                    time.sleep(0.2)  
                    GPIO.output(led_pin, GPIO.LOW)
                    time.sleep(0.2)  
                elif character == '-':
                    GPIO.output(led_pin, GPIO.HIGH)
                    time.sleep(0.6)  
                    GPIO.output(led_pin, GPIO.LOW)
                    time.sleep(0.2)  
            time.sleep(0.4)  
        else:
            #handling unknown characters with a long time delay
            time.sleep(0.8)  

# setting up the GUI
root = tk.Tk()  
root.title("Morse Code Led Blinker")  #title of the window

#handling operations when button is clicked
def blinking():
    text = custom_entry.get()  
    custom_blink_morse_code(text)  

#GUI background
custom_frame = ttk.Frame(root, padding=(20, 20))
custom_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
custom_frame.columnconfigure(0, weight=1)
custom_frame.rowconfigure(0, weight=1)

#creating a label
custom_label = ttk.Label(custom_frame, text="Enter your name", font=("Arial", 20), foreground="blue")
custom_label.grid(column=0, row=0, columnspan=2, pady=(0, 20))

#text input
custom_entry = ttk.Entry(custom_frame, width=20, font=("Arial", 20), background="lightblue")
custom_entry.grid(column=0, row=1, columnspan=2, pady=(0, 10))

custom_button = ttk.Button(custom_frame, text="Blink", command=blinking)
custom_button.grid(column=0, row=2, columnspan=2, pady=(0, 20))

root.mainloop()
GPIO.cleanup()
