import pyautogui
import time

# Initial value and increment
start = 3.0
end = 10.0
increment = 0.1
delay = 0.1  # Delay in seconds

# Ensure user is ready
print("Starting in 5 seconds. Focus on the desired input field.")
time.sleep(5)

current = start
while current <= end:
    # Left click
    pyautogui.click()
    
    # Select all and backspace
    pyautogui.hotkey('ctrl', 'a')  # Select all
    time.sleep(delay)  # Small delay
    pyautogui.press('backspace')  # Backspace to clear
    
    # Type the value
    pyautogui.typewrite(f"{current:.1f}")  # Type the number
    
    # Press Enter
    pyautogui.press('enter')  # Simulate pressing Enter
    
    # Left click again
    pyautogui.click()
    time.sleep(delay)
    
    # Increment the value
    current += increment
    current = round(current, 1)  # Avoid floating-point precision issues
