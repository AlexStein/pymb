# -*- coding: utf8 -*-

from gi.repository import Gtk

from base.database import db_session


class AlbumWindow:

    def __init__(self):

        builder = Gtk.Builder()
        builder.add_from_file("album_window.ui")

        self.window = builder.get_object("album_window")
        self.entry_name = builder.get_object("entry_name")
        self.entry_year = builder.get_object("entry_year")
        # Обработкичи событий 
        builder.connect_signals(self)  

    def on_button_clicked(self, widget):
        self.destroy()