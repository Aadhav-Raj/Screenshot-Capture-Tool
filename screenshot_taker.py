from PIL import ImageGrab
import pyautogui as py
from pynput import keyboard
import os
import sys

inputt = 0
listener = None

def screenshot(key):
    global inputt
    if key == keyboard.Key.print_screen:
        print("Print Screen key pressed.")
        # Define the bounding box
        bbox = (112, 44, 1251, 679)
        
        # Take the screenshot
        screenshot = ImageGrab.grab(bbox=bbox)
        
        # Get the directory of the script or executable
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define the folder name
        folder_name = "screenshots"
        
        # Create the folder path
        folder_path = os.path.join(script_dir, folder_name)
        
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        
        # Define the image file path
        image_path = os.path.join(folder_path, f"{inputt}.png")
        
        # Save the screenshot
        screenshot.save(image_path)
        print(f"Screenshot saved as {image_path}")
        inputt += 1
        screenshot.close()
    
    elif key == keyboard.Key.delete:
        print("Delete key pressed. Exiting.")
        if listener is not None:
            listener.stop()
        sys.exit()

def on_press(key):
    screenshot(key)

inputt = int(py.prompt(text="", title="Enter the Number of Screenshot to start from:"))
print(f"Starting from screenshot number: {inputt}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
