import tkinter as tk
window = tk.Tk()

window.title('Hello') # Window title

window.geometry("150x100") # Window size

window.configure(bg="gray") # Window background


# box 1
box1 = tk.Label(
    window,
    text="Hello \n tkinter!",
    bg="green",
    fg="orange",
    font=('arial',15)
)

# Box 1 size (x = width / y = height)
box1.pack(
    ipadx=15,
    ipady=7.5,
    expand=True
)

window.mainloop()