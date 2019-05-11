from tkinter import *





def close_window(entry_1,entry_2,root):
    from Detection_main import surv_detect
    import boto3
    from winsound import PlaySound,SND_ASYNC
    import os
    client = boto3.client('cognito-idp')
    print(entry_1.get())
    print(entry_2.get())
    try:
        response = client.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': entry_1.get(),
            'PASSWORD': entry_2.get()      
        },
        ClientId='p051gnct3tpanukb4vn58nq7o'
        )   
        
        root.destroy()
        surv_detect()
    except Exception as e:
        z=str(e)
        l="Could not connect to the endpoint URL: \"https://cognito-idp.ap-south-1.amazonaws.com/\""
        if z==l:
         PlaySound(None,SND_ASYNC)
         play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"nerrta.wav"),SND_ASYNC)
         play()    
         print("Network Error!! Try Again!!")
        else:
         PlaySound(None,SND_ASYNC)
         play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"wc.wav"),SND_ASYNC)
         play()
         print("Wrong Credentials!! Try Again!!")
        root.destroy()
        
        
        initiate_surv()
    
    
def initiate_surv(): 
    from functools import partial
    root = Tk()
    root.geometry('800x600')
    root.title("Login Page")
    
    label_0 = Label(root, text="SURVEILLANCE LOGIN",width=20,font=("bold", 20))
    label_0.place(x=220,y=33)
    
    
    label_1 = Label(root, text="Email",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)
    
    entry_1 = Entry(root,width=32)
    entry_1.place(x=240,y=130)
    
    label_2 = Label(root, text="Password",width=20,font=("bold", 10))
    label_2.place(x=68,y=180)
    
    entry_2 = Entry(root,width=32)
    entry_2.place(x=240,y=180)
    
    
    
    Button(root, text='Submit',width=20,bg='brown',fg='white',command=partial(close_window,entry_1,entry_2,root)).place(x=180,y=380)
    
    root.mainloop()
    
if __name__=='__main__':
 initiate_surv()