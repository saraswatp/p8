#!/usr/bin/env python
# coding: utf-8

# In[2]:

from klein import run, route
import _tkinter

app = flask.Flask(__name__)

@route('/')
def home():
    
    window = tkinter.Tk()
    window.title("Button GUI")
    button_widget = tkinter.Button(window,text="jai ho")
    button_widget.pack()
    tkinter.mainloop()
run("localhost", 8080)






# In[ ]:




