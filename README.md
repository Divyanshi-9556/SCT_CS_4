Basic Keylogger (Educational Use Only)
This project is part of my Cybersecurity Virtual Internship.
It demonstrates the concept of a keylogger, a program that captures keyboard input.

Disclaimer:
This program is developed strictly for educational purposes.
Running it on any computer without the owner’s knowledge and consent is illegal. Use responsibly.

Description
A keylogger is a tool that records the keys pressed on a keyboard.
This project creates a safe, educational keylogger that records keystrokes only while the program is running on your own computer.

Logs normal letters, numbers, and special keys.
Saves the captured keys in a file named keystrokes.log.
Can be stopped safely by pressing the ESC key.
Features
Records all keystrokes while the program is running.
Logs both regular characters and special keys (Enter, Space, Shift, etc.).
Easy to run and stop.
Helps understand how keylogging works in cybersecurity research.
⚙ Requirements
Python 3.x
pynput library
Install pynput using pip:

pip install pynput
▶ How to Run
Save the code as Keylogger.py.
Open Command Prompt or Terminal.
Navigate to the folder containing Keylogger.py, for example:
cd "C:\Users\ASUS\OneDrive\Desktop\vit"
Run the script:
python Keylogger.py
Start typing → all keystrokes will be recorded in keystrokes.log.
Stop the logger safely by pressing ESC.
Example Output (keystrokes.log)
h
e
l
l
o
[Key.space]
w
o
r
l
d
[Key.enter]
Learning Outcome
Understood how keyloggers capture keyboard events.
Learned to log data to a file.
Gained practical experience with Python event handling using pynput.
Developed awareness of ethical and safe usage in cybersecurity.
Important Notes
Only use this program on your own computer for learning purposes.
Never use it on others’ computers without permission — it is illegal.
Logs can be excluded from GitHub using .gitignore to prevent sensitive data from being uploaded.
Author
**Divyanshi Khare – Virtual Internship Task | Cybersecurity Education



