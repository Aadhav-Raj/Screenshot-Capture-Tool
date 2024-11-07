# Screenshot-Capture-Tool

Screenshot Capture Tool

This tool is a Python-based utility that captures screenshots within a specified bounding box when the "Print Screen" key is pressed. Screenshots are saved in a designated folder, starting from a user-specified number, and named sequentially based on the initial number input.

Features:

Capture screenshots with the "Print Screen" key within a defined screen area.
Automatic folder creation for screenshots if the folder doesn't already exist.
Dynamic sequential naming of screenshots based on a starting number provided by the user (e.g., 1.png, 2.png, etc.).
Exit the application by pressing the "Delete" key.

Requirements:

Python 3.x
Pillow for image handling (PIL module)
pyautogui for GUI interactions
pynput for keyboard event handling
Installation
Install the required libraries:


Specify the starting number for the screenshots in the prompt that appears. This number will be used as the starting filename for your screenshots.

Press the "Print Screen" key to take a screenshot. The screenshot will:

Be captured within a bounding box defined by coordinates (112, 44, 1251, 679).
Be saved in a screenshots folder in the same directory as the script.
Be named sequentially based on the starting number you entered (e.g., 1.png, 2.png, etc.).
Press the "Delete" key to exit the application.