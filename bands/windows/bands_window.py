# -*- coding: utf8 -*-
from gi.repository import Gtk, Gdk

from base.database import db_session

from bands.band import Band
from bands.windows.band_window import BandWindow

class BandsWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Группы")

        self.store = Gtk.ListStore(int, str, str)
        
        for n, name, country in db_session.query(Band.id, Band.name, Band.country).order_by(Band.name).limit(100): 
            self.store.append([n, name, country])
        
        button = Gtk.Button("Close")
        button.connect("clicked", self.on_button_clicked)

        self.treeView = Gtk.TreeView(self.store)
        
        renderer = Gtk.CellRendererText()
       
        c0 = Gtk.TreeViewColumn("", renderer, text=0)
        c0.set_visible(False)
        
        renderer_name = Gtk.CellRendererText()
        renderer_name.set_property("editable", True)
        renderer_name.connect("edited", self.name_edited)
        
        c1 = Gtk.TreeViewColumn("Группа", renderer_name, text=1)        
        
        renderer_country = Gtk.CellRendererText()
        renderer_country.set_property("editable", True)
        renderer_country.connect("edited", self.country_edited)
        
        c2 = Gtk.TreeViewColumn("Страна", renderer_country, text=2)
        
        self.treeView.append_column(c0)
        self.treeView.append_column(c1)
        self.treeView.append_column(c2)
        self.treeView.set_headers_clickable = True
        self.treeView.set_reorderable(True)
        self.treeView.connect("button_press_event", self.on_row_doubleclicked)
        self.treeView.connect("key-press-event", self.on_hotkey_pressed)
        
        self.box = Gtk.Box(orientation=1)
        self.box.set_homogeneous(False)

        self.sw = Gtk.ScrolledWindow()
        self.sw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.sw.add(self.box)
        
        self.add(self.sw)

        self.box.pack_start(self.treeView, True, True, 0)
        #self.box.pack_end(button, True, True, 0)


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

    def on_row_doubleclicked(self, widget, event):
        if event.button == 1 and event.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:
            treeSelection = self.treeView.get_selection()
            (model, iter) = treeSelection.get_selected()
            n = self.store.get_value(iter, 0)          
            band = db_session.query(Band).get(n)
            edit_window = BandWindow(band)
            edit_window.show_all()

    def on_hotkey_pressed(self, widget, event):
        if Gdk.keyval_name(event.keyval) == "Insert":
            # Добавить группу
            band = Band(name = "", country = "")
            edit_window = BandWindow(band)
            edit_window.show_all()
                            
    def on_button_clicked(self, widget):
        self.destroy()
        db_session.commit()