# -*- coding: utf8 -*-
from gi.repository import Gtk, Gdk

from base.database import db_session

from bands.band import Band
from bands.windows.band_window import BandWindow

class BandsWindow:

    def __init__(self):

        builder = Gtk.Builder()
        builder.add_from_file("bands_window.ui")
        
        self.window = builder.get_object("bands_window")
        self.store  = builder.get_object("store")

        builder.connect_signals(self)        
        
        for n, name, country in db_session.query(Band.id, Band.name, Band.country).order_by(Band.name).limit(100): 
            self.store.append([n, name, country])
        
        self.treeView = builder.get_object("treeView")

    def name_edited(self, widget, path, text):
        n = self.store[path][0]
        self.store[path][1] = text
        
        band = db_session.query(Band).get(n)
        band.name = text
        
    def country_edited(self, widget, path, text):
        n = self.store[path][0]
        self.store[path][2] = text
        
        band = db_session.query(Band).get(n)
        band.country = text

    def on_refresh_button_clicked(self, widget):
        self.refresh_treeview
    
    def refresh_treeview(self):
        self.store.clear()
        db_session.refresh
        for n, name, country in db_session.query(Band.id, Band.name, Band.country).order_by(Band.name).limit(100): 
            self.store.append([n, name, country])        

    def on_row_doubleclicked(self, widget, event):
        if event.button == 1 and event.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:
            treeSelection = self.treeView.get_selection()
            (model, iter) = treeSelection.get_selected()
            n = self.store.get_value(iter, 0)          
            band = db_session.query(Band).get(n)
            edit_window = BandWindow(band)
            edit_window.window.show_all()

    def new_band(self):
        band = Band(name = "", country = "")
        edit_window = BandWindow(band)
        edit_window.window.show_all()    

    def on_add_button_clicked(self, widget):
        self.new_band()

    def on_hotkey_pressed(self, widget, event):
        if Gdk.keyval_name(event.keyval) == "Insert":
            self.new_band()
                            
    def on_button_clicked(self, widget):
        self.window.destroy()
        db_session.commit()