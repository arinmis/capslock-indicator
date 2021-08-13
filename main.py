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
time = 1500

# get capslock status
is_capslock_on = status.get_capslock_status()



# show caps-lock on pop up 
# for given time
# then hide the window
def show_on(time):
    print("here")
    # update status 
    is_capslock_on = True 
    # build interfaces
    builder = Gtk.Builder()
    builder.add_from_file("interfaces/on.glade")
    window = builder.get_object("capslock-on")
    window.show()
    GLib.timeout_add(time, window.hide);
    Gtk.main()
    Gtk.main_quit()
     


# show caps-lock off pop up 
# for given time
# then hide the window
def show_off(time):
    # update status 
    is_capslock_on = False 
    # build interfaces
    builder = Gtk.Builder()
    builder.add_from_file("interfaces/off.glade")
    window = builder.get_object("capslock-off")
    window.show()
    GLib.timeout_add(time, window.hide);
    Gtk.main()
    Gtk.main_quit()

# listen keyboard
keyboard = Controller()


def on_press(key):
    # show capslock on
    if key == Key.caps_lock:
        if not is_capslock_on:
            print("caps lock is on")
            show_on(time)
        else: # show capslock off 
            print("caps lock is off")
            show_off(time)
     

# Collect events until released
with Listener(on_press=on_press) as listener:
    listener.join()

# main loop
