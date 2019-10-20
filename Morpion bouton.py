"""
Title : Morpion
By Lilian
Started : 09/30/19
Finished : mm/dd/yy
"""

## Dimension: 720x720

##Prochaine(s) étape(s):
    # Problème global joueur
    # Problème bouton gris
    # Message d'avertissement
    # Définition des lignes gagnantes
    # Fin




##IMPORTATION

from tkinter import * #Interface tactile

from time import sleep #Permet de faire attendre le programme notamment pour mettre en pause




##FONCTION

def grid():
    """
    Crée la grille avec l'interface tkinter et crée les boutons
    """
    
    f = Tk() #Ouverture de l'interface et définition de la fenêtre
    f.geometry("720x720") #Dimension de l'interface
    default = PhotoImage(file='default.png')
    
    #Boutons:
    #Le x=0 est le bord gauche de la fenetre
    #Le y=0 est le bord haut de la fenetre
    #La position est la position du coin en haut à gauche du bouton

    # Création des boutons
    for nameCase in case.keys():
        newbutton = Button(f, image = default, text=nameCase, height = 240, width = 240) #Définition du bouton
        buttons.append(newbutton) #Ajouter à la liste
        newbutton.config(command = game(nameCase)) #Commande du bouton
        substitute = case[nameCase] 
        newbutton.place(x= substitute[2], y= substitute[3]) #Placement du bouton
    f.mainloop() #Fermeture de l'interface


    
def game(name):
    """
    Quand la boutton est actionné :
        - Met la case en True
        - Met les points suivant le joueur (les points permettent de définir le gagnant)
        - Met la case en croix ou en cercle selon le joueur
    """
    
    #Variable Image
    cross = PhotoImage(file='croix.png')
    circle = PhotoImage(file='cercle.png')
    
    #Définition du joueur qui joue
    global player
    print(player)
    player += 1 
    player %= 2
    
    #Pour chaque clef du dictionnaire
    for key in case.keys():
        if str(key) == name: 
            substitute = case[name]
            if substitute[0] == True: #Si case déjà prise
                player -= 1 #Revient au joueur initial
                break
            else:
                substitute[0] = True #Case prise
                if player == 0:
                    substitute[1] = 1 #J2 points
                    buttons[substitute[4]-1].config(image= cross) #Met la croix
                if player == 1:
                    substitute[1] = 10#J1 points
                    buttons[substitute[4]-1].config(image= circle) #Met le cercle
                case[name] = substitute




##VARIABLE
#Dictionnaire avec comme clef le nom de la case, et comme valeur une liste avec l'appartenance à un joueur, le nombre de points, l'abscisse, l'ordonnée, le numéro de la case
case ={str(chr(c)+str(n)):[False, 0, (n-1)*240, ("ZABC".index(chr(c))-1)*240, int(("A0A1A2A3B1B2B3C1C2C3".index(chr(c)+str(n)))/2)] for c in range(65, 68) for n in range(1, 4)}
"""
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
#Fichier pour inscrire les éléments du dictionnaire
folder = open("test.txt", "w")
folder.write(str(case) + "\n")
folder.close()


#Variable permettant de déterminer quel joueur joue 
player = 0


#Liste pour les boutons
buttons = []




##SCRIPT
grid()




##PAUSE
#Permet au programme de ne pas se fermer après exécution
while 1:
    sleep(10)
