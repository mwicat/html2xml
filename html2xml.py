import gtk
import webkit
import gobject
import javascriptcore as jscore

import sys
import os

def load_finished_cb(view, frame):
    ctx = jscore.JSContext(view.get_main_frame().get_global_context())
    jsw = ctx.globalObject.window
    doc = jsw.document
    serializer = ctx.evaluateScript('new XMLSerializer()')
    print serializer.serializeToString(doc)
    gtk.main_quit()


gobject.threads_init()
window = gtk.Window()
view = webkit.WebView()

view.connect("load-finished", load_finished_cb)
view.load_string(sys.stdin.read(), "text/html", "utf-8", "file://")

gtk.main()
