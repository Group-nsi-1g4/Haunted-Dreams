import pyxel                                                                    #Mathieu brodard, Mathieu vilmot, Mohamed Latreche, Sailan Sivakumar
'''
███╗░░██╗░█████╗░███╗░░░███╗░░░░░░██████╗░██╗░░░██╗░░░░░░░░░██╗███████╗██╗░░░██╗
████╗░██║██╔══██╗████╗░████║░░░░░░██╔══██╗██║░░░██║░░░░░░░░░██║██╔════╝██║░░░██║
██╔██╗██║██║░░██║██╔████╔██║░░░░░░██║░░██║██║░░░██║░░░░░░░░░██║█████╗░░██║░░░██║
██║╚████║██║░░██║██║╚██╔╝██║░░░░░░██║░░██║██║░░░██║░░░░██╗░░██║██╔══╝░░██║░░░██║
██║░╚███║╚█████╔╝██║░╚═╝░██║░░░░░░██████╔╝╚██████╔╝░░░░╚█████╔╝███████╗╚██████╔╝
╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝░░░░░░╚═════╝░░╚═════╝░░░░░░╚════╝░╚══════╝░╚═════╝░

                                                                                ░░░░░██╗░█████╗░██╗░░░██╗███████╗██╗░░░██╗██████╗░
                                                                                ░░░░░██║██╔══██╗██║░░░██║██╔════╝██║░░░██║██╔══██╗
                                                                                ░░░░░██║██║░░██║██║░░░██║█████╗░░██║░░░██║██████╔╝
                                                                                ██╗░░██║██║░░██║██║░░░██║██╔══╝░░██║░░░██║██╔══██╗
                                                                                ╚█████╔╝╚█████╔╝╚██████╔╝███████╗╚██████╔╝██║░░██║
                                                                                ░╚════╝░░╚════╝░░╚═════╝░╚══════╝░╚═════╝░╚═╝░░╚═╝
'''
Player=dict()
Player['y']=100                                                                 #Indique l'emplacement Y du Joueur
Player['x']=100                                                                 #Indique l'emplacement X du Joueur
Player['Vitesse']=2                                                             #Indique la Vitesse du Joueur
Player['Stamina']=100                                                           #Indique la Stamina du Joueur
Player['Vue']=2                                                                 #Indique la Visibilité du Joueur
Player['Sens']='Droite'                                                         #Indique Le sens du Joueur
Player['Batterie']= 100                                                         #Indique la Batterie du Joueur

def deplacement():                                                              #Déplacement Du joueur 
    global start                                                                                
    if Player['y']+15<319:                                                      #Déplacement Vers le bas 
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            Player['y']=Player['y']+Player['Vitesse']
    if Player['x']+13<639 :                                                     #Déplacement Vers la Droite et modifie le sens vers la droite    
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            Player['x']=Player['x']+Player['Vitesse']
            Player['Sens']='Droite'
    if Player['x']+1>0 :                                                        #Déplacement Vers la gauche et modifie le sens vers la gauche 
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
            Player['x']=Player['x']-Player['Vitesse']
            Player['Sens']='Gauche'
    if Player['y']>0 :                                                          #Déplacement Vers le haut 
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z):
            Player['y']=Player['y']-Player['Vitesse']
    

'''
                                                                                ██████╗░░█████╗░████████╗
                                                                                ██╔══██╗██╔══██╗╚══██╔══╝
                                                                                ██████╦╝██║░░██║░░░██║░░░
                                                                                ██╔══██╗██║░░██║░░░██║░░░
                                                                                ██████╦╝╚█████╔╝░░░██║░░░
                                                                                ╚═════╝░░╚════╝░░░░╚═╝░░░
'''
Bot1=dict()
Bot1['x']=60                                                                    #Indique l'emplacement X du Bot1
Bot1['y']=57                                                                    #Indique l'emplacement Y du Bot1
Bot1['Vitesse']=0.5                                                               #Indique la Vitesse du Bot1
Bot1['sens']= 'Droite'                                                          #Indique le Sens du Bot1



Bot2=dict()
Bot2['x']=50                                                                    #Indique l'emplacement X du Bot2
Bot2['y']=57                                                                    #Indique l'emplacement Y du Bot2
Bot2['Vitesse']=1                                                               #Indique la Vitesse du Bot2
Bot2['sens']= 'Droite'                                                          #Indique le Sens du Bot2

