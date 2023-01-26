#!/bin/env python

import tkinter as tk
import pyp3rclip
import keyboard

class ClipboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clipboard App")
        self.geometry("280x100")
        self.attributes('-topmost', True)
        self.resizable(False, False)
        self.create_buttons()
        self.bind("<Key>", self.key)

    # a function if press ctrl and shift to same time print "Success"
    def key(self, event):
        try:
            if keyboard.is_pressed("ctrl+shift+1"):  # if key "name of your key" is pressed  
                self.copy_to_clipboard("{")

            if keyboard.is_pressed("ctrl+shift+2"):  # if key "name of your key" is pressed  
                self.copy_to_clipboard("}")

            if keyboard.is_pressed("ctrl+shift+3"):  # if key "name of your key" is pressed  
                self.copy_to_clipboard("ñ")

            if keyboard.is_pressed("ctrl+shift+4"):  # if key "name of your key" is pressed  
                self.copy_to_clipboard("'")

            if keyboard.is_pressed("ctrl+shift+5"):  # if key "name of your key" is pressed  
                self.copy_to_clipboard(">")

            if keyboard.is_pressed("ctrl+shift+6"):  # if key "name of your key" is pressed  
                self.copy_to_clipboard("<")

        except KeyError: # If other key is pressed,it will raise an error
            pass  # we won't do anything about it,just let the cycle continue

    def create_buttons(self):
        button4 = tk.Button(self, text="{", command= lambda: self.copy_to_clipboard("{") ,width=16)
        button4.grid(row=0, column=0)

        button4 = tk.Button(self, text="}", command= lambda: self.copy_to_clipboard("}") ,width=16)
        button4.grid(row=0, column=1)

        button2 = tk.Button(self, text="ñ", command= lambda: self.copy_to_clipboard("ñ") ,width=16)
        button2.grid(row=1, column=0)

        button = tk.Button(self, text="'", command= lambda: self.copy_to_clipboard("'") ,width=16)
        button.grid(row=1, column=1)

        button3 = tk.Button(self, text=">", command= lambda: self.copy_to_clipboard(">") ,width=16)
        button3.grid(row=2, column=1)

        button6 = tk.Button(self, text="<", command= lambda: self.copy_to_clipboard("<") ,width=16)
        button6.grid(row=2, column=0)

    def copy_to_clipboard(self, copy):
        pyp3rclip.copy(copy)
        print("Success", copy)

if __name__ == "__main__":
    app = ClipboardApp()
    app.mainloop()

