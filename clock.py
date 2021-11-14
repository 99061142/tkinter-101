from tkinter import *
from time import strftime


# Makes the window
window = Tk() # Make window
window.title('Clock') # Window title
window.geometry("800x200") # Window size


# Updates the time
def clock(): 
    time = strftime("%H:%M:%S") # Get the time
    text.set(time) # Updates the label
    window.after(1000, clock) # Loop every second


text = StringVar() # Time

# Makes the label
label = Label(window)

label = Label(
    window, 
    font=("arial", 140, 'bold'), 
    bg="lightblue", 
)

label.configure(textvariable=text)

label.pack(
    fill="both", expand=True
    )


# If the code starts
if __name__ == "__main__":
    clock() 
    window.mainloop() 