"""
File allowing to test lines codes. Will be deleted after.
"""

from tkinter import Button, Tk, PhotoImage
fenetre = Tk()
def photo():
    global bouton
    global name
    bouton.config(image=image, text=name)
image = PhotoImage(file="./Image/cercle.png")
name = "a1"
bouton = Button(fenetre, command=photo)
bouton.pack()
fenetre.mainloop()
