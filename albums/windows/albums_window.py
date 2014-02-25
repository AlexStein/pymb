# -*- coding: utf8 -*-

from gi.repository import Gtk

class AlbumsWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Альбомы")

        button = Gtk.Button("Close")
        button.connect("clicked", self.on_button_clicked)

        self.add(button)

    def on_button_clicked(self, widget):
        self.destroy()
