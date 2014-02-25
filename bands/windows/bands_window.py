from gi.repository import Gtk

from base.database import engine, db_session
from sqlalchemy.sql import select

from bands.band import Band

class BandsWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Группы")

        store = Gtk.ListStore(str, str)
        
        #conn = engine.connect()        
        
        #s = select([bands])
        #result = conn.execute(s)          
        
        for row in db_session.query(Band).order_by(Band.name): 
            store.append([row.name, row.country])
        
        button = Gtk.Button("Close")
        button.connect("clicked", self.on_button_clicked)

        treeView = Gtk.TreeView(store)
        
        renderer = Gtk.CellRendererText()
        
        c1 = Gtk.TreeViewColumn("Группа", renderer, text=0)        
        c2 = Gtk.TreeViewColumn("Страна", renderer, text=1)
        
        treeView.append_column(c1)
        treeView.append_column(c2)
        treeView.set_headers_clickable = True
        
        self.box = Gtk.Box(orientation=1)
        self.add(self.box)
        
        self.box.pack_start(treeView, True, True, 0)
        self.box.pack_start(button, True, True, 0)

    def on_button_clicked(self, widget):
        self.destroy()