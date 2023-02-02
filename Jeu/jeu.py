import pyxel                                                                    #Mathieu brodard, Mathieu vilmot, Mohamed Latreche, Sailan Sivakumar
'''
███╗░░██╗░█████╗░███╗░░░███╗░░░░░░██████╗░██╗░░░██╗░░░░░░░░░██╗███████╗██╗░░░██╗
████╗░██║██╔══██╗████╗░████║░░░░░░██╔══██╗██║░░░██║░░░░░░░░░██║██╔════╝██║░░░██║
██╔██╗██║██║░░██║██╔████╔██║░░░░░░██║░░██║██║░░░██║░░░░░░░░░██║█████╗░░██║░░░██║
██║╚████║██║░░██║██║╚██╔╝██║░░░░░░██║░░██║██║░░░██║░░░░██╗░░██║██╔══╝░░██║░░░██║
██║░╚███║╚█████╔╝██║░╚═╝░██║░░░░░░██████╔╝╚██████╔╝░░░░╚█████╔╝███████╗╚██████╔╝
╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝░░░░░░╚═════╝░░╚═════╝░░░░░░╚════╝░╚══════╝░╚═════╝░


                                                                                
                                                                                ██╗░░░██╗████████╗██╗██╗░░░░░██╗████████╗░█████╗░██╗██████╗░███████╗░██████╗
                                                                                ██║░░░██║╚══██╔══╝██║██║░░░░░██║╚══██╔══╝██╔══██╗██║██╔══██╗██╔════╝██╔════╝
                                                                                ██║░░░██║░░░██║░░░██║██║░░░░░██║░░░██║░░░███████║██║██████╔╝█████╗░░╚█████╗░
                                                                                ██║░░░██║░░░██║░░░██║██║░░░░░██║░░░██║░░░██╔══██║██║██╔══██╗██╔══╝░░░╚═══██╗
                                                                                ╚██████╔╝░░░██║░░░██║███████╗██║░░░██║░░░██║░░██║██║██║░░██║███████╗██████╔╝
                                                                                ░╚═════╝░░░░╚═╝░░░╚═╝╚══════╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░
                                                                                Autres fonctions multitâches ou détectant des choses.
'''
global Xmap,Ymap        
Xmap=0
Ymap=0

def Detectdeplace() :                                                                 #Fonction retournant True si le joueur se déplace
    if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):                         #Test en Bas
        return True
    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):                        #Test à Droite
        return True
    if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q) :                        #Test à Gauche
        return True
    if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z):                           #Test en Haut
        return True

