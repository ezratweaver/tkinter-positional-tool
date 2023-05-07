import tkinter as tk

debug_window = tk.Tk()

def debug_screen(main_window):
    x_text = tk.Label(debug_window, text="X:", font=("Impact", 20), anchor="center")
    y_text = tk.Label(debug_window, text="Y:", font=("Impact", 20), anchor="center")

    x_text.place(x=72, y=30)
    y_text.place(x=72, y=70)

    def print_mouse_position(event):
        x, y = event.x, event.y
        x_text.config(text=f"X: {x}")
        y_text.config(text=f"Y: {y}")

    def close_windows():
        debug_window.destroy()
        main_window.destroy()


    main_window.bind("<Motion>", print_mouse_position)

    main_window.protocol("WM_DELETE_WINDOW", close_windows)
    debug_window.protocol("WM_DELETE_WINDOW", close_windows)

    debug_window.geometry("200x150+1000+100")
    debug_window.resizable(False, False)
    debug_window.mainloop()