def ai2():                                                                      #Fait en sorte que le bot2 pourusit le joueur en fonction de sa vitesse 
    timer=0                                                                     #met le timer a 0 
    if Player['x']-Bot2['x'] >= 0:
        Bot2['x']=Bot2['x']+1*Bot2['Vitesse']
    if Player['x']-Bot2['x'] <= 0:
        Bot2['x']=Bot2['x']-1*Bot2['Vitesse']
    if Player['y']-Bot2['y'] >= 0:
        Bot2['y']=Bot2['y']+1*Bot2['Vitesse']
    if Player['y']-Bot2['y'] <= 0:
        Bot2['y']=Bot2['y']-1*Bot2['Vitesse']
    timer=timer+1                                                               #fait de changer x ticks de design (essai et non final)
    if timer>3:
        timer=0
    if timer ==1:
        Bot2['Sens']='Droite'
    if timer ==3:
        Bot2['Sens']='Gauche'
        
def ai1():                                                                      #Fait en sorte que le bot2 pourusit le joueur en fonction de sa vitesse 
    if Player['x']-Bot1['x'] >= 0:
        Bot1['Sens']='Droite'
        Bot1['x']=Bot1['x']+1*Bot1['Vitesse']
    if Player['x']-Bot1['x'] <= 0:
        Bot1['Sens']='Gauche'
        Bot1['x']=Bot1['x']-1*Bot1['Vitesse']
    if Player['y']-Bot1['y'] >= 0:
        Bot1['y']=Bot1['y']+1*Bot1['Vitesse']
    if Player['y']-Bot1['y'] <= 0:
        Bot1['y']=Bot1['y']-1*Bot1['Vitesse']



global start                                                                    #Met en place La variable Global start 
start=0                                                                         #Indique si le jeu est commencer ou non (0 pour non)



 
global Xsouris,Ysouris                                                          #Met en place la variable Global Xsouris, Ysouris 
Xsouris,Ysouris=100,100                                                         
def curseur():                                                                  #Position du curseur 
    global Xsouris,Ysouris
    Xsouris,Ysouris=100,100
    Xsouris=pyxel.mouse_x
    Ysouris=pyxel.mouse_y



    

def Course():                                                                   #Course et système de Stamina
    if pyxel.btn(pyxel.KEY_SHIFT) and Player['Stamina'] >= 0:
        Player['Vitesse']=4
        Player['Stamina']= Player['Stamina']-2
        
    else:
        if Player['Stamina']<=25:                                               #Si le joueur a peu de Stamina : sa vitesse est réduite temporairement
            Player['Vitesse']=1
        else:
            Player['Vitesse']=2
        if not pyxel.btn(pyxel.KEY_SHIFT):                                      #Si le joueur essai toujours de courrir, sa stamina ne reviens pas (ajout de stress ++)
            Player['Stamina']= Player['Stamina']+0.5
    if  Player['Stamina'] >= 101 :                                              #Stamina ne dépasse pas 100%
        Player['Stamina']= Player['Stamina']-1
    if  Player['Stamina'] <= 0 :                                                #Stamina ne passe pas 0%
        Player['Stamina']= Player['Stamina']+2  

'''
                                                                                ██╗░░░░░░█████╗░███╗░░░███╗██████╗░███████╗
                                                                                ██║░░░░░██╔══██╗████╗░████║██╔══██╗██╔════╝
                                                                                ██║░░░░░███████║██╔████╔██║██████╔╝█████╗░░
                                                                                ██║░░░░░██╔══██║██║╚██╔╝██║██╔═══╝░██╔══╝░░
                                                                                ███████╗██║░░██║██║░╚═╝░██║██║░░░░░███████╗
                                                                                ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝
'''



def Batterie():                                                                 #Diminue la luminosité de la lampe torche en fonction de la Batterie  
    if Player['Batterie']>0:
        Player['Batterie']=Player['Batterie']-0.01
    if Player['Batterie']<=100:
        Player['Vue']=60
    if Player['Batterie']<=80:
        Player['Vue']=55
    if Player['Batterie']<=60:
        Player['Vue']=45
    if Player['Batterie']<=40:
        Player['Vue']=35
    if Player['Batterie']<=20:
        Player['Vue']=20
    if Player['Batterie']<=3:
        Player['Batterie']=2
    if pyxel.btn(pyxel.KEY_B):
        Player['Batterie']=100
    if pyxel.btn(pyxel.KEY_N):
        Player['Batterie']=Player['Batterie']-10
