# #Import tkinter library
# from tkinter import *
# from tkinter import ttk

# #Create an instance of Tkinter frame or window
# win = Tk()

# #Set the geometry of tkinter frame
# win.geometry("750x250")
# def callback():
#    Label(win, text="Hello World!", font=('Georgia 20 bold')).pack(pady=4)

# #Create a Label and a Button widget
# btn = ttk.Button(win, text="Press Enter to Show a Message", command= callback)
# btn.pack(ipadx=10)

# win.bind('<Return>',lambda event:callback())

# win.mainloop()

#Import tkinter library
from logging import root
from tkinter import *
from tkinter import ttk

from numpy import size
# root = Tk()
# root.title("Lchat")


BG_COLOR = "#DBE6FF"

gil = Tk()
gil.title('Lchat')
#Create an instance of tkinter frame or window
#Set the geometry of tkinter frame

gil.configure(background=BG_COLOR)
gil.geometry("750x250+400+300")
#Create a Label widget
#send thing
def send(e: Text):
    content = e.get("1.0", END)
    to_send = "You -> " + content + '\n'
    e.delete('1.0', END)
    txt['text'] += to_send

txt = Label(gil, bg=BG_COLOR, anchor='w', justify=LEFT)
# scrollbar = Scrollbar(gil, orient='vertical')
# scrollbar.pack(side=RIGHT, fill='y')
txt.pack(side=TOP, fill='both')

#idk what to call this
e = Text(width=500, height=1)
e.pack(side=BOTTOM)
e.bind('<Return>', lambda x: send(e))

gil.mainloop()