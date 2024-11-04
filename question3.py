import tkinter as tk

def display_name():
    name = name_entry.get()
    output_label.config(text=name)

window = tk.Tk()
window.title("Midterm in OOP")
window.geometry("600x400")

frame = tk.Frame(window)
frame.pack(expand=True)

name_label = tk.Label(frame, text="Enter your fullname:", fg='red')
name_label.grid(row=0, column=0, sticky='e', padx=10, pady=5)  # Align right

name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

display_button = tk.Button(frame, text="Click to display your Fullname", command=display_name, fg='red')
display_button.grid(row=1, column=0, pady=10)

output_label = tk.Label(frame, text="")
output_label.grid(row=1, column=1, padx=10, pady=5)

window.mainloop()
