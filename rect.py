import tkinter as tk


class myapps:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("Rect")
        self.root.geometry("640x480")
        self.root.configure(background="black")
        self.canvas=tk.Canvas(background="black",width=640,height=480)
        self.canvas.pack(padx=1,pady=1)
        c=self.canvas
        for a in range(0,640,40):
            for b in range(0,480,20):
                bb=(b//20 & 1)
                
                c.create_rectangle(a+(bb*20),b,a+20+(20*bb),b+20,fill="white")
        
        






root=tk.Tk()
apps=myapps(root)
root.mainloop()