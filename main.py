import tkinter as tk
import pyperclip
import platform

def copy_to_clipboard(copy):
    if platform.system() == 'Windows':
        import win32clipboard
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(copy)
        win32clipboard.CloseClipboard()
    elif platform.system() == 'Linux':
        from subprocess import call
        call(['xsel', '-bi'], input=copy)
    print("Success", copy)

root = tk.Tk()
root.title("Clipboard App")
root.geometry("250x100")

button4 = tk.Button(root, text="{", command= lambda: copy_to_clipboard("}") ,width=16)
button4.grid(row=0, column=0)

button4 = tk.Button(root, text="}", command= lambda: copy_to_clipboard("}") ,width=16)
button4.grid(row=0, column=1)

button2 = tk.Button(root, text="ñ", command= lambda: copy_to_clipboard("ñ") ,width=16)
button2.grid(row=1, column=0)

button = tk.Button(root, text="'", command= lambda: copy_to_clipboard("'") ,width=16)
button.grid(row=1, column=1)

button3 = tk.Button(root, text=">", command= lambda: copy_to_clipboard(">") ,width=16)
button3.grid(row=2, column=1)

button6 = tk.Button(root, text="<", command= lambda: copy_to_clipboard("<") ,width=16)
button6.grid(row=2, column=0)

root.mainloop()
