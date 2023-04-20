import tkinter as tk
from datetime import datetime
import os

# Function to append a log entry to the log file
def append_to_log_file(event=None):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(get_log_file_path(), "a") as file:
        file.write(f"{dt_string}: {text_input.get()}\n")
    text_input.delete(0, tk.END)
    display_log_contents()

# Function to read the contents of the log file and display them in the Text widget
def display_log_contents():
    log_file_path = get_log_file_path()
    if not os.path.exists(log_file_path):
        with open(log_file_path, 'w') as f:
            pass
    with open(log_file_path, "r") as file:
        log_contents = file.readlines()
    log_contents.reverse()
    log_text.delete(1.0, tk.END)
    for line in log_contents:
        log_text.insert(tk.END, line)

# Function to get the log file path for the current date
def get_log_file_path():
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return os.path.join(log_dir, f"{date_string}.txt")


def search_logs():
    search_string = search_input.get()
    with open(get_log_file_path(), "r") as file:
        log_contents = file.readlines()
    matching_lines = [line for line in log_contents if search_string in line]
    log_text.delete(1.0, tk.END)
    for line in matching_lines:
        log_text.insert(tk.END, line)


# Initialize the Tkinter window
root = tk.Tk()
root.title("Troubleshooting Log Entry Program")

# Create a label for the text input box
text_label = tk.Label(root, text="Enter troubleshooting step:")

# Initialize the text input box
text_input = tk.Entry(root, width=75)

# Bind the Return key to the append_to_log_file function
text_input.bind("<Return>", append_to_log_file)

# Pack the label and text input box into the window
text_label.pack()
text_input.pack()

# Initialize the submit button
submit_button = tk.Button(root, text="Submit", command=append_to_log_file)

# Pack the submit button into the window
submit_button.pack()

# Initialize the Text widget to display log contents
log_text = tk.Text(root, height=20, width=80)
log_text.pack()

# Create a label and entry box for the search input
search_label = tk.Label(root, text="Search logs:")
search_input = tk.Entry(root, width=50)

# Pack the search label and input box into the window
search_label.pack()
search_input.pack()

# Create a search button and bind it to the search_logs() function
search_button = tk.Button(root, text="Search", command=search_logs)
search_button.pack()



# Display the initial contents of the log file
display_log_contents()

# Start the Tkinter event loop
root.mainloop()
