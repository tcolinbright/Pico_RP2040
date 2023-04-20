import tkinter as tk
from datetime import datetime

# Function to append a log entry to the log file
def append_to_log_file():
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("log_file.txt", "a") as file:
        file.write(f"{dt_string}: {text_input.get()}\n")
    text_input.delete(0, tk.END)
    display_log_contents()

# Function to read the contents of the log file and display them in the Text widget
def display_log_contents():
    with open("log_file.txt", "r") as file:
        log_contents = file.read()
    log_text.delete(1.0, tk.END)
    log_text.insert(tk.END, log_contents)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Troubleshooting Log Entry Program")

# Create a label for the text input box
text_label = tk.Label(root, text="Enter troubleshooting step:")

# Initialize the text input box
text_input = tk.Entry(root, width=75)

# Pack the label and text input box into the window
text_label.pack()
text_input.pack()

# Initialize the submit button
submit_button = tk.Button(root, text="Submit", command=append_to_log_file)

# Pack the submit button into the window
submit_button.pack()

# Initialize the Text widget to display log contents
log_text = tk.Text(root, height=10, width=100)
log_text.pack()

# Display the initial contents of the log file
display_log_contents()

# Start the Tkinter event loop
root.mainloop()
