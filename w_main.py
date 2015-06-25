#!/usr/bin/env python
import os

from handlers import handlers
from gi.repository import Gtk

gladefile = os.path.join(os.path.dirname(__file__), "w_main.glade")

class w_main(object):

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladefile)
        self.firstWin = self.builder.get_object("main")

        all_handlers = handlers(self.builder)

        self.builder.connect_signals(all_handlers)

        self.firstWin.connect("delete-event", Gtk.main_quit)
        self.firstWin.show_all()
        print "Starting ..."
        Gtk.main()

