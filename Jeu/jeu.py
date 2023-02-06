import pyxel,random                                                              #Mathieu brodard, Mathieu vilmot, Mohamed Latreche, Sailan Sivakumar
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

def Detectdeplace() :                                                               #Fonction retournant True si le joueur se déplace
    if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):                         #Test en Bas
        return True
    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):                        #Test à Droite
        return True
    if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q) :                        #Test à Gauche
        return True
    if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z):                           #Test en Haut
        return True

def FrameDep(entity,s):                                                             #Fonction permetant de changer les Sprites d'entités par intervale de s ticks 
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
            
def BoutonMenu(x1,x2,xdetec1,xdetec2,y1,y2,ydetec1,ydetec2):
    if (Xsouris>=xdetec1 and Xsouris<=xdetec2) and (Ysouris>=ydetec1 and Ysouris<=ydetec2):       #Si la souris est sur Le bouton: afficher les flèches et active la detection des clicks
        pyxel.blt(x1,y1,2,0,1,6,8,0)
        pyxel.blt(x2,y2,2,8,1,6,8,0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):                                                   #Si le joueur clique : Active peut importe ce qu'il y a après
            return True
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
Player['StamDepletion']=1


def deplacement():                                                              #Déplacement Du joueur                                                                             
    if Player['y']<=320 :                                                       #Déplacement Vers le bas 
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            Player['y']=Player['y']+Player['Vitesse']
    if Player['x']<=640 :                                                       #Déplacement Vers la Droite et modifie le sens vers la droite    
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            Player['x']=Player['x']+Player['Vitesse']
            Player['Sens']='Droite'
    if Player['x']>=0 :                                                         #Déplacement Vers la gauche et modifie le sens vers la gauche 
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
            Player['x']=Player['x']-Player['Vitesse']
            Player['Sens']='Gauche'
    if Player['y']>=0 :                                                         #Déplacement Vers le haut 
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z):
            Player['y']=Player['y']-Player['Vitesse']
    if Detectdeplace() == True and pyxel.btn(pyxel.KEY_SHIFT) != True :
        FrameDep(Player,24)
    else:
        Player['Frame']= 0
        
        
        
def Course():                                                                   #Course et système de Stamina
    if pyxel.btn(pyxel.KEY_SHIFT) and Player['Fatigue'] != 1:
        Player['Vitesse']=4
        Player['Stamina']= Player['Stamina']-Player['StamDepletion']
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
    if Player['Stamina']<=101 and Player['Stamina']>85 and Player['Fatigue']!=1:                   #Si la stamina restante est entre 100% et 80% et que le joueur n'est pas fatiguer :
        pyxel.blt(Player['x']-75,Player['y']-68,2,96,0,32,16,1)                                          #Montrer la barre remplie
        
    elif Player['Stamina']<=85 and Player['Stamina']>60 and Player['Fatigue']!=1:                  #Si la stamina restante est entre 80% et 60% et que le joueur n'est pas fatiguer:
        pyxel.blt(Player['x']-75,Player['y']-68,2,96,16,32,16,1)                                         #Montrer la barre asser remplie
        
    elif Player['Stamina']<=60 and Player['Stamina']>45 and Player['Fatigue']!=1:                  #Si la stamina restante est entre 60% et 45% et que le joueur n'est pas fatiguer:
        pyxel.blt(Player['x']-75,Player['y']-68,2,96,32,32,16,1)                                         #Montrer la barre à moitié vide
        
    elif Player['Stamina']<= 45 and Player['Stamina']>25 and Player['Fatigue']!=1:                 #Si la stamina restante est entre 45% et 25% et que le joueur n'est pas fatiguer:
        pyxel.blt(Player['x']-75,Player['y']-68,2,96,48,32,16,1)                                         #Montrer la barre presque vide
        
    elif Player['Stamina']<=25 and Player['Fatigue']!=1:                                           #Si la stamina restante est entre 25% et 0% et que le joueur n'est pas fatiguer:
        pyxel.blt(Player['x']-75,Player['y']-68,2,96,64,32,16,1)                                         #Montrer la barre rouge et vide
        
    elif Player['Fatigue']==1:                                                                     #Si le joueur est fatiguer peut importe sa stamina restante :
        pyxel.blt(Player['x']-75,Player['y']-68,2,96,80,32,16,1)                                         #Montrer la barre casser

