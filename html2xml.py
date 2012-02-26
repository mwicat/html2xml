import gtk
import webkit
import gobject
import javascriptcore as jscore
import tidy

options = dict(output_xhtml=1, 
               add_xml_decl=1,
               numeric_entities=1,
               indent=1, 
               tidy_mark=0)


import sys
import os

def load_finished_cb(view, frame):
    ctx = jscore.JSContext(view.get_main_frame().get_global_context())
    jsw = ctx.globalObject.window
    doc = jsw.document
    serializer = ctx.evaluateScript('new XMLSerializer()')
    html_str = serializer.serializeToString(doc)
    xml_str = tidy.parseString(html_str, **options)
    print xml_str
    gtk.main_quit()


gobject.threads_init()
window = gtk.Window()
view = webkit.WebView()

view.connect("load-finished", load_finished_cb)
view.load_string(sys.stdin.read(), "text/html", "utf-8", "file://")

gtk.main()
