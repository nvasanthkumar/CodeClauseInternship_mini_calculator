from tkinter import *
root=Tk()
root.config(bd=5)
root.title('mini calculator')
root.iconbitmap('calc.ico')
root.resizable(0,0)
button_colour='gray80'
button_font=('ubuntu',20)
button_width,button_height=5,2
l=[]
e = Entry(root, width=31, bd=20, bg='white', font=(button_font, 20),justify='right')  # Adjust font size here
e.grid(row=0, column=0,padx=2,pady=(5, 0), ipady=5, columnspan=5, sticky='W')
e.focus()

def click(number):
    if e.get=='ERROR':
        clear()
    else:
        current=e.get()
        e.delete(0,END)
        e.insert(0,str(current)+str(number))

def clear(event):
    e.delete(0,END)
def equal(event):
    l.append(e.get())
    try:
        # global displayed
        ans=eval(e.get())
        e.delete(0,END)
        e.insert(0,ans)
    except:
        ans='ERROR'
        e.delete(0,END)
        e.insert(0,ans)
    l.append(ans)
    my_listbox.insert('end','\u27A1'+str(l[-2]))
    my_listbox.insert('end', '=' + str(l[-1]))
def back(event):
    expression=e.get()
    if expression:
        expression=expression[:-1]
        e.delete(0,END)
        e.insert(0,expression)

my_frame=Frame(root,width=50,height=50)
my_scrollbar=Scrollbar(my_frame,orient=VERTICAL)
my_listbox=Listbox(my_frame,yscrollcommand=my_scrollbar.set,height=18,font=10,width=12,bg='gray65')
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
my_listbox.pack()
my_frame.grid(row=1,column=4,rowspan=5,ipady=2)


Button7=Button(root,text="7",command=lambda:click(7),bg=button_colour,font=button_font,width=button_width,height=button_height).grid(row=1,column=0)
Button8=Button(root,text="8",command=lambda:click(8),bg=button_colour,font=button_font,width=button_width,height=button_height).grid(row=1,column=1)
Button9=Button(root,text="9",command=lambda:click(9),bg=button_colour,font=button_font,width=button_width,height=button_height).grid(row=1,column=2)
Button6=Button(root,text="6",command=lambda:click(6),width=button_width,height=button_height,bg=button_colour,font=button_font).grid(row=2,column=2)
Button5=Button(root,text="5",command=lambda:click(5),width=button_width,height=button_height,bg=button_colour,font=button_font).grid(row=2,column=1)
Button4=Button(root,text="4",command=lambda:click(4),width=button_width,height=button_height,bg=button_colour,font=button_font).grid(row=2,column=0)
Button3=Button(root,text="3",command=lambda:click(3),width=button_width,height=button_height,bg=button_colour,font=button_font).grid(row=3,column=2)
Button2=Button(root,text="2",command=lambda:click(2),width=button_width,height=button_height,bg=button_colour,font=button_font).grid(row=3,column=1)
Button1=Button(root,text="1",command=lambda:click(1),width=button_width,height=button_height,bg=button_colour,font=button_font).grid(row=3,column=0)
Button0=Button(root,text="0",command=lambda:click(0),width=button_width,height=button_height,bg=button_colour,font=button_font).grid(row=4,column=1)
Buttonplus=Button(root,text="+",command=lambda:click('+'),width=button_width,height=button_height,bg=button_colour,font=button_font).grid(row=4,column=3)
Buttonequal=Button(root,text="ans",command=equal,width=button_width,height=button_height,bg=button_colour,font=button_font).grid(row=4,column=2)
Buttonsubtract=Button(root,text="-",command=lambda:click('-'),width=button_width,height=button_height,bg=button_colour,font=button_font).grid(row=3,column=3)
Buttonmultiply=Button(root,text="*",command=lambda:click('*'),width=button_width,height=button_height,bg=button_colour,font=button_font).grid(row=2,column=3)
Buttondivision=Button(root,text="/",command=lambda:click('/'),width=button_width,height=button_height,font=button_font,bg=button_colour).grid(row=1,column=3)
Buttondot=Button(root,text=".",command=lambda:click('.'),width=button_width,height=button_height,bg=button_colour,font=button_font).grid(row=4,column=0)
Buttonclear=Button(root,text="Clear",command=clear,width=10,height=button_height,bg=button_colour,font=button_font).grid(row=5,column=0,columnspan=2,ipadx=4)
Buttonx=Button(root,text='\u2190',command=back,width=10,height=button_height,bg=button_colour,font=button_font).grid(row=5,column=2,columnspan=2,ipadx=5)
root.bind('<Return>',equal)
root.bind('<BackSpace>',back)
root.bind('<Delete>',clear)
root.mainloop()