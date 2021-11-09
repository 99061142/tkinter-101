import tkinter
from time import sleep

window = tkinter.Tk()

# Code
window.title("My First Window") # Window title
size = 50 # Width and height of the window
color_num = 0 # Number of the color that is chosen 


# Change the window
def change_window():
    global size
    global color_num

    colors = ("white", "yellow", "orange", "red", "purple", "black") # All the colors for the window
        

    # If there must be a new color for the window
    if color_num < len(colors):
        # Prints the countdown
        countdown_num = 6 - color_num 
        print(countdown_num)

        # Changes the window size
        window_size = f"{size}x{size}"
        window.geometry(window_size) 
    
        size += 50 # Updates the size

        color = colors[color_num] # Pick the color
        window.configure(bg = color) # Change the window background color
        color_num += 1 # updates the number for the color that must be chosen

        window.after(2000, change_window)
    
    # If all the colors are chosen
    else:
        window.destroy()
        print("BOOM!")


# If the code starts
if __name__ == "__main__":
    change_window() # Changes the window
    window.mainloop() # Opens the window