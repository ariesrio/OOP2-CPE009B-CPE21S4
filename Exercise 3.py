from tkinter import*
class MyWindow:
    def __init__(self,win):
            self.Label1 = Label(win,fg="Red", text= "Calculator")
            self.Label1.place(x=150, y=50)


            self.Label2 = Label(win, fg="Green", text="Number 1")
            self.Label2.place(x= 50, y=80)


            self.Label3 = Label(win, fg="Blue", text="Number 2")
            self.Label3.place(x=50, y=120)

            self.Label4 = Label(win, fg="Blue", text="Result: ")
            self.Label4.place(x=50, y=160)

            self.Button1 = Button(win, fg="Black", text="Add",  command = self.add)
            self.Button1.place(x=90, y=200)

            self.Button2 = Button(win, fg="Black", text="Subtract", command=self.sub)
            self.Button2.place(x=80, y=240)

            self.Button2 = Button(win, fg="Black", text="Multiply", command=self.mul)
            self.Button2.place(x=160, y=200)

            self.Button2 = Button(win, fg="Black", text="Divide", command=self.div)
            self.Button2.place(x=170, y=240)

            self.Entry1 = Entry(win, bd=5)
            self.Entry1.place(x=150, y=80)

            self.Entry2 = Entry(win, bd=5)
            self.Entry2.place(x=150, y=120)

            self.Entry3 = Entry(win, bd=5)
            self.Entry3.place(x=150, y=160)


    def add(self):
        self.Entry3.delete(0,'end')

        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, int(result))

    def sub(self):
        self.Entry3.delete(0,'end')

        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, int(result))

    def mul(self):
        self.Entry3.delete(0,'end')

        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, int(result))
    def div(self):
        self.Entry3.delete(0,'end')

        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, int(result))

window=Tk()
Mywin = MyWindow(window)
window.geometry("400x300+10+10")
window.title("Standard Calculator")
window.mainloop()