#Mathieu brodard, Mathieu vilmot, Mohamed Latreche, Sailan Sivakumar
import pyxel
import time

''' Ajout : Bouton options foncitonnel (on peut modifier la lumière)
            Essai de ennemis plus effrayant (le crewmate blanc a été éjecté pour un design faisant plus peur)
            MàJ des bots: il vont a une vitesse constante non dépendante de la distance entre lui et le joueur (vitesse des bots sot donc augmentés)
            media.pyxres : j'ai fait une musique avec des sons différent (c'était un test pour voir comment ça marche)
                         + si vous allez dans les personnage vous verrez plein de test et design (certain copier d'internet) pour des monstres.            
'''
global timer
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
Player1 = {'position':[x1,y1] , 'Vitesse': 2, 'Stamina': 100, 'Vue' : 2, 'Sens' : 'Droite', 'Batterie': 100}
bot2 = {'position':[x2,y2] , 'Vitesse': 1 , 'Sens' : 'Droite'}
bot1= {'position':[x3,y3] , 'Vitesse': 0.5 , 'Sens' : 'Droite'}
start=0
timer=0
timer2=0

    
def deplacement1():
    global y1,x1,Player1
#Déplacement haut,bas,gauche,droite avec detections de sens droite/gauche
    if y1+15<319:
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            y1=y1+Player1['Vitesse']
    if x1+13<639 :   
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            x1=x1+Player1['Vitesse']
            Player1['Sens']='Droite'
    if x1+1>0 :
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
            x1=x1-Player1['Vitesse']
            Player1['Sens']='Gauche'
    if y1>0 :
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z):
            y1=y1-Player1['Vitesse']
            
#Ennemis qui suit le joueur avec detection de sens
def ai2():
    global x2,y2,x1,y1,timer
    if x1-x2 >= 0:
        x2=x2+1*bot2['Vitesse']
    if x1-x2 <= 0:
        x2=x2-1*bot2['Vitesse']
    if y1-y2 >= 0:
        y2=y2+1*bot2['Vitesse']
    if y1-y2 <= 0:
        y2=y2-1*bot2['Vitesse']
#fait de changer x ticks de design (essai et non final)
    timer=timer+1
    if timer>3:
        timer=0
    if timer ==1:
        bot2['Sens']='Droite'
    if timer ==3:
        bot2['Sens']='Gauche'
        
def ai1():
    global x3,y3
    if x1-x3 >= 0:
        bot1['Sens']='Droite'
        x3=x3+1*bot1['Vitesse']
    if x1-x3 <= 0:
        bot1['Sens']='Gauche'
        x3=x3-1*bot1['Vitesse']
    if y1-y3 >= 0:
        y3=y3+1*bot1['Vitesse']
    if y1-y3 <= 0:
        y3=y3-1*bot1['Vitesse']

#Lumière autour du joueur par rapport à la vue
def flash():
    global x1,y1
    pyxel.circ(x1+8,y1+8,Player1['Vue'],5)
    pyxel.circ(x1+8,y1+8,Player1['Vue']-8,12)
    pyxel.circ(x1+8,y1+8,Player1['Vue']-16,6)




