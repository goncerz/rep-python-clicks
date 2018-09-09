from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.btnClicks = 0
        self.createWidget()

    def createWidget(self):
        self.btn = Button(self)
        self.btn["text"] = "Liczba klikniec: " + str(self.btnClicks)
        self.btn["command"] = self.updCount
        self.btn.grid()

    def updCount(self):
        self.btnClicks += 1
        self.btn["text"] = "Liczba klikniec: " + str(self.btnClicks)

root = Tk()
root.title("Licznik klikniec")
root.geometry("300x100")

app = Application(root)

root.mainloop()
