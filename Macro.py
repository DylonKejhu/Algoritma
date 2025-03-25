import pyautogui
import time
import keyboard

# Function to simulate key press and mouse clicks
def perform_macro():
    while True:
        # Check if the 'M' key is pressed to stop the loop
        if keyboard.is_pressed('m'):
            print("Macro stopped!")
            break

        # Press the '1' key for inventory
        pyautogui.press('1')  # Simulate pressing the '1' key for inventory
        time.sleep(0.2)  # Add a short delay to ensure it registers
        
        # Click the mouse 5 times
        for _ in range(5):
            pyautogui.click()
            time.sleep(0.3)  # Small delay between clicks
        
        # Press the '2' key for the next action
        pyautogui.press('2')  # Simulate pressing the '2' key
        time.sleep(0.2)  # Add a short delay to ensure it registers
        # Click the mouse 1 time
        pyautogui.click()

        # Delay before repeating the loop, adjust as needed
        time.sleep(1)

# Call the function to run the macro
perform_macro()
2