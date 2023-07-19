import tkinter as tk

root = tk.Tk()

root.geometry('500x500')
root.title('Test-RIR Calculator')

label = tk.Label(root, text='Enter your name', font=('Arial',18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=2, font=('Arial',12))
textbox.pack(padx=10, pady=20)

entry = tk.Entry(root, font=('Arial',12))
entry.pack(padx=10, pady=10)

button_1 = tk.Button(root, text='Click here', font=('Arial',12))
button_1.pack()




root.mainloop()

