from Classifier import *
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf

class MessageDialogWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Mail Classification Tool")
        self.set_border_width(10)
        self.set_default_size(256, True)

        grid = Gtk.Grid()
        self.add(grid)

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename='images/logo.png', width=256,height=256,preserve_aspect_ratio=True)
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        grid.add(image)
        
        self.entry = Gtk.Entry()
        self.entry.set_text("Enter Some Text to check")
        grid.attach(self.entry,1,0,2,1)
        
        button1 = Gtk.Button("Check")
        button1.connect("clicked", self.check_mail)
        grid.attach_next_to(button1, self.entry, Gtk.PositionType.BOTTOM, 2, 1)
    
    def on_info_clicked(self, widget,text):
        print 
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Mail Classification")
        dialog.format_secondary_text(text)
        dialog.run()

        dialog.destroy()

    def check_mail(self,widget):
        a=self.entry.get_text()
        lis=[]
        # print(a)
        if(a!=''):
            lis.append(a)
            b=checkingmail(lis)
            # print(lis,b)
            a=b[0]
            if(a=='ham'):
                self.on_info_clicked(self,text="This Looks Okay, Not SPAM!")
                # print(lis,b)
                # Mail.delete(0,END)
                lis.clear()
            else:
                self.on_info_clicked(self,text="This is definetely SPAM!")
                # Mail.delete(0,END) 
                print(lis,b) 
                lis.clear()

win = MessageDialogWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
