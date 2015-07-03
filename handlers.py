#!/usr/bin/env python

from gi.repository import Gtk
from convert import Convert

class handlers():

    def __init__(self, builder):
        self.builder = builder

    def on_close_clicked(self, *args):
        print "Quit ..."
        Gtk.main_quit(*args)

    def on_file_set(self, widget):
        file_name = widget.get_filename()
        text_file = self.builder.get_object('text_file')
        text_file.set_text(file_name)

    def on_exec_clicked(self, widget):
        text_file = self.builder.get_object('text_file')
        file_name = text_file.get_text()
        output = self.builder.get_object('output')

        is_mp4 = self.builder.get_object("extension_mp4").get_active()
        is_mkv = self.builder.get_object("extension_mkv").get_active()

        extension = "mp4" if is_mp4 is True else "mkv"

        converter = Convert()
        converter.run(file_name, extension, output)
