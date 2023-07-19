import tkinter as tk

class gui:
    def __init__(self):
        self.root = tk.Tk()
        self.textbox = tk.Text(self.root, height=2, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Click here', font=('Arial',12), command=self.show_message)
        self.button.pack()

        self.root.mainloop()

    def show_message(self):
        print(self.textbox.get('1.0', tk.END))

gui()
