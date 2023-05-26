import tkinter as tk
from render import raw_img
from PIL import ImageTk
root = tk.Tk()
try:    
    def child_window():
        child = tk.Tk()
        child.title("Child Window")
        child.geometry("600x600")
        root.destroy()
        tk_image = ImageTk.PhotoImage(raw_img,master=child) # type: ignore
        lb = tk.Label(child,image=tk_image)
        lb.pack(side = "top", fill = "both", expand =1) 
        c_button = tk.Button(child, text="Close Window",command=child.destroy)
        c_button.pack(side='bottom')
        child.mainloop()

    def mainwindow():
        root.title("Main Window")
        root.geometry("600x600")
        button = tk.Button(root, text="Click to Open a New Window!",command=child_window)
        button.pack(side='top')
        root.mainloop()

    mainwindow()
except Exception as e:
    print("Oops! Something went wrong!")
    print(e)