def FrameDep(entity,s):                                                         #Fonction permetant de changer les Sprites d'entités par intervale de s ticks 
    if pyxel.frame_count % s >= 0 and pyxel.frame_count % s < (s//4) :
        entity['Frame'] = 0
    elif pyxel.frame_count % s >= (s//4) and pyxel.frame_count % s <= (s//2) :
        entity['Frame'] = 1
    elif pyxel.frame_count % s >= (s//2) and pyxel.frame_count % s <= (s*0.75) :
        entity['Frame'] = 2
    elif pyxel.frame_count % s >= (s*0.75) :
        entity['Frame'] = 3
        
def Draw32px(entity,u,v,inverse):                                               #Fonction permettant d'afficher une entité de 32 pixels et 4 frame d'animations.
    if entity['Sens']=='Droite':                                                    #Regarde si il regarde à Gauche
        if entity['Frame']==0:                                                           #Les différentes Frames d'animations
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v,inverse*32,32,1)
        elif entity['Frame']==1:
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v+32,inverse*32,32,1)
        elif entity['Frame']==2:
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v+64,inverse*32,32,1)
        else:
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v+96,inverse*32,32,1)
    if entity['Sens']=='Gauche':                                                    #Regarde si il regarde à Droite
        if entity['Frame']==0:                                                            #Les différentes Frames d'animations
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v,-inverse*32,32,1)
        elif entity['Frame']==1:
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v+32,-inverse*32,32,1)
        elif entity['Frame']==2:
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v+64,-inverse*32,32,1)
        else:
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v+96,-inverse*32,32,1)
'''

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
Player['Frame']= 0
Player['Fatigue']= 0



def deplacement():                                                              #Déplacement Du joueur                                                                             
    if Player['y']<=320 :                                                      #Déplacement Vers le bas 
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            Player['y']=Player['y']+Player['Vitesse']
    if Player['x']<=640 :                                                     #Déplacement Vers la Droite et modifie le sens vers la droite    
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            Player['x']=Player['x']+Player['Vitesse']
            Player['Sens']='Droite'
    if Player['x']>=0 :                                                        #Déplacement Vers la gauche et modifie le sens vers la gauche 
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
            Player['x']=Player['x']-Player['Vitesse']
            Player['Sens']='Gauche'
    if Player['y']>=0 :                                                          #Déplacement Vers le haut 
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z):
            Player['y']=Player['y']-Player['Vitesse']
    if Detectdeplace() == True and pyxel.btn(pyxel.KEY_SHIFT) != True :
        FrameDep(Player,24)
    else:
        Player['Frame']= 0
        
        
        
def Course():                                                                   #Course et système de Stamina
    if pyxel.btn(pyxel.KEY_SHIFT) and Player['Fatigue'] != 1:
        Player['Vitesse']=4
        Player['Stamina']= Player['Stamina']-1.75
        FrameDep(Player,12)
        if Player['Stamina']<=5:
            Player['Fatigue']= 1
    else:
        if Player['Stamina']<=25:                                               #Si le joueur a peu de Stamina : sa vitesse est réduite temporairement
            Player['Vitesse']=1
        else:
            Player['Vitesse']=2
            Player['Fatigue']= 0
        if not pyxel.btn(pyxel.KEY_SHIFT):                                      #Si le joueur essai toujours de courrir, sa stamina ne reviens pas (ajout de stress ++)
            Player['Stamina']= Player['Stamina']+0.5
    if  Player['Stamina'] >= 101 :                                              #Stamina ne dépasse pas 100%
            Player['Stamina']= Player['Stamina']-1
    if  Player['Stamina'] <= 0 :                                                #Stamina ne passe pas 0%
        Player['Stamina']= Player['Stamina']+2  

def drawSprint():
    if Player['Stamina']<=101 and Player['Stamina']>85 and Player['Fatigue']!=1:
        pyxel.blt(Player['x']-75,Player['y']-68,2,96,0,32,16,1)
        
    elif Player['Stamina']<=85 and Player['Stamina']>60 and Player['Fatigue']!=1:
        pyxel.blt(Player['x']-75,Player['y']-68,2,96,16,32,16,1)
        
    elif Player['Stamina']<=60 and Player['Stamina']>45 and Player['Fatigue']!=1:
        pyxel.blt(Player['x']-75,Player['y']-68,2,96,32,32,16,1)
        
    elif Player['Stamina']<= 45 and Player['Stamina']>25 and Player['Fatigue']!=1:
        pyxel.blt(Player['x']-75,Player['y']-68,2,96,48,32,16,1)
        
    elif Player['Stamina']<=25 and Player['Fatigue']!=1:
        pyxel.blt(Player['x']-75,Player['y']-68,2,96,64,32,16,1)
        
    elif Player['Fatigue']==1:
        pyxel.blt(Player['x']-75,Player['y']-68,2,96,80,32,16,1)

def BougeMap():
    global Xmap,Ymap
    if Player['x']>=635:
        Xmap-=640
        Player['x']-=630
        
    elif Player['x']<=5:
        Xmap=Xmap+640
        Player['x']+=630
    elif Player['y']>=315:
        Ymap-=320
        Player['y']-=310
    elif Player['y']<=5:
        Ymap=Ymap+320
        Player['y']+=310
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
Bot1['Sens']= 'Droite'                                                          #Indique le Sens du Bot1
Bot1['Frame']= 0


Bot2=dict()
Bot2['x']=50                                                                    #Indique l'emplacement X du Bot2
Bot2['y']=57                                                                    #Indique l'emplacement Y du Bot2
Bot2['Vitesse']=1.5                                                               #Indique la Vitesse du Bot2
Bot2['Sens']= 'Droite'                                                          #Indique le Sens du Bot2
Bot2['Frame']=0

def ai2():                                                                      #Fait en sorte que le bot2 pourusit le joueur en fonction de sa vitesse 
    if Player['x']-Bot2['x'] >= 0:
        Bot2['Sens']='Droite'
        Bot2['x']=Bot2['x']+1*Bot2['Vitesse']
    if Player['x']-Bot2['x'] <= 0:
        Bot2['Sens']='Gauche'
        Bot2['x']=Bot2['x']-1*Bot2['Vitesse']
    if Player['y']-Bot2['y'] >= 0:
        Bot2['y']=Bot2['y']+1*Bot2['Vitesse']
    if Player['y']-Bot2['y'] <= 0:
        Bot2['y']=Bot2['y']-1*Bot2['Vitesse']
    FrameDep(Bot2,36)
        
        
        
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
        pyxel.blt(Player['x']-80,Player['y']-80,2,64,0,32,16,1)    
    if Player['Batterie']<=80:
        Player['Vue']=55
        pyxel.blt(Player['x']-80,Player['y']-80,2,64,16,32,16,1)
    if Player['Batterie']<=60:
        Player['Vue']=45
        pyxel.blt(Player['x']-80,Player['y']-80,2,64,32,32,16,1)
    if Player['Batterie']<=40:
        Player['Vue']=35
        pyxel.blt(Player['x']-80,Player['y']-80,2,64,48,32,16,1)
    if Player['Batterie']<=20:
        Player['Vue']=20
        pyxel.blt(Player['x']-80,Player['y']-80,2,64,64,32,16,1)
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
            if b>=Player['Vue']-7 and b<=Player['Vue'] and pyxel.pget(x,y)==4:
                pyxel.pset(x,y,1)
                
def LampeLum():
    for x in range(Player['x']-66,Player['x']+66):
        for y in range(Player['y']-66,Player['y']+66):
            b=pyxel.sqrt((x-Player['x'])**2+(y-Player['y'])**2)
            if b<Player['Vue']-22:
                pyxel.pset(x,y,10)
            if b>=Player['Vue']-22 and b<Player['Vue']-16:
                pyxel.pset(x,y,9)
            if b>=Player['Vue']-16 and b<=Player['Vue']-7:
                pyxel.pset(x,y,4)
            if b>=Player['Vue']-7 and b<=Player['Vue']:
                pyxel.pset(x,y,1)

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
            deplacement() 
            ai2()
            ai1()
            curseur()
            Course()
            BougeMap()
            
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
            pyxel.clip(Player['x']-75,Player['y']-75,150,150)                   
            pyxel.cls(0)                                                        #colorie toute la map en noir
            LampeLum()                                                          #affiche les couleurs de la lampe  
            pyxel.bltm(Xmap,Ymap,0,0,0,6400,3200,1)                                     #imprime la tilemap
                                                                                            #Si l'ennemis est dans le flash : il est visible
            Draw32px(Bot1,192,0,1)
            Draw32px(Bot2,224,0,-1)
            
            Lampe()                                                             #affiche qu'une certaine partie de la map a l'écran
                                                                                           
            Draw32px(Player,0,0,1)                                              #affiche le joueur et des animations
            
            
            Batterie()                                                          #Batterie restante en haut a gauche de l'écran           
                                                                                #Ce changement était nessessaire pour que la batterie s'affiche.

            drawSprint()                   #Stamina en haut a gauche (si elle est faible : elle devient rouge)
           
        if start==0 or start==-1 :
            pyxel.blt(Xsouris,Ysouris,2,48,0,6,6,0)
            pyxel.clip()
        

App()

'''
            XX=(str('X : '))+(str(Xsouris))                                     
            YY=(str('Y : '))+(str(Ysouris))                                     
            pyxel.text(Player['x']-75,Player['y']-75,XX,2)                                                #Position Y du curseur en haut a droite de l'écran                                   
            pyxel.text(Player['x']-45,Player['y']-75,YY,2)                                               #Position Y du curseur en haut a droite de l'écran 
'''