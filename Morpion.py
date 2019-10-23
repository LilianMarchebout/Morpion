"""
Title : Morpion
Owner : Lilian
Contributor : None
Started : 09/30/19
Finished : mm/dd/yy
"""

## Dimension: 720x720

##Prochaine(s) étape(s):
    # Problème : Actionne pas les boutons 
    # Message d'avertissement
    # Définition des lignes gagnantes
    # Fin




##IMPORTATION
import sys
if sys.version_info[0] < 3:
    from Tkinter import Button, Tk, PhotoImage
else:
    from tkinter import Button, Tk, PhotoImage  #Interface tactile

from time import sleep #Permet de faire attendre le programme notamment pour mettre en pause




##VARIABLE
#Dictionnaire avec comme clef le nom de la case, et comme valeur une liste avec l'appartenance à un joueur, le nombre de points, l'abscisse, l'ordonnée, le numéro de la case
def files():
    """
    Fichier pour inscrire les éléments du dictionnaire
    """
    folder = open("element_dic.txt", "w")
    folder.write("")
    folder.close()
    folder = open("element_dic.txt", "a")
    for nameCase in case.keys():
        folder.write(nameCase + " = " +str(case[nameCase]) + "\n")
    folder.close()
case ={str(chr(utf)+str(number)):[False, 0, (number-1)*240, ("ZABC".index(chr(utf))-1)*240, int(("A0A1A2A3B1B2B3C1C2C3".index(chr(utf)+str(number)))/2)] for utf in range(65, 68) for number in range(1, 4)}
"""
Case:
    {'A1': [False, 0, 0, 0, 1],
    'A2': [False, 0, 240, 0, 2],
    'A3': [False, 0, 480, 0, 3],
    'B1': [False, 0, 0, 240, 4], 
    'B2': [False, 0, 240, 240, 5], 
    'B3': [False, 0, 480, 240, 6], 
    'C1': [False, 0, 0, 480, 7], 
    'C2': [False, 0, 240, 480, 8], 
    'C3': [False, 0, 480, 480, 9]}
"""
files()


#Variable permettant de déterminer quel joueur joue 
player = 0


#Liste pour les boutons
buttons = []




##FONCTION

def gridd():
    """
    Crée la grille avec l'interface tkinter et crée les boutons
    """
    global window
    window.geometry("720x720") #Dimension de l'interface
    default = PhotoImage(file='./Image/default.png')



    #Boutons:
    #Le x=0 est le bord gauche de la fenetre
    #Le y=0 est le bord haut de la fenetre
    #La position est la position du coin en haut à gauche du bouton

    # Création des boutons
    global intermediateVariable
    intermediateVariable = 0
    for nameCase in case.keys():
        newbutton = Button(window, image = default, name = str(nameCase).lower(), text=nameCase, height = 240, width = 240) #Définition du bouton
        newbutton.pack()
        buttons.append(newbutton) #Ajouter à la liste
        newbutton.config(command = intermediateFunction(nameCase))#Commande du bouton
        substitute = case[nameCase] 
        newbutton.place(x= substitute[2], y= substitute[3]) #Placement du bouton
        print(newbutton._name)
    intermediateVariable = 1
    global player
    player = 0



def intermediateFunction(name):
    """
    Sert à que le bouton ne lance pas la commande lors de sa définition.
    """
    global player
    global intermediateVariable
    if intermediateVariable == 1:
        game(name)



def game(name):
    """
    Quand la boutton est actionné :
        - Met la case en True
        - Met les points suivant le joueur (les points permettent de définir le gagnant)
        - Met la case en croix ou en cercle selon le joueur
    """
    
    #Variable Image
    cross = PhotoImage(file='./Image/croix.png')
    circle = PhotoImage(file='./Image/cercle.png')
    
    #Définition du joueur qui joue
    global player
    print(player)
    player += 1 
    player %= 2
    
    #Pour chaque clef du dictionnaire
    for nameCase in case.keys():
        if str(nameCase) == name: 
            substitute = case[name]
            if substitute[0] == True: #Si case déjà prise
                player -= 1 #Revient au joueur initial
                break
            else:
                substitute[0] = True #Case prise
                if player == 0:
                    substitute[1] = 1 #J2 points
                    files()
                    buttons[substitute[4]-1].config(image= cross) #Met la croix
                if player == 1:
                    substitute[1] = 10#J1 points
                    files()
                    buttons[substitute[4]-1].config(image= circle) #Met le cercle
                case[name] = substitute




##SCRIPT
window = Tk() #Ouverture de l'interface et définition de la fenêtre
gridd()
window.mainloop() #Fermeture de l'interface


##PAUSE
#Permet au programme de ne pas se fermer après exécution
while 1:
    sleep(10)