#Diminnue la Visibilité en fonction de la Batterie 
def Batterie(): 
    if Player1['Batterie']>0:
        Player1['Batterie']=Player1['Batterie']-0.01
    if Player1['Batterie']<=100:
        Player1['Vue']=60
    if Player1['Batterie']<=80:
        Player1['Vue']=55
    if Player1['Batterie']<=60:
        Player1['Vue']=45
    if Player1['Batterie']<=40:
        Player1['Vue']=35
    if Player1['Batterie']<=20:
        Player1['Vue']=20
    if Player1['Batterie']<=1:
        Player1['Batterie']=2
    if pyxel.btn(pyxel.KEY_B):
        Player1['Batterie']=100

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
#Stamina ne passe pas 0%
    if  Player1['Stamina'] <= 0 :
        Player1['Stamina']= Player1['Stamina']+2        
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
#Si la souris est sur 'Options' : afficher les même flèche et va dans un autre menu si clicks
    if (x4>=120 and x4<=160) and (y4>=78 and y4<=87):
        pyxel.blt(110,79,2,0,1,6,8,0)
        pyxel.blt(160,79,2,8,1,6,8,0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            start=-1
#Pareil qu'au dessus avec le bouton 'Quit Game' et le click pour quitter
    if (x4>=120 and x4<=160) and (y4>=118 and y4<=127):
        pyxel.blt(110,119,2,0,1,6,8,0)
        pyxel.blt(160,119,2,8,1,6,8,0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.quit()

#Le menu des Options avec la Vue modifiable
def options():
    global start,Player1
    pyxel.cls(0)
    pyxel.text(120,120,str("Return"),7)
#Bouton pour retruner au menu principal
    if (x4>=120 and x4<=160) and (y4>=118 and y4<=127):
        pyxel.blt(110,119,2,0,1,6,8,0)
        pyxel.blt(160,119,2,8,1,6,8,0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            start=0
#Boutons permettant de changer la Vue du personnage
    pyxel.text(80,40,str("Lumiere : Petite   Moyenne   Grande"),7)
    if (x4>=120 and x4<=142) and (y4>=38 and y4<=47) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        Player1["Vue"]=25
    if (x4>=156 and x4<=182) and (y4>=38 and y4<=47) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        Player1["Vue"]=35
    if (x4>=196 and x4<=218) and (y4>=38 and y4<=47) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        Player1["Vue"]=45
#montrer la vue selectionner en soulignant celle selectionnée
    if Player1["Vue"]==25:
        pyxel.line(120,48,142,48,7)
    elif Player1["Vue"]==35:
        pyxel.line(156,48,182,48,7)
    else:
        pyxel.line(196,48,218,48,7)

    
class App:
    def __init__(self):
#Changement du titre du jeu (Lmao j'ai pas d'idée)
        global start
        pyxel.init(640,320 , title="Jeu d'horreur de la meilleur team d'horreur du jeu vidéo")
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
            Batterie()
#Si la partie n'est pas démarrée
        elif start==0:
            menu()
            curseur()
#Si on est dans le menu des options
        elif start==-1:
            options()
            curseur()



    def draw(self):
        global start
#Si la partie est démarrée
        if start==1:
            pyxel.cls(0)
            pyxel.blt(0,0,0,0,0,640,320,0)
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
            
#Batterie
            Bat=(str('Batterie : '))+(str(Player1['Batterie']))
            pyxel.text(0,20,Bat,2)        
#Si le joueur regarde a droite : sprite a droite et inversement
            if ((-x3+x1) < Player1['Vue'] and (x3-x1) < Player1['Vue']) and ((-y3+y1) < Player1['Vue'] and (y3-y1) < Player1['Vue'])  :
                if bot1['Sens']=='Droite':
                    pyxel.blt(x3,y3,1,32,0,16,16,0)
                if bot1['Sens']=='Gauche':
                    pyxel.blt(x3,y3,1,32,16,16,16,0)
                    
#Position du curseur
            XX=(str('X : '))+(str(x4))
            YY=(str('Y : '))+(str(y4))
            pyxel.text(0,0,XX,2)
            pyxel.text(30,0,YY,2)
            
#Stamina en haut a gauche (si elle est faible : elle devient rouge)
            Stam=(str('Stamina : '))+(str(Player1['Stamina']))
            if Player1['Stamina'] >= 25 :
                pyxel.text(0,10,Stam,2)
            else:
                pyxel.text(0,10,Stam,8)
                
#Curseur Visible pendant le jeu avec un point et dans le menu principal et les options avec un curseur
            pyxel.pset(x4,y4,14)
        if start==0 or start==-1 :
            pyxel.blt(x4,y4,2,48,0,6,6,0)
        
        
        
        

App()