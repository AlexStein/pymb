from gi.repository import Gtk

from base.database import db_session

from bands.band import Band

class BandsWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Группы")

        self.store = Gtk.ListStore(int, str, str)
        
        for n, name, country in db_session.query(Band.id, Band.name, Band.country).order_by(Band.name): 
            self.store.append([n, name, country])
        
        button = Gtk.Button("Close")
        button.connect("clicked", self.on_button_clicked)

        treeView = Gtk.TreeView(self.store)
        
        renderer = Gtk.CellRendererText()
       
        c0 = Gtk.TreeViewColumn("", renderer, text=0)
        c0.set_visible(False)
        
        renderer_name = Gtk.CellRendererText()
        renderer_name.set_property("editable", True)
        
        c1 = Gtk.TreeViewColumn("Группа", renderer_name, text=1)        
        
        renderer_country = Gtk.CellRendererText()
        renderer_country.set_property("editable", True)
        
        c2 = Gtk.TreeViewColumn("Страна", renderer_country, text=2)
        
        treeView.append_column(c0)
        treeView.append_column(c1)
        treeView.append_column(c2)
        treeView.set_headers_clickable = True
        
        self.box = Gtk.Box(orientation=1)
        self.add(self.box)
        
        self.box.pack_start(treeView, True, True, 0)
        self.box.pack_start(button, True, True, 0)

        renderer_name.connect("edited", self.name_edited)
        renderer_country.connect("edited", self.country_edited)

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

    def on_button_clicked(self, widget):
        self.destroy()
        db_session.commit()