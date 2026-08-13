import tkinter as tk

window = tk.Tk()

window.geometry("500x500")
window.title("wtfamidoinhere")

label = tk.Label(window, text="hello world", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(window, font=("Arial", 20))
textbox.pack()
window.mainloop()