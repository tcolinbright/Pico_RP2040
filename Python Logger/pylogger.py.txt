import datetime
import tkinter as tk

def append_to_log_file(event=None):
    now = datetime.datetime.now()
    log_entry = f"{now}: {text_input.get()}\n"
    with open("log_file.txt", "a") as f:
        f.write(log_entry)
    text_input.delete(0, tk.END)

root = tk.Tk()
root.title("Log Entry")
root.geometry("400x200")

text_input = tk.Entry(root, width=50, bd=5)
text_input.pack()
text_input.bind("<Return>", append_to_log_file)

submit_button = tk.Button(root, text="Submit")
submit_button.pack()

root.mainloop()