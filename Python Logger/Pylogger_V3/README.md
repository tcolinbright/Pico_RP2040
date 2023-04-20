# Documentation for Troubleshooting Log Entry Program

## Introduction:
The Troubleshooting Log Entry Program is a Python program designed to allow users to enter and save troubleshooting steps in a log file for future reference. This program uses the Tkinter library to create a simple graphical user interface (GUI) that includes an entry box for the user to enter the troubleshooting step, a button to submit the entry to the log file, and a text box to display the contents of the log file.

## Installation:
To run the Troubleshooting Log Entry Program, you will need to have Python 3 installed on your computer. You can download the latest version of Python from the official Python website: https://www.python.org/downloads/.

Once Python is installed, you will need to create a virtual environment for the program using the following command in your terminal or command prompt:

```bash
python -m venv env
```
This command will create a new virtual environment called "env" in the current directory.

After the virtual environment is created, activate it using the following command:

```bash
source env/bin/activate
```

Next, install the required dependencies for the program using the following command:

```bash
pip install tkinter
```

Usage:
To run the Troubleshooting Log Entry Program, navigate to the directory where the program is located and activate the virtual environment using the following command:

```bash
source env/bin/activate
```

Then, run the program using the following command:

```bash
python pylogger_v3.1.py
```

This will launch the program in a new window. To enter a troubleshooting step, type the step into the entry box and press the "Submit" button or the "Enter" key. The troubleshooting step will be saved to a log file in the "logs" directory in the format "YYYY-MM-DD.txt", where "YYYY" is the year, "MM" is the month, and "DD" is the day.

The contents of the log file will be displayed in the text box below the entry box. To clear the contents of the text box, press the "Clear" button.

To exit the program, simply close the window or press the "Quit" button.


<br><br/>

## Walkthrough:

```python
import tkinter as tk
from datetime import datetime
import os
```

These are the necessary imports for the program. tkinter is a Python library for creating graphical user interfaces, datetime is used to obtain the current date and time, and os is used to create directories and access files.

```python
# Function to append a log entry to the log file
def append_to_log_file(event=None):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(get_log_file_path(), "a") as file:
        file.write(f"{dt_string}: {text_input.get()}\n")
    text_input.delete(0, tk.END)
    display_log_contents()
```

This function is called when the user submits a troubleshooting step. It retrieves the current date and time using ```datetime.now()```, formats it as a string, and writes a log entry to the file using ```open()```. The ```text_inpu```t widget is then cleared and the ```display_log_contents()``` function is called to refresh the contents of the ```log_text``` widget.

```python
# Function to read the contents of the log file and display them in the Text widget
def display_log_contents():
    with open(get_log_file_path(), "r") as file:
        log_contents = file.readlines()
    log_contents.reverse()
    log_text.delete(1.0, tk.END)
    for line in log_contents:
        log_text.insert(tk.END, line)
```

This function is called to display the contents of the log file in the ```log_text``` widget. It reads the log file using ```open()```, reverses the order of the log entries, clears the contents of the ```log_text widget```, and then inserts each log entry into the widget using a for loop.

```python
# Function to get the log file path for the current date
def get_log_file_path():
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return os.path.join(log_dir, f"{date_string}.txt")
```

This function returns the path to the log file for the current date. It uses ```datetime.now()``` to get the current date, creates a logs directory if one does not already exist, and then returns the path to a text file named with the current date.

```python
# Initialize the Tkinter window
root = tk.Tk()
root.title("Troubleshooting Log Entry Program")
```

This creates a new Tkinter window with the title "Troubleshooting Log Entry Program".

```python
# Create a label for the text input box
text_label = tk.Label(root, text="Enter troubleshooting step:")

# Initialize the text input box
text_input = tk.Entry(root, width=75)

# Bind the Return key to the append_to_log_file function
text_input.bind("<Return>", append_to_log_file)

# Pack the label and text input box into the window
text_label.pack()
text_input.pack()
```

These lines create a label and an entry box for the user to input their troubleshooting steps. The ```text_label``` and ```text_input``` widgets are then packed into the ```Tkinter``` window using ```pack()```. The ```bind()``` method is used to bind the Return key to the ```append_to_log_file()``` function.

```python
# Initialize the submit button
submit_button = tk.Button(root, text="Submit", command=append_to_log_file)
```

Pack the submit button into the window

```python
submit_button.pack()
```

The code above initializes a submit button that calls the ```append_to_log_file()``` function when clicked. The ```submit_button``` widget is then packed into the ```Tkinter``` window using ```pack()```.

```python
Initialize the Text widget to display log contents
log_text = tk.Text(root, height=20, width=80)
log_text.pack()
```

Display the initial contents of the log file

```python
display_log_contents()
```

Start the Tkinter event loop

```python
root.mainloop()
```

The code above initializes a Text widget called ```log_text``` to display the contents of the log file. The height and width of the widget are set using the height and width parameters. The widget is then packed into the ```Tkinter``` window using ```pack()```. The ```display_log_contents()``` function is called to display the initial contents of the log file in the widget. Finally, the ```Tkinter``` event loop is started using the ```mainloop()``` method.