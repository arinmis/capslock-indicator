import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# create window
win = Gtk.Window()


# remove header bar
hb = Gtk.HeaderBar()
hb.set_show_close_button(False)
win.set_titlebar(hb)

# capsloc images
capslock_on_img = Gtk.Image()
capslock_on_img.new_from_file("images/demo.png")

#######################
box = Gtk.Box()
box.set_spacing(50)
#box.set_orientation (Gtk.Orientation.VERTICAL)
win.add(box)

box.pack_start(capslock_on_img, True, True, 0)
######################

# show capslock on image
def capslock_on(): 
    win.show_all()  


win.connect("destroy", Gtk.main_quit)
# remove 
win.show_all()

#win.hide()
Gtk.main()


