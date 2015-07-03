#!/usr/bin/env python

from gi.repository import Gdk, GObject

import os, threading, locale

class Convert:
    def __init__(self):
        GObject.threads_init()
        Gdk.threads_init()
        encoding = locale.getpreferredencoding()
        self.utf8conv = lambda x : unicode(x, encoding).encode('utf8')

    def run(self, filename, extension, output):
        """
        @type filename: str
        @type extension: str
        @type output: gi.repository.Gtk.TextView.TextView
        """
        output_buffer = output.get_buffer()
        """@type : gi.repository.Gtk.TextBuffer.TextBuffer"""
        output_buffer.set_text("");

        if not os.path.isfile(filename):
            output_buffer.set_text("File not found")
            return

        command = 'chromecastize --%s "%s"' % (extension, filename)
        print ('Command : %s' % filename)

        thr = threading.Thread(target= self.read_output, args=(output, output_buffer, command))
        thr.start()

    def read_output(self, view, buffer, command):
        stdin, stdouterr = os.popen4(command)
        while 1:
            line = stdouterr.readline()
            if not line:
                break
            Gdk.threads_enter()
            iter = buffer.get_end_iter()
            buffer.place_cursor(iter)
            buffer.insert(iter, self.utf8conv(line))
            #view.scroll_to_mark(buffer.get_insert(), 0.1)
            Gdk.threads_leave()
