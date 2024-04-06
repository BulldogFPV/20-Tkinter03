###############################################################################
# Done: 1. (5 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 18 and
#   paste it below.
#
#   Now, use the geometry managers we have learned about and reorganize/
#   reformat your fillable form. You must use more than just the pack() method,
#   but you can still use it if it is what you need in a certain spot.
#
#   You may need to add more frames and such to move things around effectively.
#
#   Feel free to be creative on how you want your form to look.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
import tkinter as tk

window = tk.Tk()
window.title("Form")

def submit_form():
    form_data = {}
    for label_text, entry in zip(labels, entries):
        form_data[label_text] = entry.get()
    print("Form Submitted")
    for label, value in form_data.items():
        print(label + ":", value)

header_frame = tk.Frame(window)
header_frame.pack(side=tk.TOP)

form_frame = tk.Frame(window)
form_frame.pack(side=tk.TOP)

header_label = tk.Label(header_frame, text="Form Details", font=("Helvetica", 16))
header_label.pack()

labels = ["Name", "Address Line 1", "Address Line 2", "City", "State", "Zip Code", "Phone Number", "Email Address"]
entries = []
for i, label_text in enumerate(labels):
    label = tk.Label(form_frame, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5)
    
    entry = tk.Entry(form_frame)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.pack(pady=10)

window.configure(bg='cyan')
for entry in entries:
    entry.configure(bg='yellow')

window.mainloop()