#prototype lampe V1
def Lampe():                                                                    #Affiche une partie de la map autour du joueur en fonction de la visibilité 
    for x in range(Player['x']-75,Player['x']+75):
        for y in range(Player['y']-75,Player['y']+75):
            b=pyxel.sqrt((x-Player['x'])**2+(y-Player['y'])**2)
            if b>Player['Vue']:
                pyxel.pset(x,y,0)
            if b>=Player['Vue'] and b<Player['Vue']+4:
                pyxel.pset(x,y,10)
            if b>=Player['Vue']+4 and b<Player['Vue']+6:
                pyxel.pset(x,y,9)

'''
                                                                                ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
                                                                                ████╗░████║██╔════╝████╗░██║██║░░░██║
                                                                                ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
                                                                                ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
                                                                                ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
                                                                                ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
'''
def menu():                                                                     #Le Menu principale dans sont intégralité : Jouer et Quitter pour l'instant
    global Xsouris,Ysouris,start
    pyxel.cls(0)
    pyxel.text(120,40,str("Start Game"),7)
    pyxel.text(120,80,str("Options"),7)
    pyxel.text(120,120,str("Quit Game"),7)
    
    if (Xsouris>=120 and Xsouris<=160) and (Ysouris>=38 and Ysouris<=47):       #Si la souris est sur 'Start Game' : afficher les flèches et detections des clicks
        pyxel.blt(110,39,2,0,1,6,8,0)
        pyxel.blt(160,39,2,8,1,6,8,0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            start=1
                                                                                
    if (Xsouris>=120 and Xsouris<=160) and (Ysouris>=78 and Ysouris<=87):       #Si la souris est sur 'Options' : afficher les même flèche et va dans un autre menu si clicks
        pyxel.blt(110,79,2,0,1,6,8,0)
        pyxel.blt(160,79,2,8,1,6,8,0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            start=-1
                                                                                
    if (Xsouris>=120 and Xsouris<=160) and (Ysouris>=118 and Ysouris<=127):     #Pareil qu'au dessus avec le bouton 'Quit Game' et le click pour quitter
        pyxel.blt(110,119,2,0,1,6,8,0)
        pyxel.blt(160,119,2,8,1,6,8,0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.quit()
    
    if pyxel.btn(pyxel.KEY_E):
        start=1



def options():                                                                  #Le menu des Options avec la Vue modifiable
    global start
    pyxel.cls(0)
    pyxel.text(120,120,str("Return"),7)
    
    if (Xsouris>=120 and Xsouris<=160) and (Ysouris>=118 and Ysouris<=127):     #Bouton pour retruner au menu principal
        pyxel.blt(110,119,2,0,1,6,8,0)
        pyxel.blt(160,119,2,8,1,6,8,0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            start=0
    pyxel.text(80,40,str("Lumiere : Petite   Moyenne   Grande"),7)              #Boutons permettant de changer la Vue du personnage
    
    if (Xsouris>=120 and Xsouris<=142) and (Ysouris>=38 and Ysouris<=47) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        Player["Vue"]=25
    
    if (Xsouris>=156 and Xsouris<=182) and (Ysouris>=38 and Ysouris<=47) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        Player["Vue"]=35
    
    if (Xsouris>=196 and Xsouris<=218) and (Ysouris>=38 and Ysouris<=47) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        Player["Vue"]=45
    
    if Player["Vue"]==25:                                                       #montrer la vue selectionner en soulignant celle selectionnée
        pyxel.line(120,48,142,48,7)
    
    elif Player["Vue"]==35:
        pyxel.line(156,48,182,48,7)
    
    else:
        pyxel.line(196,48,218,48,7)
'''

                                                                                ░█████╗░██████╗░██████╗░
                                                                                ██╔══██╗██╔══██╗██╔══██╗
                                                                                ███████║██████╔╝██████╔╝
                                                                                ██╔══██║██╔═══╝░██╔═══╝░
                                                                                ██║░░██║██║░░░░░██║░░░░░
                                                                                ╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░
'''
class App:
    def __init__(self):                                                         #Initialisation du Jeu 
        pyxel.init(640,320 , title="Nom du jeu")                                #Initialisation de la résolution du jeu et de son titre
        pyxel.load("media.pyxres")                                              #charge les graphisme depuis le fichier media 
        pyxel.run(self.update, self.draw)                                       #lance l'update et le draw en continue 

    def update(self):                                                           #Repète et met a jour ce code tout les x seconde 
        '''
                                                                                ██╗░░░██╗██████╗░██████╗░░█████╗░████████╗███████╗
                                                                                ██║░░░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
                                                                                ██║░░░██║██████╔╝██║░░██║███████║░░░██║░░░█████╗░░
                                                                                ██║░░░██║██╔═══╝░██║░░██║██╔══██║░░░██║░░░██╔══╝░░
                                                                                ╚██████╔╝██║░░░░░██████╔╝██║░░██║░░░██║░░░███████╗
                                                                                ░╚═════╝░╚═╝░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
        '''

        global start
        if pyxel.btnp(pyxel.KEY_TAB):                                           #Stop le jeu et ouvre le Menu quand on appui sur tab
            start=0

        if start==1:                                                            #Si la partie est démarrée, lancement des fonction ci dessous:
            Lampe()
            deplacement() 
            ai2()
            ai1()
            curseur()
            Course()
            Batterie()

        elif start==0:                                                          #Si la partie n'est pas démarrée
            menu()
            curseur()

        elif start==-1:                                                         #Si on est dans le menu des options
            options()
            curseur()

    def draw(self):
        '''
                                                                                ██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
                                                                                ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
                                                                                ██║░░██║██████╔╝███████║░╚██╗████╗██╔╝
                                                                                ██║░░██║██╔══██╗██╔══██║░░████╔═████║░
                                                                                ██████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░
                                                                                ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░
        '''
        global start

        if start==1:                                                            #Si la partie est démarrée
            pyxel.clip(Player['x']-75,Player['y']-75,150,150)                   #affiche qu'une certaine partie de la map a l'écran
            pyxel.cls(0)                                                        #colorie toute la map en noir 
            pyxel.blt(0,0,0,0,0,640,320,0)                                      #imprime """la map"""
            Lampe()
            
            if Player['Sens']=='Droite':
                pyxel.blt(Player['x']-8,Player['y']-8,1,0,0,16,16,0)
            elif Player['Sens']=='Gauche':
                pyxel.blt(Player['x'],Player['y'],1,0,16,16,16,0)
                
#Si l'ennemis est dans le flash : il est visible
# + Si il regarde a droite : sprite a droite et inversement
            if ((-Bot2['x']+Player['x']) < Player['Vue'] and (Bot2['x']-Player['x']) < Player['Vue']) and ((-Bot2['y']+Player['y']) < Player['Vue'] and (Bot2['y']-Player['y']) < Player['Vue'])  :
                if Bot2['Sens']=='Droite':
                    pyxel.blt(Bot2['x'],Bot2['y'],1,16,0,16,16,0)
                elif Bot2['Sens']=='Gauche':
                    pyxel.blt(Bot2['x'],Bot2['y'],1,16,16,16,16,0)
            
        
#Si le joueur regarde a droite : sprite a droite et inversement
            if ((-Bot1['x']+Player['x']) < Player['Vue'] and (Bot1['x']-Player['x']) < Player['Vue']) and ((-Bot1['y']+Player['y']) < Player['Vue'] and (Bot1['y']-Player['y']) < Player['Vue'])  :
                if Bot1['Sens']=='Droite':
                    pyxel.blt(Bot1['x'],Bot1['y'],1,32,0,16,16,0)
                if Bot1['Sens']=='Gauche':
                    pyxel.blt(Bot1['x'],Bot1['y'],1,32,16,16,16,0)
                    

            XX=(str('X : '))+(str(Xsouris))                                     
            YY=(str('Y : '))+(str(Ysouris))                                     
            pyxel.text(0,0,XX,2)                                                #Position Y du curseur en haut a droite de l'écran                                   
            pyxel.text(30,0,YY,2)                                               #Position Y du curseur en haut a droite de l'écran 


            Bat=(str('Batterie : '))+(str(Player['Batterie']))
            pyxel.text(0,20,Bat,2)                                              #Batterie restante en haut a droite de l'écran           


            Stam=(str('Stamina : '))+(str(Player['Stamina']))                   #Stamina en haut a gauche (si elle est faible : elle devient rouge)
            if Player['Stamina'] >= 25 :
                pyxel.text(0,10,Stam,2)
            else:
                pyxel.text(0,10,Stam,8)
                

            pyxel.pset(Xsouris,Ysouris,14)                                      #Curseur Visible pendant le jeu avec un point et dans le menu principal et les options avec un curseur
        if start==0 or start==-1 :
            pyxel.blt(Xsouris,Ysouris,2,48,0,6,6,0)
        
        
        
        

App()