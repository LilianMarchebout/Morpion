"""
File allowing to test lines codes.
"""


from tkinter import Button, Tk, PhotoImage
fenetre = Tk()
image = PhotoImage(file="./Image/cercle.png")
bouton = Button(fenetre, command=photo("a1"))
bouton.pack()
def photo(name):
    global bouton
    bouton.config(image=image, name= name)
fenetre.mainloop()
