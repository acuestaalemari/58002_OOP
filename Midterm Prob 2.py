from tkinter import *
class MyWindow:
    def __init__(self,win):
        self.lbl1 = Label(win, text='Given Name:', font=('Verdana', 12), fg='red', anchor='center')
        self.lbl1.place(x=150,y=100)
        self.lbl2 = Label(win, text='Middle Name:', font=('Verdana', 12), fg='red', anchor='center')
        self.lbl2.place(x=150,y=130)
        self.lbl3 = Label(win, text='Last Name:', font=('Verdana', 12), fg='red', anchor='center')
        self.lbl3.place(x=150,y=160)
        self.lbl4 = Label(win, text='Full Name:', font=('Verdana', 12), fg='red', anchor='center')
        self.lbl4.place(x=250, y=70)
        

        self.txt1 = Entry(win,bd=1)
        self.txt1.place(x=350,y=100)

        self.txt2 = Entry(win,bd=1)
        self.txt2.place(x=350,y=130)

        self.txt3 = Entry(win,bd=1)
        self.txt3.place(x=350,y=160)

        self.txt4 = Entry(win,bd=3)
        self.txt4 = Entry(width= 30)
        self.txt4.place(x=350,y=200)
        self.btnshow = Button(win,text="Show Full Name")
        self.btnshow.place (x= 250,y=225)
        self.btnshow.bind('<Button-1>',self.show)

    def show(self, show):
        self.txt4.delete(0, 'end')
        num1 = (self.txt1.get())
        num2 = (self.txt2.get())
        num3 = (self.txt3.get())
        result = num1 + " " + num2 + " " + num3
        self.txt4.insert(END,str(result))

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Full Name")
window.mainloop()