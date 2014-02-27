from gi.repository import Gtk

from base.database import db_session

from bands.band import Band

class BandsWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Группы")

        store = Gtk.ListStore(str, str)
        
        for name, country in db_session.query(Band.name, Band.country).order_by(Band.name): 
            store.append([name, country])
        
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