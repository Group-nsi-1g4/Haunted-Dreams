#Mathieu brodard, Mathieu vilmot, Mohamed Latreche, Sailan Sivakumar
import pyxel
import time

''' Ajout : Menu avec jouer et quitter fonctionnel (pas encore option car il faut voir se qu'on fait) Tab pour l'ouvrir (Les deux flèches en au a gauche du clavier)
            Le sprite changeant avce le sens : ajout de 'sens' dans les dictionnaires
            Quelque changement dans media.pyxres : page 2 pour les menus et page 1 avec les différent sens des personnages
'''
global start
global Player1
global Player2
global x1
global y1
global x2
global y2
global x3
global y3
global x4
global y4
x1,y1=0,57
x2,y2=50,57
x3,y3=60,57
x4,y4=100,100
#Dictionnaires des ennnemis et joueurs
Player1 = {'position':[x1,y1] , 'Vitesse': 2, 'Stamina': 100, 'Vue' : 25, 'Sens' : 'Droite'}
bot2 = {'position':[x2,y2] , 'Vitesse': 0.04 , 'Sens' : 'Droite'}
bot1= {'position':[x3,y3] , 'Vitesse': 0.02 , 'Sens' : 'Droite'}
start=0




def deplacement1():
    global y1,x1,Player1
#Déplacement haut,bas,gauche,droite avec detections de sens droite/gauche
    if y1+15<159:
        if pyxel.btn(pyxel.KEY_DOWN):
            y1=y1+Player1['Vitesse']
    if x1+13<319:   
        if pyxel.btn(pyxel.KEY_RIGHT):
            x1=x1+Player1['Vitesse']
            Player1['Sens']='Droite'
    if x1+1>0 :
        if pyxel.btn(pyxel.KEY_LEFT):
            x1=x1-Player1['Vitesse']
            Player1['Sens']='Gauche'
    if y1>0 :
        if pyxel.btn(pyxel.KEY_UP):
            y1=y1-Player1['Vitesse']

#Ennemis qui suit le joueur avec detection de sens
def ai2():
    global x2,y2,x1,y1
    x2=x2+((x1-x2)*bot2['Vitesse'])
    y2=y2+((y1-y2)*bot2['Vitesse'])
    if x1-x2 >= 0:
        bot2['Sens']='Droite'
    if x1-x2 <= 0:
        bot2['Sens']='Gauche'
def ai1():
    global x3,y3
    x3=x3+((x1-x3)*bot1['Vitesse'])
    y3=y3+((y1-y3)*bot1['Vitesse'])
    if x1-x3 >= 0:
        bot1['Sens']='Droite'
    if x1-x3 <= 0:
        bot1['Sens']='Gauche'

#Lumière autour du joueur par rapport à la vue
def flash():
    global x1,y1
    pyxel.circ(x1+8,y1+8,Player1['Vue'],5)
    pyxel.circ(x1+8,y1+8,Player1['Vue']-8,12)
    pyxel.circ(x1+8,y1+8,Player1['Vue']-16,6)

#Position du curseur 
def curseur():
    global x4,y4
    x4=pyxel.mouse_x
    y4=pyxel.mouse_y

#Course et système de Stamina
def Course():
    global Player1 
    if pyxel.btn(pyxel.KEY_SHIFT) and Player1['Stamina'] >= 0:
        Player1['Vitesse']=4
        Player1['Stamina']= Player1['Stamina']-2

    else:
#Si le joueur a peu de Stamina : sa vitesse est réduite temporairement
        if Player1['Stamina']<=25:
            Player1['Vitesse']=1
        else:
            Player1['Vitesse']=2
#Si le joueur essai toujours de courrir, sa stamina ne reviens pas (ajout de stress ++)
        if not pyxel.btn(pyxel.KEY_SHIFT):
            Player1['Stamina']= Player1['Stamina']+0.5
#Stamina ne dépasse pas 100%
    if  Player1['Stamina'] >= 101 :
        Player1['Stamina']= Player1['Stamina']-1

#Le Menu principale dans sont intégralité : Jouer et Quitter pour l'instant
def menu():
    global x4,y4,start,x1,x2,x3,y1,y2,y3,bot1,bot2,Player1
    pyxel.cls(0)
    pyxel.text(120,40,str("Start Game"),7)
    pyxel.text(120,80,str("Options"),7)
    pyxel.text(120,120,str("Quit Game"),7)
#Si la souris est sur 'Start Game' : afficher les flèches et detections des clicks
    if (x4>=120 and x4<=160) and (y4>=38 and y4<=47):
        pyxel.blt(110,39,2,0,1,6,8,0)
        pyxel.blt(160,39,2,8,1,6,8,0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            start=1
#Pareil qu'au dessus avec le bouton 'Quit Game'
    if (x4>=120 and x4<=160) and (y4>=118 and y4<=127):
        pyxel.blt(110,119,2,0,1,6,8,0)
        pyxel.blt(160,119,2,8,1,6,8,0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.quit()


class App:
    def __init__(self):
#Changement du titre du jeu (Lmao j'ai pas d'idée)
        global start
        pyxel.init(320,160 , title="Jeu d'horreur de la meilleur team d'horreur du jeu vidéo")
        pyxel.load("media.pyxres")
        pyxel.run(self.update, self.draw)



    def update(self):
        global start

#Appuier sur TAB pour ouvrir le menu ET stopper le jeu
        if pyxel.btnp(pyxel.KEY_TAB):
            start=0
#Si la partie est démarrée
        if start==1:
            deplacement1() 
            ai2()
            ai1()
            curseur()
            Course()

#Si la partie n'est pas démarrée
        elif start==0:
            menu()
            curseur()



    def draw(self):
        global start

#Si la partie est démarrée
        if start==1:
            pyxel.cls(0)
            pyxel.blt(0,0,0,0,0,320,320,0)
            flash()
            if Player1['Sens']=='Droite':
                pyxel.blt(x1,y1,1,0,0,16,16,0)
            elif Player1['Sens']=='Gauche':
                pyxel.blt(x1,y1,1,0,16,16,16,0)

#Si l'ennemis est dans le flash : il est visible
# + Si il regarde a droite : sprite a droite et inversement
            if ((-x2+x1) < Player1['Vue'] and (x2-x1) < Player1['Vue']) and ((-y2+y1) < Player1['Vue'] and (y2-y1) < Player1['Vue'])  :
                if bot2['Sens']=='Droite':
                    pyxel.blt(x2,y2,1,16,0,16,16,0)
                elif bot2['Sens']=='Gauche':
                    pyxel.blt(x2,y2,1,16,16,16,16,0)

#Si le joueur regarde a droite : sprite a droite et inversement
            if ((-x3+x1) < Player1['Vue'] and (x3-x1) < Player1['Vue']) and ((-y3+y1) < Player1['Vue'] and (y3-y1) < Player1['Vue'])  :
                if bot1['Sens']=='Droite':
                    pyxel.blt(x3,y3,1,32,0,16,16,0)
                if bot1['Sens']=='Gauche':
                    pyxel.blt(x3,y3,1,32,16,16,16,0)

#Position du curseur
            pyxel.text(0,0,str(x4),14)
            pyxel.text(15,0,str(y4),14)

#Stamina en haut a gauche (si elle est faible : elle devient rouge)
            if Player1['Stamina'] >= 25 :
                pyxel.text(0,10,str(Player1['Stamina']),6)
            else:
                pyxel.text(0,10,str(Player1['Stamina']),8)

#Curseur Visible
            pyxel.pset(x4,y4,14)
        if start==0:
            pyxel.blt(x4,y4,2,48,0,6,6,0)




App()