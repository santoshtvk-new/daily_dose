import tkinter as tk
from tkinter import messagebox, font

bars = []


class Sidebar(tk.Toplevel):
    def __init__(self, top):
        super().__init__(top)

        self.yclick = 0
        self.xclick = 0
        self.config(bg='#838383')
        self.attributes('-topmost', 'true')
        self.resizable(True, True)
        self.custom_font = font.Font(size=15)

        self.titlebar = tk.Frame(self, bg='#FFFF00', relief='flat', bd=2)
        self.titlebar.bind('<Button-1>', self.get_pos)
        self.titlebar.bind('<B1-Motion>', self.move_window)
        self.titlebar.pack(fill=tk.X, expand=1, side=tk.TOP)

        self.closebutton = tk.Label(self.titlebar, text='X', bg='#FFFF00', relief='flat', cursor='hand2',
                                    font=self.custom_font)
        self.closebutton.bind('<Button-1>', self.quit_window)
        self.closebutton.pack(side=tk.RIGHT)
        bars.append(self)

    def quit_window(self, event):
        self.closebutton.config(relief='flat', bd=0)
        if messagebox.askyesno('Delete Note?', 'Are you sure you want to delete this note?', parent=self):
            self.destroy()
            root.destroy()

    def get_pos(self, event):
        self.xclick = event.x
        self.yclick = event.y
        print(self.xclick, self.yclick)

    def move_window(self, event):
        self.geometry('+{0}+{1}'.format(event.x_root - self.xclick, event.y_root - self.yclick))

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
            root.destroy()


root = tk.Tk()

def on_closing():
    print("gone")
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        for i in bars:
            i.on_closing()
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)

s = Sidebar(root)
s.mainloop()


# from tkinter import *
# from tkinter import ttk
#
# # Create an instance of tkinter frame or window
# win=Tk()
#
# # Set the size of the window
# win.geometry("700x350")
# win.overrideredirect(True)
#
# ws = win.winfo_screenwidth() # width of the screen
# hs = win.winfo_screenheight() # height of the screen
#
# # calculate x and y coordinates for the Tk root window
# x = (ws/2) - (700/2)
# y = (hs/2) - (350/2)
#
# def moveMouseButton(e):
#     x1 = e.x_root()
#     y1 = e.y_root()
#     x0 = e.x()
#     y0 = e.y()
#
#     win.geometry("%s x %s" % ((x1 - x0), (y1 - y0)))
#
# win.geometry('%dx%d+%d+%d' % (700, 350, x, y))
#
# # Add a Label widget
# label=Label(win,text="Grab the lower-right corner to resize the window")
# label.pack(side="top", fill="both", expand=True)
#
# # Add the gripper for resizing the window
# grip=ttk.Sizegrip()
# grip.place(relx=1.0, rely=1.0, anchor="se")
# grip.lift(label)
# grip.bind("<B1-Motion>", moveMouseButton)
#
# win.mainloop()
