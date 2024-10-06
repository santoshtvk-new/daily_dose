import tkinter as tk
from tkinter import messagebox, font

small_w = 50
small_h = 50
big_w = 300
bars = []
#################################################### UNDER DEVELOPMENT

class Sidebar(tk.Toplevel):
    def __init__(self, top):
        super().__init__(top)
        self.icon_style = False

        self.ws = self.winfo_screenwidth()  # width of the screen
        self.hs = self.winfo_screenheight()  # height of the screen

        # self.geometry(f"{small_w}x{small_h}+{int(self.ws - small_w)}+{int((self.hs / 2) - (small_h / 2))}")
        self.overrideredirect(True)
        self.yclick = 0
        self.xclick = 0
        self.config(bg='#888')
        self.attributes('-topmost', 'true')
        self.custom_font = font.Font(size=15)
        self.image = tk.PhotoImage(file="pull.png")
        self.touch = tk.Button(self, image=self.image, cursor='hand2')
        self.touch.bind('<Button-3>', self.toggle_window)
        self.touch.bind('<Button-1>', self.get_pos)
        self.touch.bind('<B1-Motion>', self.move_window)
        self.touch["border"] = "0"
        self.touch["bg"] = "white"
        self.touch.pack(side=tk.TOP)
        bars.append(self)

        self.listbox = tk.Listbox(root)
        self.scrollbar = tk.Scrollbar(root)
#
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.pack(fill=tk.BOTH, expand=1)
        self.geometry(f"{big_w}x{int(self.hs)}+{int(self.ws - big_w)}+{0}")
        self.icon_style = True
#
        for values in range(1000000, 1000100):
            self.listbox.insert(tk.END, values)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

    def toggle_window(self, event=None):
        if self.icon_style:
            self.scrollbar.pack_forget()
            self.geometry(f"{small_w}x{small_h}+{int(self.ws - small_w)}+{int((self.hs / 2) - (small_h / 2))}")
            self.icon_style = False
        else:
            self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
            self.scrollbar.pack(fill=tk.BOTH, expand=1)
            self.geometry(f"{big_w}x{int(self.hs)}+{int(self.ws - big_w)}+{0}")
            self.icon_style = True

    def get_pos(self, event):
        self.xclick = event.x
        self.yclick = event.y
        print(self.xclick, self.yclick)

    def move_window(self, event):
        self.geometry('+{0}+{1}'.format(self.ws - small_w, event.y_root - self.yclick))  # event.x_root - self.xclick

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Click OK to proceed closing Side-Bar Application"):
            self.destroy()
            root.destroy()


root = tk.Tk()
root.withdraw()
s = Sidebar(root)
s.mainloop()
