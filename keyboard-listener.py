from pynput.keyboard import Key, Listener, Controller

keyboard = Controller()

def on_press(key):
    print('{0} pressed'.format(key))
    print(keyboard.shift_pressed)
     

# Collect events until released
with Listener(on_press=on_press) as listener:
    listener.join()

