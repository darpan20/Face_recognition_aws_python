from tkinter import *



def Recognition(c,c1,var1,root):
    from Attendance_upload import xmain
   
    print(c.get())
    
    print(c1.get())
    print(var1.get())
    root.destroy()
    xmain()
    
def app(): 
    from functools import partial
    root = Tk()
    root.geometry('800x600')
    root.title("Main Menu")
    
    label_0 = Label(root, text="ATTENDANCE SYSTEM",width=20,font=("bold",20))
    label_0.place(x=100,y=33)
    
    
    
    
    
    label_4 = Label(root, text="Select Year :",width=20,font=("bold", 10))
    label_4.place(x=5,y=250)
    
    list1 = ['1st Year','2nd Year','3rd Year','4th Year'];
    c=StringVar()
    droplist=OptionMenu(root,c, *list1)
    droplist.config(width=15)
    c.set('Year') 
    droplist.place(x=250,y=250)
    
    label_5 = Label(root, text="SELECT BRANCH :",width=20,font=("bold", 10))
    label_5.place(x=5,y=350)
    list2 = ['CS','EC','EE','ME','CE','IT'];
    c1=StringVar()
    droplist=OptionMenu(root,c1, *list2)
    droplist.config(width=15)
    c1.set('Branch') 
    droplist.place(x=250,y=350)
    
    
    label_4 = Label(root, text="Section :",width=20,font=("bold", 10))
    label_4.place(x=5,y=450)
    var1 = IntVar()
    Radiobutton(root, text="A",padx = 5, variable=var1, value=1).place(x=235,y=450)
    Radiobutton(root, text="B",padx = 5, variable=var1, value=2).place(x=285,y=450)
    Radiobutton(root, text="C",padx = 5, variable=var1, value=3).place(x=335,y=450)
    Radiobutton(root, text="D",padx = 5, variable=var1, value=4).place(x=385,y=450)
    Radiobutton(root, text="E",padx = 5, variable=var1, value=5).place(x=435,y=450)
    Radiobutton(root, text="F",padx = 5, variable=var1, value=6).place(x=485,y=450)
    Button(root, text='Submit',width=20,bg='brown',fg='white',command=partial(Recognition,c,c1,var1,root)).place(x=50,y=550)
    root.mainloop()
if __name__=='__main__':
 app()    