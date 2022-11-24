from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter import messagebox
import os

filename = None

def newFile():
    global filename
    filename = None
    root.title("Untiteld")
    text.delete(0.0, END)

def saveFile ():
    global filename
    t = text.get(0.0, END)
    f  = open(file = filename, mode="w")
    f.write(t)
    f.close()
    
    

def saveAs():
    global filename
    filename = asksaveasfile(mode='w', defaultextension=  ".txt ", initialfile="Untiled")
    t = text.get(0.0, END)
    try:
        filename.write(t.rstrip())
    except:
        messagebox.showerror("Oops", "Unable to save the file!!")

def openFile():
    global filename
    filename = askopenfilename(defaultextension=".txt")
    root.title(os.path.basename(filename))
    t  = open(filename, 'r')
    text.delete(0.0, END)
    text.insert(0.0, t.read())
    t.close()


root = Tk()
root.title("My own Notepad")
root.minsize(width=400, height= 400)
root.maxsize(width=800, height= 800)

text = Text( root, width=800, height=800)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command= openFile)
filemenu.add_command(label="Save", command= saveFile)
filemenu.add_command(label="SaveAs", command= saveAs)

filemenu.add_separator()

filemenu.add_command(label="Quit",command= root.quit)
menubar.add_cascade(label="File" , menu =filemenu)

root.config(menu = menubar)
root.mainloop()