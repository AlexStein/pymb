# -*- coding: utf8 -*-
#!/usr/bin/python3
import os

from gi.repository import Gtk

from bands.windows.bands_window import BandsWindow
from albums.windows.albums_window import AlbumsWindow
from albums.windows.new_album_window import NewAlbumWindow
from settings.windows.settings_window import SettingsWindow

from base.database import init_db

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="pyMB")

        table = Gtk.Table(2, 2, True)
        self.add(table)
    
        button1 = Gtk.Button(label="Группы")
        button1.connect("clicked", self.on_click_bands)
        
        button2 = Gtk.Button(label="Альбомы")
        button2.connect("clicked", self.on_click_albums)
        
        button3 = Gtk.Button(label="Добавить")
        button3.connect("clicked", self.on_click_add_album)
        
        button4 = Gtk.Button(label="Настройки")
        button4.connect("clicked", self.on_click_settings)
          
        table.attach(button1, 0, 1, 0, 1)
        table.attach(button2, 1, 2, 0, 1)
        table.attach(button3, 0, 1, 1, 2)
        table.attach(button4, 1, 2, 1, 2)
  
    def on_click_bands(self, button):
        bw = BandsWindow()
        bw.resize(480, 360)
        bw.show_all()
  
    def on_click_albums(self, button):
        aw = AlbumsWindow()
        aw.show_all()
          
    def on_click_add_album(self, button):
        naw = NewAlbumWindow()
        naw.show_all()
      
    def on_click_settings(self, button):
        sw = SettingsWindow()
        sw.show_all()    

def write_pidfile_or_die(path_to_pidfile):

    if os.path.exists(path_to_pidfile):
        pid = int(open(path_to_pidfile).read())

        if pid_is_running(pid):
            print("Программа уже запущена!  Process {0} is still running.".format(pid))
            raise SystemExit

        else:
            os.remove(path_to_pidfile)

    open(path_to_pidfile, 'w').write(str(os.getpid()))
    return path_to_pidfile

def pid_is_running(pid):
    try:
        os.kill(pid, 0)

    except OSError:
        return

    else:
        return pid

# Проверяем pid-файл
write_pidfile_or_die('/tmp/pymb.pid')

init_db()
    
win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.resize(480, 360)
win.show_all()
Gtk.main()
