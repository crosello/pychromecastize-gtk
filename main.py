#!/usr/bin/env python

import sys
import w_main

try:
    from gi.repository import Gtk
except RuntimeError, e:
    print("devel-assistant requires a currently running X server.")
    print("%s: %r" % (e.__class__.__name__, str(e)))
    sys.exit(1)

w_main.w_main()
