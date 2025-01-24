import tkinter as tk


class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1280x720")
        self.root.title("Team 15")

        self.label = tk.Label(self.root, text="Splash Screen", font=('TkDefaultFont', 18))
        self.label.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Continue", font=('TkDefaultFont', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)


        self.root.mainloop()

    def show_message(self):
        self.label.destroy()

gui = MyGUI()