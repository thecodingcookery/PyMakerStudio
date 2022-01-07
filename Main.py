from tkinter import *

App = Tk()

App.title("PyMaker Studio")

canvas = Canvas(App, width=1200, height=800)

welcomeText = Label(App, text="Welcome to PyMaker Studio")
newProjectButton = Button(App, text="New Project")


welcomeText.pack()
newProjectButton.pack()
canvas.pack()
App.mainloop()