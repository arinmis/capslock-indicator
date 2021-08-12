#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GLib 

builder = Gtk.Builder()
builder.add_from_file("interfaces/on.glade")

window = builder.get_object("capslock-on")
# show caps-lock on pop up 
window.show()


# wait for a 2 second
# hide window
# GLib.timeout_add(2000, window.hide());
# look at this:  
# https://docs.gtk.org/glib/func.timeout_add.html

Gtk.main()



