# -*- coding: utf8 -*-
#!/usr/bin/python3
import os

from gi.repository import Gtk

from bands.windows.bands_window import BandsWindow
from albums.windows.albums_window import AlbumsWindow
from albums.windows.new_album_window import NewAlbumWindow

from base.database import init_db
        
class Handler:        
    
    def on_click_bands(self, button):
        bw = BandsWindow()
        bw.window.show_all()
  
    def on_click_albums(self, button):
        aw = AlbumsWindow()
        aw.show_all()
          
    def on_click_add_album(self, button):
        naw = NewAlbumWindow()
        naw.show_all()
      
    def on_click_settings(self, button):
        sw = builder.get_object("settings_window")
        sw.resize(480, 360)
        sw.show_all()    

    def on_quit(self, *args):
        Gtk.main_quit(*args)
        
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
    
builder = Gtk.Builder()
builder.add_from_file("main.ui")
# Обработкичи событий 
builder.connect_signals(Handler())

window = builder.get_object("window")
window.show_all()

Gtk.main()
