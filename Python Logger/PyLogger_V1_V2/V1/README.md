# Troubleshooting Log Entry Program

The Troubleshooting Log Entry Program is a simple Python program that allows you to enter troubleshooting steps into a log file. Each entry is timestamped with the current date and time, and the program provides a text input box and a submit button for ease of use.

## Usage:

To use the Troubleshooting Log Entry Program, follow these steps:

   - Make sure you have Python 3 installed on your computer.

   - Download the program code from the GitHub repository.

   - Open a terminal or command prompt and navigate to the directory where you downloaded the program code.

   - Run the program by executing the following command:

   - python log_entry.py

   - A window will appear with a text input box and a submit button. Enter your troubleshooting steps in the text input box and click the submit button.

   - The program will append your entry to a log file called log_file.txt in the same directory as the program code. Each entry will be timestamped with the current date and time.

   - The text input box will be cleared after each submission, allowing you to enter a new log entry.

## Dependencies:

The Troubleshooting Log Entry Program requires the following dependencies:

   - Python 3.x
   - Tkinter (included with most Python installations)

## Installation:

To install the Troubleshooting Log Entry Program, follow these steps:

   - Download the program code from the GitHub repository.

   - Make sure you have Python 3 installed on your computer.

   - Open a terminal or command prompt and navigate to the directory where you downloaded the program code.

   - Run the program by executing the following command:


    python log_entry.py

<br><br/>

## Code

The code for the Troubleshooting Log Entry Program is shown below:

```python

import datetime
import tkinter as tk

def append_to_log_file():
    now = datetime.datetime.now()
    log_entry = f"{now}: {text_input.get()}\\n"
    with open("log_file.txt", "a") as f:
        f.write(log_entry)
    text_input.delete(0, tk.END)

root = tk.Tk()
root.title("Log Entry")
root.geometry("400x200")

text_input = tk.Entry(root, width=50)
text_input.pack()

submit_button = tk.Button(root, text="Submit", command=append_to_log_file)
submit_button.pack()

root.mainloop()
```

<br><br/>

## Walkthrough:

The code begins by importing the ```datetime``` and ```tkinter``` modules. The ```datetime``` module is used to generate timestamps for each log entry, and the ```tkinter``` module is used to create the program's graphical user interface.

```python
import datetime
import tkinter as tk
```


The append_to_log_file function is defined next. This function is called when the user clicks the submit button. It generates a timestamp using the datetime.now() function, retrieves the contents of the text input box using the get method of the Entry widget, and appends the timestamp and log entry to a file called log_file.txt.

```python
def append_to_log_file():
    now = datetime.datetime.now()
    log_entry = f"{now}: {text_input.get()}\\n"
    with open("log_file.txt", "a") as f:
        f.write(log_entry)
    text_input.delete(0, tk.END)
```


The root variable is then initialized as a Tk object, which represents the main window of the program. The title method is used to set the window title to "Log Entry", and the geometry method is used to set the window size to 400x200 pixels.

```python
root = tk.Tk()
root.title("Log Entry")
root.geometry("400x200")
```

The ```text_input``` variable is then initialized as an ```Entry``` widget, which provides a text input box for the user to enter their troubleshooting steps. The width parameter is set to 50, which sets the width. The ```text_input``` widget is then packed using the ```pack``` method, which adds it to the main window.

```python
text_input = tk.Entry(root, width=50)
text_input.pack()
```

The ```submit_button``` variable is initialized as a ```Button``` widget, which provides a clickable button that the user can press to submit their log entry. The text parameter is set to "Submit", which sets the text displayed on the button.

The command parameter is set to the ```append_to_log_file``` function, which is called when the user clicks the button.

Finally, the ```submit_button``` widget is packed using the ```pack``` method, which adds it to the main window.

```python
submit_button = tk.Button(root, text="Submit", command=append_to_log_file)
submit_button.pack()
```



The ```root.mainloop()``` function is called at the end of the program, which starts the Tkinter event loop and allows the program to respond to user input.

```python
root.mainloop()
```

## Conclusion:

The Troubleshooting Log Entry Program is a simple Python program that allows you to enter troubleshooting steps into a log file. By using the program's text input box and submit button, you can easily track your troubleshooting steps and keep a record of your progress.