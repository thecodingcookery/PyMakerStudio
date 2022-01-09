from tkinter import *

App = Tk()

App.title("PyMaker Studio")

canvas = Canvas(App, width=1200, height=800)

welcomeText = Label(App, text="Welcome to PyMaker Studio", font="Helvetica 18 bold")
space1 = Label(App)
newProjectButton = Button(App, text="New Project", width=20)


welcomeText.pack()
space1.pack()
newProjectButton.pack()
canvas.pack()
App.mainloop()