def BougeMap():                                                                          #Illusion de se déplacer sur la map
    global Xmap,Ymap
    if Player['x']>=635:                                                                      #Dès que le joueur est asser à droite de l'écran
        Xmap-=640                                                                                  #la tilemap va 1 écran à droite
        Player['x']-=630                                                                           #le joueur passe à gauche
        
    elif Player['x']<=5:                                                                      #Dès que le joueur est asser à gauche de l'écran
        Xmap=Xmap+640                                                                              #la tilemap va 1 écran à gauche
        Player['x']+=630                                                                           #le joueur passe à droite
        
    elif Player['y']>=315:                                                                    #Dès que le joueur est asser en haut de l'écran
        Ymap-=320                                                                                  #la tilemap va 1 écran en haut
        Player['y']-=310                                                                           #le joueur passe en bas
        
    elif Player['y']<=5:                                                                      #Dès que le joueur est asser en bas de l'écran
        Ymap=Ymap+320                                                                              #la tilemap va 1 écran en bas
        Player['y']+=310                                                                           #le joueur passe en haut
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
Bot1['Sens']='Droite'
Bot1['Frame']= 0
Bot1['Type']='Amogus'


Bot2=dict()
Bot2['x']=50                                                                    #Indique l'emplacement X du Bot2
Bot2['y']=57                                                                    #Indique l'emplacement Y du Bot2
Bot2['Sens']='Droite'
Bot2['Frame']=0
Bot2['Type']='Phantom'

Bot3=dict()
Bot3['x']=250                                                                    #Indique l'emplacement X du Bot2
Bot3['y']=157                                                                    #Indique l'emplacement Y du Bot2
Bot3['Sens']='Droite'
Bot3['Frame']=0
Bot3['Type']='Phantom'

def bot(entity):                                                                 #Fait en sorte que les bots pourusivent le joueur en fonction de leur vitesse 
    if Player['x']-entity['x'] >= 0:
        entity['Sens']='Droite'
        entity['x']=entity['x']+1*entity['Vitesse']
    if Player['x']-entity['x'] <= 0:
        entity['Sens']='Gauche'
        entity['x']=entity['x']-1*entity['Vitesse']
    if Player['y']-entity['y'] >= 0:
        entity['y']=entity['y']+1*entity['Vitesse']
    if Player['y']-entity['y'] <= 0:
        entity['y']=entity['y']-1*entity['Vitesse']
    FrameDep(entity,36)
        
        
        
def types(entity):                                                              #Utilise les différentes fonction selon le type du bot 
    if entity['Type']=='Phantom':                                               #Détecte si le bot est un Fantome
        Phantom(entity)
    if entity['Type']=='Amogus':                                                #Détecte si le bot est un Amogus (On ne va pas garder ce type)
        Amogus(entity)
    
def Phantom(entity):                                                            #Fait les caractéristique du Fantome
    entity['Vitesse']=random.uniform(0.05,1)+random.uniform(0.05,1)             #Sa vitesse change aléatoirement entre 0.1 et 2.
    Draw32px(entity,224,0,-1)
    bot(entity)

