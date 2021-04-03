import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('paint')
win.geometry("1000x800")
my_canvas=tk.Canvas(win,width=800,height=400,bg='white')
my_canvas.pack(pady=20)
def func(e):
    x1=e.x -1
    y1=e.y -1
    x2=e.x +1
    y2=e.y +1
    size=10
    brush_type='round'
    brush_color='green'
    my_canvas.create_line(x1,y1,x2,y2,width=size,capstyle=brush_type,fill=brush_color,smooth=True)
def func1():
    pass
my_canvas.bind('<B1-Motion>',func)
my_frame=tk.Frame(win)
my_frame.pack(pady=20)
my_label=tk.Label(my_frame,text='Brush Size')
my_label.grid(row=0,column=0)

slider=ttk.Scale(my_label,from_=1,to=70,command=func1,value=10)
slider.pack(padx=5,pady=5)
win.mainloop()