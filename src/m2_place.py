import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# Done: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 2. (4 pts)
#
#   Now, create one frame dimensions 200 by 200.
#
#   Use the default pack() method to place it in the window.
#
#   Also, place 3 labels in the frame labeling them as Label A, Label B, and
#   Label C and give them different background colors.
#
#   Use the place() method to place each of these labels at different
#   coordinates such that they do not overlap.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################
window = tk.Tk()
window.title("Tkinter Example")
window.geometry("400x400")

frame = tk.Frame(window, width=200, height=200, bg="purple")
frame.pack()

label_a = tk.Label(frame, text="Label A", bg="lime green")
label_b = tk.Label(frame, text="Label B", bg="cyan")
label_c = tk.Label(frame, text="Label C", bg="yellow")

label_a.place(x=10, y=10)
label_b.place(x=100, y=50)
label_c.place(x=50, y=130)

window.mainloop()