def Amogus(entity):                                                             #Fait les caractéristique de l'Amogus (rien)
    entity['Vitesse']=1.5
    Draw32px(entity,192,0,1)
    bot(entity)

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
    if Player['Batterie']<=100:                                                      #Si la batterie est entre 100% et 80%:
        Player['Vue']=60                                                                  #la vue passe a 60 pixels
        
    if Player['Batterie']<=80:                                                       #Si la batterie est entre 80% et 60%:
        Player['Vue']=55                                                                  #la vue passe a 55 pixels
        
    if Player['Batterie']<=60:                                                       #Si la batterie est entre 60% et 40%:
        Player['Vue']=45                                                                  #la vue passe a 45 pixels
        
    if Player['Batterie']<=40:                                                       #Si la batterie est entre 40% et 20%:
        Player['Vue']=35                                                                  #la vue passe a 35 pixels
        
    if Player['Batterie']<=20:                                                       #Si la batterie est à 20% ou moins:
        Player['Vue']=20                                                                  #la vue passe a 20 pixels
        
    if Player['Batterie']<=3:                                                        #La batterie ne va pas en dessous de 2%
        Player['Batterie']=2

    if Player['Vue']<20:
        Player['Vue']=20
    if pyxel.btn(pyxel.KEY_B):                                                  #Test de la batterie avec des touches
        Player['Batterie']=100
    if pyxel.btn(pyxel.KEY_N):
        Player['Batterie']=Player['Batterie']-10
  

def BatterieAffichage():                                                                 #Diminue la luminosité de la lampe torche en fonction de la Batterie
    if Player['Batterie']<=100:                                                      #Si la batterie est entre 100% et 80%:
        pyxel.blt(Player['x']-80,Player['y']-80,2,64,0,32,16,1)                           #le barre de pile est pleine (vert foncé)
        
    if Player['Batterie']<=80:                                                       #Si la batterie est entre 80% et 60%:
        pyxel.blt(Player['x']-80,Player['y']-80,2,64,16,32,16,1)                          #le barre de pile est 1 barre vide (vert clair)
        
    if Player['Batterie']<=60:                                                       #Si la batterie est entre 60% et 40%:
        pyxel.blt(Player['x']-80,Player['y']-80,2,64,32,32,16,1)                          #le barre de pile est 2 barres vide (jaune)
        
    if Player['Batterie']<=40:                                                       #Si la batterie est entre 40% et 20%:
        pyxel.blt(Player['x']-80,Player['y']-80,2,64,48,32,16,1)                          #le barre de pile à 2 barres restantes (orange)
        
    if Player['Batterie']<=20:                                                       #Si la batterie est à 20% ou moins:
        pyxel.blt(Player['x']-80,Player['y']-80,2,64,64,32,16,1)                          #le barre de pile à 1 barre restante (rouge)

        
        

#prototype lampe V1
def Lampe():                                                                    #Affiche une partie de la map autour du joueur en fonction de la visibilité 
    for x in range(Player['x']-75,Player['x']+75):
        for y in range(Player['y']-75,Player['y']+75):
            b=pyxel.sqrt((x-Player['x'])**2+(y-Player['y'])**2)
            if b>Player['Vue']:
                pyxel.pset(x,y,0)
            if b>=Player['Vue']-7 and b<=Player['Vue'] and pyxel.pget(x,y)==4:  #remplace les détails du sols si ils sont loins (plus de réalisme)
                pyxel.pset(x,y,1)
                
def LampeLum():
    for x in range(Player['x']-75,Player['x']+75):
        for y in range(Player['y']-75,Player['y']+75):
            b=pyxel.sqrt((x-Player['x'])**2+(y-Player['y'])**2)                 #place différents pixels de couleurs selon la distance avec le joueur: 
            if b<Player['Vue']-22:                                                   #à 22 pixels ou moins, couleur jaune
                pyxel.pset(x,y,10)
            if b>=Player['Vue']-22 and b<Player['Vue']-16:                           #à 16 pixels ou moins, couleur orange
                pyxel.pset(x,y,9)
            if b>=Player['Vue']-16 and b<=Player['Vue']-7:                           #à 7 pixels ou moins, couleur marron
                pyxel.pset(x,y,4)
            if b>=Player['Vue']-7 and b<=Player['Vue']:                              #à 7 pixel jusqu'a la limite, couleur bleu foncé
                pyxel.pset(x,y,1)
            if pyxel.btn(pyxel.KEY_F):                                          #affiche le rayon blanc du flash 
                if b<Player['Vue']-40:                                                   
                    pyxel.pset(x,y,7)


