import tkinter as tk

Window = tk.Tk()
Window.geometry("400x300")

#var_list = ["bin", "oct", "hex"]
EntryRezult = 0
selection = 0

class Convector:
   def __init__(self):
    global EntryRezult
    Text = tk.Label(Window, text="Конвектор в разные системы счисления... ")
    Text.pack()
    Textt = tk.Label(Window, text="Введите число и выберите систему..")
    Textt.pack()
    var_list = tk.StringVar(value=["bin", "oct", "hex"])
    self.List = tk.Listbox(Window,listvariable= var_list,selectmode=tk.SINGLE, width=20, height=3)
    self.List.pack()
    self.Entry = tk.Entry(Window)
    self.Entry.pack()
    EntryRezult = self.Entry.get()
    self.List.bind("<<ListboxSelect>>", self.Rasschet)
   def Rasschet(self, event = None):
     selection = self.List.curselection()
     index = selection
     item_text = self.List.get(index)
     self.List.get(selection)
     if item_text == "bin":
       self.bins()
     elif item_text == "oct":
       self.oct()
     elif item_text == "hex":
       self.hex()
     if not selection:
       return
   def bins(self):
     global EntryRezult
     EntryRezult = int(self.Entry.get())
     EntryRezult = bin(EntryRezult)[2:]
     lbl = tk.Label(Window,text=f"РЕЗУЛЬТАТ ПЕРЕВОДА В 2 СИСТЕМУ : {EntryRezult}")
     lbl.pack()
   def oct(self):
     global EntryRezult
     EntryRezult = int(self.Entry.get())
     EntryRezult = oct(EntryRezult)[2:]
     lbl = tk.Label(Window,text=f"РЕЗУЛЬТАТ ПЕРЕВОДА В 8 СИСТЕМУ: {EntryRezult}")
     lbl.pack()
   def hex(self):
     global EntryRezult
     EntryRezult = int(self.Entry.get())
     EntryRezult = hex(EntryRezult)[2:]
     lbl = tk.Label(Window,text=f"РЕЗУЛЬТАТ ПЕРЕВОДА В 16 СИСТЕМУ: {EntryRezult}")
     lbl.pack()
convect = Convector()

Window.mainloop()
