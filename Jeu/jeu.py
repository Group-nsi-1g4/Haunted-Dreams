#Mathieu brodard, Mathieu vilmot, Mohamed Latreche, Sailan Sivakumar
import pyxel
import time

#Ajout: Flash fonctionnel sur les ennemis uniquement
#       Stamina et course (Shift pour courir)

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
Player1 = {'position':[x1,y1] , 'Vitesse': 2, 'Stamina': 100, 'Vue' : 25}
bot2 = {'position':[x2,y2] , 'Vitesse': 0.04}
bot1= {'position':[x3,y3] , 'Vitesse': 0.02}



    
def deplacement1():
    global y1,x1
#Déplacement haut,bas,gauche,droite
    if y1+15<159:
        if pyxel.btn(pyxel.KEY_DOWN):
            y1=y1+Player1['Vitesse']
    if x1+13<319:   
        if pyxel.btn(pyxel.KEY_RIGHT):
            x1=x1+Player1['Vitesse']
    if x1+1>0 :
        if pyxel.btn(pyxel.KEY_LEFT):
            x1=x1-Player1['Vitesse']
    if y1>0 :
        if pyxel.btn(pyxel.KEY_UP):
            y1=y1-Player1['Vitesse']
            
#Ennemis qui suit le joueur
def ai2():
    global x2,y2,Vue,x1,y1
    x2=x2+((x1-x2)*bot2['Vitesse'])
    y2=y2+((y1-y2)*bot2['Vitesse'])
def ai1():
    global x3,y3
    x3=x3+((x1-x3)*bot1['Vitesse'])
    y3=y3+((y1-y3)*bot1['Vitesse'])

#Lumière autour du joueur
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
        Player1['Stamina']= Player1['Stamina']+0.5
#Stamina ne dépasse pas 100%
    if  Player1['Stamina'] >= 101 :
        Player1['Stamina']= Player1['Stamina']-1


class App:
    def __init__(self):
        pyxel.init(320,160 , title="Projet jeu Pyxel")
        pyxel.load("media.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        deplacement1() 
        ai2()
        ai1()
        curseur()
        Course()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0,0,0,0,0,320,320,0)
        flash()
        pyxel.blt(x1,y1,1,0,0,16,16,0)
#Si l'ennemis est dans le flash : il est visible
        if ((-x2+x1) < Player1['Vue'] and (x2-x1) < Player1['Vue']) and ((-y2+y1) < Player1['Vue'] and (y2-y1) < Player1['Vue'])  :
            pyxel.blt(x2,y2,1,16,0,16,16,0)
        if ((-x3+x1) < Player1['Vue'] and (x3-x1) < Player1['Vue']) and ((-y3+y1) < Player1['Vue'] and (y3-y1) < Player1['Vue'])  :
            pyxel.blt(x3,y3,1,32,0,16,16,0)
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
        
        

App()