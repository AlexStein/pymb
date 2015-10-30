# -*- coding: utf8 -*-

from gi.repository import Gtk

from base.database import db_session

from albums.album import Album
#from albums.windows.new_album_window import NewAlbumWindow


class AlbumsWindow:

    def __init__(self):

        builder = Gtk.Builder()
        builder.add_from_file("albums_window.ui")
        
        self.window = builder.get_object("albums_window")
        self.store  = builder.get_object("list_albums")

        builder.connect_signals(self)        
        
        for n, name, year in db_session.query(Album.id, Album.name, Album.year).order_by(Album.year).limit(100): 
            self.store.append([n, name, year])
        
        self.treeView = builder.get_object("treeView")

    def on_button_clicked(self, widget):
        self.destroy()
