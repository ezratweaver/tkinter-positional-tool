import tkinter as tk
from debug import debug_screen

window = tk.Tk()

window.geometry("500x300")
window.resizable(False, False)

debug_screen(window)

window.mainloop()

