# Activity-1
# from tkinter import*
# from PIL import Image, ImageTk

# root=Tk()
# root.title("Image")
# root.geometry("500x500")

# upload=Image.open("flo.jpg")

# image=ImageTk.PhotoImage(upload)

# label=Label(root, image=image, height=699, width=466)
# label.place(x=20,y=10)
# label2=Label(root, text="This is a picture of a flower.")
# label2.place(x=20,y=650)

# root.mainloop()



#Activity-2

# from tkinter import *
# from tkinter import messagebox

# root=Tk()
# root.geometry("300x300")

# def msg():
#     messagebox.showwarning("Alert","Stop! Virus found")

# button=Button(root, text="Scan for virus", command=msg)
# button.place(x=50,y=80)

# root.mainloop()



#Activity-3

from tkinter import *

root=Tk()
root.geometry("300x300")
root.title("title")

# def topwin():
#     top=Toplevel()
#     top.geometry("200x100")
#     top.title("top level window")
#     l1=Label(top, text="This is the top level window")
#     l1.pack()
    
#     top.mainloop()
    
# l=Label(root, text="This is the root window")
# btn=Button(root, text="Click here to open another window", command=topwin)


def key():
    l2=Label(text="Hi there!")
    
button=Button(text="Click here", command=key)

# l.place(x=30,y=30)
# btn.place(x=30,y=50)
button.pack()

root.mainloop()