def flash():                                                                    #Flash les enemie 
        if pyxel.btn(pyxel.KEY_F):                                              #si la touche F est pressé alors 
                Player['Batterie']=Player['Batterie']-0.7                       #enlève 20% de batterie par seconde de flash 
                Player['Vue']=Player['Vue']+5                                   #augmente la vue par 5 a chaque seconde 
                if Player['Vue']>85:                                            #permet de ne pas dépassé le clip 
                    Player['Vue']=Player['Vue']-5
                if Player['Batterie']<5:                                        #permet de faire une transition si le joueur na plus de batterie 
                    Player['Vue']=Player['Vue']-10
                if not pyxel.btn(pyxel.KEY_F):                                        #permet de faire une transition si le joueur na plus de batterie 
                    Player['Vue']=Player['Vue']-10



            










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
    
    BoutonMenu(110,160,120,160,39,39,38,47)                                     #La fonction permettant de faire fonctionner le bouton Start Game
    if BoutonMenu(110,160,120,160,39,39,38,47)==True:
            start=1
    BoutonMenu(110,160,120,160,79,79,78,87)                                     #La fonction permettant de faire fonctionner le bouton Options
    if BoutonMenu(110,160,120,160,79,79,78,87)==True:                                                                            
        start=-1
        
    BoutonMenu(110,160,120,160,119,119,118,127)                                 #La fonction permettant de faire fonctionner le bouton Quit Game
    if BoutonMenu(110,160,120,160,119,119,118,127)==True:
        pyxel.quit()
    
    if pyxel.btn(pyxel.KEY_E):
        start=1



def options():                                                                  #Le menu des Options avec la Stamina modifiable
    global start
    pyxel.cls(0)
    pyxel.text(120,120,str("Return"),7)
    
    if (Xsouris>=120 and Xsouris<=160) and (Ysouris>=118 and Ysouris<=127):     #Bouton pour retruner au menu principal
        pyxel.blt(110,119,2,0,1,6,8,0)
        pyxel.blt(160,119,2,8,1,6,8,0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            start=0
    pyxel.text(80,40,str("Stamina : Courte   Moyenne   Longue   Infinie"),7)              #Boutons permettant de changer la Stamina du personnage
    
    if (Xsouris>=120 and Xsouris<=142) and (Ysouris>=38 and Ysouris<=47) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        Player['StamDepletion']=1.5
    
    if (Xsouris>=156 and Xsouris<=182) and (Ysouris>=38 and Ysouris<=47) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        Player['StamDepletion']=1
        
    if (Xsouris>=196 and Xsouris<=218) and (Ysouris>=38 and Ysouris<=47) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        Player['StamDepletion']=0.5
        
    if (Xsouris>=232 and Xsouris<=258) and (Ysouris>=38 and Ysouris<=47) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        Player['StamDepletion']=0
    
    if Player['StamDepletion']==1.5:                                                       #montrer la Stamina selectionnée en soulignant celle selectionnée
        pyxel.line(120,48,142,48,7)
    
    elif Player['StamDepletion']==1:
        pyxel.line(156,48,182,48,7)
    
    elif Player['StamDepletion'] == 0.5:
        pyxel.line(196,48,218,48,7)
    
    else:
        pyxel.line(232,48,258,48,7)
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
            types(Bot1)
            types(Bot2)
            types(Bot3)
            
            Lampe()                                                             #affiche qu'une certaine partie de la map a l'écran
                                                                                           
            Draw32px(Player,0,0,1)                                              #affiche le joueur et des animations
            BatterieAffichage()
            if not pyxel.btn(pyxel.KEY_F) and Player['Batterie']>5:             #si la touche flash et la battetrie est supérierur a 5
                Batterie()                                                          #Batterie restante en haut a gauche de l'écran           
            flash()                                                                   #Ce changement était nessessaire pour que la batterie s'affiche.

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