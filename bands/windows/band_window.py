# -*- coding: utf8 -*-
from gi.repository import Gtk

from base.database import db_session

#from bands.band import Band

class BandWindow:

    def __init__(self, band):

        builder = Gtk.Builder()
        builder.add_from_file("band_dialog.ui")

        self.window = builder.get_object("band_dialog")
        self.entry_name = builder.get_object("entry_name")
        self.entry_country = builder.get_object("entry_country")
        # Обработкичи событий 
        builder.connect_signals(self)        

        self.edited = False
        self.band = band
        
    def on_entry_changed(self, widget):
        self.edited = True

    def on_ok_button_clicked(self, widget):
        if self.edited:
            self.band.name = self.entry_name.get_text()
            self.band.country = self.entry_country.get_text()
            
            db_session.add(self.band)
            db_session.commit()
        
        self.window.destroy()
        
    def on_cancel_button_clicked(self, widget):
        self.window.destroy()
        