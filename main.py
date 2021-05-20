from tkinter import *


window = Tk()
window.geometry("450x200")
window.config(bg='purple')
window.resizable(height=False, width=False)
window.title("Calculating area of a circle")
class Circle:
    result=StringVar()
    def __init__(self, root):
        self.label1 = Label(root, text="Enter number :")
        self.label1.place(x=20, y=30)
        self.label2 = Label(root, text="Your Answer is:")
        self.label2.place(x=20, y=60)

        # entry boxes
        self.entry1 = Entry(root, bg='light blue', fg='black')
        self.entry1.place(x=200, y=30, width=100)
        self.entry2 = Label(root, bg='light blue', text="", textvariable=self.result, fg='black')
        self.entry2.place(x=200, y=60, width=100)

        # calculate button
        self.button = Button(root, text="Calculate area", fg='black', border=4, bg="light blue", command=self.area)
        self.button.place(x=320, y=40 )
    def area(self):
        answer1=int(self.entry1.get())*int(self.entry1.get())*3.14
        self.result.set(answer1)
obj_circle=Circle(window)
window.mainloop()

