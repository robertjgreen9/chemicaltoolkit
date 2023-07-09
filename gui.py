import tkinter as tk

root = tk.Tk()
root.geometry("300x200") # Set the size of the window

variable1_entry = tk.Entry(root)
variable1_entry.pack()

variable2 = tk.StringVar(root)
variable2.set("Option 1") # set the default option

# Populate variable2_options with values from a file
# variable2_options = []
# with open("options.txt", "r") as f:
#     for line in f:
#         variable2_options.append(line.strip())

# variable2_entry = tk.OptionMenu(root, variable2, *variable2_options)
# variable2_entry.pack()

def on_button_click():
    variable1 = variable1_entry.get()
    #variable2_value = variable2.get()
    #my_function(variable1, variable2_value)
    my_function(variable1, variable1)

button = tk.Button(root, text="Run Function", command=on_button_click)
button.pack()

root.mainloop()