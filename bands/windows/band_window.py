from gi.repository import Gtk

from base.database import db_session

from bands.band import Band

class BandWindow(Gtk.Window):

    def __init__(self, band):
        Gtk.Dialog.__init__(self, title="Группа")

        """ Version > 3.10
        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        hbox.pack_start(listbox, True, True, 0)        
        
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Наименование", xalign=0)
        entry = Gtk.Entry()
        
        self.entry.set_text(band.name)        
        
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(entry, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Страна", xalign=0)
        entry = Gtk.Entry()
        
        self.entry.set_text(band.country)        
        
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(entry, False, True, 0)
        
        listbox.add(row)
        """
        
        self.edited = False
        self.band = band
        
        table = Gtk.Table(3, 2, True)
        table.props.margin = 6
        self.add(table)

        label1 = Gtk.Label("Наименование", xalign=0)
        self.entry1 = Gtk.Entry()
        self.entry1.set_max_length(255)
        self.entry1.set_text(self.band.name)
        self.entry1.connect("changed", self.on_edit)

        label2 = Gtk.Label("Страна", xalign=0)
        self.entry2 = Gtk.Entry()
        self.entry2.set_max_length(255)
        self.entry2.set_text(self.band.country)
        self.entry2.connect("changed", self.on_edit)
        
        button = Gtk.Button("OK")
        button.connect("clicked", self.on_button_clicked)

        table.attach(label1, 0, 1, 0, 1)
        table.attach(self.entry1, 1, 2, 0, 1)
        table.attach(label2, 0, 1, 1, 2)
        table.attach(self.entry2, 1, 2, 1, 2)
        table.attach(button, 1, 2, 2, 3)        
    
    def on_edit(self, widget):
        self.edited = True

    def on_button_clicked(self, widget):
        if self.edited:
            self.band.name = self.entry1.get_text()
            self.band.country = self.entry2.get_text()
          
            db_session.commit()
        
        self.destroy()