#!/usr/bin/env python3 
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk 
from gi.repository import GLib 

# keyboard lib
from pynput.keyboard import Key, Listener, Controller

# capslock status
import status

# pop up time in ms
time = 700

# get capslock status
is_capslock_on = status.get_capslock_status()




# show caps-lock on pop up 
# for given time
# then hide the window
def show_on():
    # build interfaces
    builder = Gtk.Builder()
    builder.add_from_file("interfaces/on.glade")
    window = builder.get_object("capslock-on")
    return window

     

# show caps-lock off pop up 
# for given time
# then hide the win
def show_off():
    # build interfaces
    builder = Gtk.Builder()
    builder.add_from_file("interfaces/off.glade")
    window = builder.get_object("capslock-off")
    return window


# listen keyboard
keyboard = Controller()

class MyException(Exception): 
    pass


def on_press(key):

    # define gloabal variable for pynput 
    global is_capslock_on 
      
    # exit keyboard listener
    window = Gtk.Window()
    if key == Key.esc:
        raise MyException(key) 
    
    if key == Key.caps_lock:
        if not is_capslock_on:
            window = show_on()
            is_capslock_on = True
        else:
            window = show_off()
            is_capslock_on = False 

        # show window and kill  
        window.show_all()
        GLib.timeout_add(time, window.hide);
        # connect destroy event
        window.connect("destroy", Gtk.main_quit)
        # quit window after 1 ms
        GLib.timeout_add(time, Gtk.main_quit) 
        Gtk.main()


     

# Collect events until released
with Listener(on_press=on_press) as listener:
    listener.join()

