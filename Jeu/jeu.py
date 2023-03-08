import pyxel,random                                                              #Mathieu brodard, Mathieu vilmot, Mohamed Latreche, Sailan Sivakumar
'''                                                                                
                                                                                ██╗░░░██╗████████╗██╗██╗░░░░░██╗████████╗░█████╗░██╗██████╗░███████╗░██████╗
                                                                                ██║░░░██║╚══██╔══╝██║██║░░░░░██║╚══██╔══╝██╔══██╗██║██╔══██╗██╔════╝██╔════╝
                                                                                ██║░░░██║░░░██║░░░██║██║░░░░░██║░░░██║░░░███████║██║██████╔╝█████╗░░╚█████╗░
                                                                                ██║░░░██║░░░██║░░░██║██║░░░░░██║░░░██║░░░██╔══██║██║██╔══██╗██╔══╝░░░╚═══██╗
                                                                                ╚██████╔╝░░░██║░░░██║███████╗██║░░░██║░░░██║░░██║██║██║░░██║███████╗██████╔╝
                                                                                ░╚═════╝░░░░╚═╝░░░╚═╝╚══════╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░
                                                                                Autres fonctions multitâches ou détectant des choses.
Bonjour, le jeu n'est pas dutout fini, il reste énormement de chose a faire, ceci dit c'est une demo fonctionnel de ce que nous immaginions pour le jeu.
merci d'être indulgent 
et désoler du manque de commenttaire (spécifiquement le menu)
beaucoup de méchanique de jeu reste a programmer et a aprofondire (exemple : les attaque du joueur)
si vous avez des suggestions elle sont les bien venu
on espère que le jeu vous plaira  

coeur <3
touche actuelle  (peuvent être changé):
zqsd et flèche directionnel pour se déplacer 
F pour le flash (rester appuyer, consomme beaucoup de batterie et permet d'impacter certain mob )
shift pour courrir (consomme de l'endurence)
tab pour retourner au menu
ALT pour frapper (consomme de l'endurence)

touche devlopeur
debut/home pour mettre le jour 
W pour mettre la vie au max 
et plein d'autre a découvrir ! 

'''
global start                                                                    #Met en place La variable Global start 
start=10                                                                         #Indique si le jeu est commencer ou non (0 pour non)
global Xmap,Ymap,XResol,YResol,MapMob        
Xmap=0
Ymap=0
XResol=640
YResol=350
MapMob=[[random.randint(1,3),random.randint(1,3),random.randint(1,3)] for _ in range(6)]
MapMob[0][0]=0

def Detectdeplace() :                                                               #Fonction retournant True si le joueur se déplace
    if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):                         #Test en Bas
        return True
    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):                        #Test à Droite
        return True
    if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q) :                        #Test à Gauche
        return True
    if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z):                           #Test en Haut
        return True

def Detectflash(entity):                                                            #Detecte si le joueur flash proche d'une entité quelquonque
    if pyxel.btn(pyxel.KEY_F) and (Player['x']<entity['x']+48 and Player['x']>entity['x']-48 and Player['y']>entity['y']-48 and Player['y']<entity['y']+48) and Player['Batterie']>=5 :
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
        
def WarioApparition():                                                              #La fonction Wario non fonctionnel pour la early acces
    Bot1['Type']=='Wario'
    Bot1['x']=100
    Bot1['y']=100
        
def Draw32px(entity,u,v,inverse,col):                                               #Fonction permettant d'afficher une entité de 32 pixels et 4 frame d'animations.
    if entity['Sens']=='Droite':                                                    #Regarde si il regarde à Gauche
        if entity['Frame']==0:                                                           #Les différentes Frames d'animations
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v,inverse*32,32,col)
        elif entity['Frame']==1:
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v+32,inverse*32,32,col)
        elif entity['Frame']==2:
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v+64,inverse*32,32,col)
        else:
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v+96,inverse*32,32,col)
    if entity['Sens']=='Gauche':                                                    #Regarde si il regarde à Droite
        if entity['Frame']==0:                                                            #Les différentes Frames d'animations
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v,-inverse*32,32,col)
        elif entity['Frame']==1:
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v+32,-inverse*32,32,col)
        elif entity['Frame']==2:
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v+64,-inverse*32,32,col)
        else:
            pyxel.blt(entity['x']-16,entity['y']-16,1,u,v+96,-inverse*32,32,col)

def Draw64px(entity,u,v,col):                                                               #Fonction dessinant les objets de taille 64 pixels
    if entity['Frame']<=1:
        pyxel.blt(entity['x']-32,entity['y']-32,1,u,v,64,64,col)                            #echange entre 2 frames (prend beaucoup de place sur le pyxres)
    else:
        pyxel.blt(entity['x']-32,entity['y']-32,1,u,v+64,64,64,col)
            
def BoutonMenu(x1,x2,xdetec1,xdetec2,y1,y2,ydetec1,ydetec2):
    if (Xsouris>=xdetec1 and Xsouris<=xdetec2) and (Ysouris>=ydetec1 and Ysouris<=ydetec2):       #Si la souris est sur Le bouton: afficher les flèches et active la detection des clicks
        pyxel.blt(x1,y1,2,0,1,6,8,0)
        pyxel.blt(x2,y2,2,8,1,6,8,0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):                                                   #Si le joueur clique : Active peut importe ce qu'il y a après
            return True


global debug
debug=0
def DebugMenu():
    global debug
    if debug>1 or debug<0:
        debug=0
    if debug==1:
        pyxel.text(0,0,str('PV:')+str(Player['PV']),7)
        pyxel.text(0,10,str('Batterie:')+str(Player['Batterie']),7)
        pyxel.text(0,20,str('Stamina:')+str(Player['Stamina']),7)
        pyxel.text(0,30,str('start:')+str(start),7)
        pyxel.text(0,40,str('Xmob:')+str(Player['Xmob']),7)
        pyxel.text(0,50,str('Ymob:')+str(Player['Ymob']),7)
        pyxel.text(0,60,str('Devmode:')+str(Devmode),7)
        pyxel.text(0,70,str('Porte:')+str(Porte),7)
        pyxel.text(0,80,str('XPointeur:')+str(pyxel.mouse_x),7)
        pyxel.text(0,90,str('YPointeur:')+str(pyxel.mouse_y),7)
        pyxel.text(0,100,str('BOT:')+str(Bot1['Type'])+str(Bot2['Type'])+str(Bot3['Type'])+str(Bot4['Type']),7)
        pyxel.pset(pyxel.mouse_x,pyxel.mouse_y,7)


        
'''
                                                                                    ░██████╗░█████╗░██╗░░░░░██╗░░░░░███████╗░██████╗
                                                                                    ██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔════╝██╔════╝
                                                                                    ╚█████╗░███████║██║░░░░░██║░░░░░█████╗░░╚█████╗░
                                                                                    ░╚═══██╗██╔══██║██║░░░░░██║░░░░░██╔══╝░░░╚═══██╗
                                                                                    ██████╔╝██║░░██║███████╗███████╗███████╗██████╔╝
                                                                                    ╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═════╝░
'''

#Le début des 100 lignes de l'enfer


Preset1={'Bot1Map':{'Type':'Zombie','x':320,'y':80,'PV':2}                                      #réglage Salle 2
       ,'Bot2Map':{'Type':'Phantom','x':120,'y':160,'PV':1}
       ,'Bot3Map':{'Type':'Phantom','x':540,'y':160,'PV':1}
       ,'Bot4Map':{'Type':'Mort','x':0,'y':0,'PV':1}}

Preset2={'Bot1Map':{'Type':'Phantom','x':320,'y':160,'PV':1}                                      #réglage Salle 2
       ,'Bot2Map':{'Type':'Mage','x':80,'y':60,'PV':1}
       ,'Bot3Map':{'Type':'Mort','x':0,'y':0,'PV':1}
       ,'Bot4Map':{'Type':'Mort','x':0,'y':0,'PV':1}}

Preset3={'Bot1Map':{'Type':'Zombie','x':320,'y':160,'PV':6}                                      #réglage Salle 2
       ,'Bot2Map':{'Type':'Golem','x':160,'y':160,'PV':1}
       ,'Bot3Map':{'Type':'Golem','x':480,'y':160,'PV':1}
       ,'Bot4Map':{'Type':'Phantom','x':140,'y':40,'PV':1}}

Preset4={'Bot1Map':{'Type':'Zombie','x':60,'y':280,'PV':3}                                      #réglage Salle 2
       ,'Bot2Map':{'Type':'Phantom','x':320,'y':300,'PV':1}
       ,'Bot3Map':{'Type':'Zombie','x':320,'y':160,'PV':3}
       ,'Bot4Map':{'Type':'Mort','x':0,'y':0,'PV':1}}

Preset5={'Bot1Map':{'Type':'Arabe','x':460,'y':160,'PV':1}                                      #réglage Salle 2
       ,'Bot2Map':{'Type':'Zombie','x':280,'y':120,'PV':2}
       ,'Bot3Map':{'Type':'Zombie','x':360,'y':120,'PV':3}
       ,'Bot4Map':{'Type':'Golem','x':320,'y':160,'PV':1}}

Preset6={'Bot1Map':{'Type':'Phantom','x':260,'y':200,'PV':1}                                      #réglage Salle 2
       ,'Bot2Map':{'Type':'Phantom','x':380,'y':160,'PV':1}
       ,'Bot3Map':{'Type':'Mage','x':460,'y':40,'PV':1}
       ,'Bot4Map':{'Type':'Phantom','x':320,'y':100,'PV':1}}

Preset7={'Bot1Map':{'Type':'Golem','x':320,'y':160,'PV':1}                                      #réglage Salle 2
       ,'Bot2Map':{'Type':'Mage','x':320,'y':160,'PV':1}
       ,'Bot3Map':{'Type':'Zombie','x':240,'y':80,'PV':4}
       ,'Bot4Map':{'Type':'Zombie','x':460,'y':240,'PV':1}}

Preset8={'Bot1Map':{'Type':'Golem','x':300,'y':260,'PV':1}                                      #réglage Salle 2
       ,'Bot2Map':{'Type':'Zombie','x':40,'y':160,'PV':4}
       ,'Bot3Map':{'Type':'Phantom','x':280,'y':120,'PV':1}
       ,'Bot4Map':{'Type':'Phantom','x':360,'y':200,'PV':1}}

Preset=[Preset1.copy(),Preset2.copy(),Preset3.copy(),Preset4.copy(),Preset5.copy(),Preset6.copy(),Preset7.copy(),Preset8.copy()]

ObjetPreset=[None,'Boisson','Jambon','Batterie','Coeur',None]

MapMob=[]

def SalleAlea():
    global MapMob
    Salle2={}
    Salle2=Preset[random.randint(0,7)].copy()
    Salle2['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle3={}
    Salle3=Preset[random.randint(0,7)].copy()
    Salle3['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle4={}
    Salle4=Preset[random.randint(0,7)].copy()
    Salle4['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle5={}
    Salle5=Preset[random.randint(0,7)].copy()
    Salle5['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle6={}
    Salle6=Preset[random.randint(0,7)].copy()
    Salle6['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle7={}
    Salle7=Preset[random.randint(0,7)].copy()
    Salle7['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle8={}
    Salle8=Preset[random.randint(0,7)].copy()
    Salle8['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle9={}
    Salle9=Preset[random.randint(0,7)].copy()
    Salle9['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle10={}
    Salle10=Preset[random.randint(0,7)].copy()
    Salle10['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle11={}
    Salle11=Preset[random.randint(0,7)].copy()
    Salle11['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle12={}
    Salle12=Preset[random.randint(0,7)].copy()
    Salle12['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle13={}
    Salle13=Preset[random.randint(0,7)].copy()
    Salle13['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle14={}
    Salle14=Preset[random.randint(0,7)].copy()
    Salle14['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle15={}
    Salle15=Preset[random.randint(0,7)].copy()
    Salle15['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle16={}
    Salle16=Preset[random.randint(0,7)].copy()
    Salle16['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle17={}
    Salle17=Preset[random.randint(0,7)].copy()
    Salle17['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle18={}
    Salle18=Preset[random.randint(0,7)].copy()
    Salle18['ObjetMap']={'Type':ObjetPreset[random.randint(0,5)], 'x':random.randint(40,600), 'y':random.randint(40,280)}
    Salle1={'Bot1Map':{'Type':'Mort','x':0,'y':0,'PV':1}
           ,'Bot2Map':{'Type':'Mort','x':0,'y':0,'PV':1}
           ,'Bot3Map':{'Type':'Mort','x':0,'y':0,'PV':1}
           ,'Bot4Map':{'Type':'Mort','x':0,'y':0,'PV':1}
           ,'ObjetMap':{'Type':None,'x':0,'y':0}}
    MapMob= [[Salle1 ,Salle2 ,Salle3 ,None]                                             #La map entière (avec les dictionnaires des salles correspondante (None = Pas de bots ou d'objet))
        ,[Salle4 ,Salle5 ,Salle6 ,None]
        ,[Salle7 ,Salle8 ,Salle9 ,None]
        ,[Salle10,Salle11,Salle12,None]
        ,[Salle13,Salle14,Salle15,None]
        ,[Salle16,Salle17,Salle18,None]
        ,[None   ,None   ,None   ,None]]

SalleAlea()

def MapMobSet():                                                                                  #Fonction mettant les preset des Mobs des Maps
    global MapMob,Lock
    if MapMob[Player['Ymob']][Player['Xmob']]==None:                                               #La salle de départ
        Bot1['Type']='Mort'
        Bot2['Type']='Mort'
        Bot3['Type']='Mort'
        Bot4['Type']='Mort'
        Objet['Type']=None
    else:                                                                                          #La salle 1
        Salle(MapMob[Player['Ymob']][Player['Xmob']])
    JambonBot['Type']='Mort'


def Salle(m):                                                                                     #cette fonction mets en place les salles selon les réglages donnés.
    Bot1['Type']=m['Bot1Map']['Type']                                                             #Bot1 avec sont Type, x et y de départ
    Bot1['x']=m['Bot1Map']['x']
    Bot1['y']=m['Bot1Map']['y']
    Bot1['PV']=m['Bot1Map']['PV']
    Bot2['Type']=m['Bot2Map']['Type']                                                             #Bot2 avec sont Type, x et y de départ
    Bot2['x']=m['Bot2Map']['x']
    Bot2['y']=m['Bot2Map']['y']
    Bot2['PV']=m['Bot2Map']['PV']
    Bot3['Type']=m['Bot3Map']['Type']                                                             #Bot3 avec sont Type, x et y de départ
    Bot3['x']=m['Bot3Map']['x']
    Bot3['y']=m['Bot3Map']['y']
    Bot3['PV']=m['Bot3Map']['PV']
    Bot4['Type']=m['Bot4Map']['Type']                                                             #Bot4 avec sont Type, x et y de départ
    Bot4['x']=m['Bot4Map']['x']
    Bot4['y']=m['Bot4Map']['y']
    Bot4['PV']=m['Bot4Map']['PV']
    Objet['x']=m['ObjetMap']['x']
    Objet['y']=m['ObjetMap']['y']
    Objet['Type']=m['ObjetMap']['Type']
    

global Lock
Lock=0

def SPorte():
    global Lock
    if Player['x']>33 and Player['x']<600 and Player['y']>33 and Player['y']<315 :
        if Bot1['Type']=='Mort' or Bot1['Type']=='Golem' and Bot2['Type']=='Mort' or Bot2['Type']=='Golem' and Bot3['Type']=='Mort' or Bot3['Type']=='Golem' and Bot4['Type']=='Mort' or Bot4['Type']=='Golem' :
            Lock=0
        else :
            Lock=1

    

    if Lock==1:
        pyxel.blt(277,314,0,176,72,85,42,3) 
        pyxel.blt(602,125,0,176,128,48,80,3)
        pyxel.blt(277,-10,0,176,72,85,42,3)
        pyxel.blt(-9,125,0,176,128,48,80,3)








'''

                                                                                ░░░░░██╗░█████╗░██╗░░░██╗███████╗██╗░░░██╗██████╗░
                                                                                ░░░░░██║██╔══██╗██║░░░██║██╔════╝██║░░░██║██╔══██╗
                                                                                ░░░░░██║██║░░██║██║░░░██║█████╗░░██║░░░██║██████╔╝
                                                                                ██╗░░██║██║░░██║██║░░░██║██╔══╝░░██║░░░██║██╔══██╗
                                                                                ╚█████╔╝╚█████╔╝╚██████╔╝███████╗╚██████╔╝██║░░██║
                                                                                ░╚════╝░░╚════╝░░╚═════╝░╚══════╝░╚═════╝░╚═╝░░╚═╝
'''
Coup=0
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
Player['StamDepletion']=1                                                       #rapidité a laquel la stamina se perd (course uniquement)
Player['StamRegen']=0.5                                                         #rapidité a laquel la stamina se regenere
Player['PV']=6
Player['Immune']=0
Player['Xmob']=0
Player['Ymob']=0
Player['Frappe']=dict()                                                         #Tous Player['frappe'][qqose] sont pour l'attaque du joueur.
Player['Frappe']['Status']=False
Player['Frappe']['Frame']=0
Player['Frappe']['x']=0
Player['Frappe']['y']=0
Player['Frappe']['Sens']='Droite'
Player['Objet']=None
Player['Energisante']=0
global XYmap
XYmap=MapMob[Player['Ymob']][Player['Xmob']]


    
def deplacement():                                                              #Déplacement Du joueur                                                                             
    if (pyxel.pget(Player['x']-10,Player['y']+14)!=1 and pyxel.pget(Player['x']-9,Player['y']+14)!=1 and pyxel.pget(Player['x']-8,Player['y']+14)!=1 and pyxel.pget(Player['x']-7,Player['y']+14)!=1 and pyxel.pget(Player['x']-6,Player['y']+14)!=1 and pyxel.pget(Player['x']-5,Player['y']+14)!=1 and pyxel.pget(Player['x']-4,Player['y']+14)!=1 and pyxel.pget(Player['x']-3,Player['y']+14)!=1 and pyxel.pget(Player['x']-2,Player['y']+14)!=1 and pyxel.pget(Player['x']-1,Player['y']+14)!=1 and pyxel.pget(Player['x']+9,Player['y']+14)!=1 and pyxel.pget(Player['x']+8,Player['y']+14)!=1 and pyxel.pget(Player['x']+7,Player['y']+14)!=1 and pyxel.pget(Player['x']+6,Player['y']+14)!=1 and pyxel.pget(Player['x']+5,Player['y']+14)!=1 and pyxel.pget(Player['x'],Player['y']+14)!=1 and pyxel.pget(Player['x']+1,Player['y']+14)!=1 and pyxel.pget(Player['x']+2,Player['y']+14)!=1 and pyxel.pget(Player['x']+3,Player['y']+14)!=1 and pyxel.pget(Player['x']+4,Player['y']+14)!=1):   
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            Player['y']=Player['y']+Player['Vitesse']

    if (pyxel.pget(Player['x']+9,Player['y']-16)!=1 and pyxel.pget(Player['x']+9,Player['y']-15)!=1 and pyxel.pget(Player['x']+9,Player['y']-14)!=1 and pyxel.pget(Player['x']+9,Player['y']-13)!=1 and pyxel.pget(Player['x']+9,Player['y']-12)!=1 and pyxel.pget(Player['x']+9,Player['y']-11)!=1 and pyxel.pget(Player['x']+9,Player['y']-10)!=1 and pyxel.pget(Player['x']+9,Player['y']+-9)!=1 and pyxel.pget(Player['x']+9,Player['y']+-8)!=1 and pyxel.pget(Player['x']+9,Player['y']+-7)!=1 and pyxel.pget(Player['x']+9,Player['y']+-6)!=1 and pyxel.pget(Player['x']+9,Player['y']+-5)!=1 and pyxel.pget(Player['x']+9,Player['y']+-4)!=1 and pyxel.pget(Player['x']+9,Player['y']+-3)!=1 and pyxel.pget(Player['x']+9,Player['y']+-2)!=1 and pyxel.pget(Player['x']+9,Player['y']+-1)!=1 and pyxel.pget(Player['x']+9,Player['y']+9)!=1 and pyxel.pget(Player['x']+9,Player['y']++1)!=1 and pyxel.pget(Player['x']+9,Player['y']++2)!=1 and pyxel.pget(Player['x']+9,Player['y']++3)!=1 and pyxel.pget(Player['x']+9,Player['y']++4)!=1 and pyxel.pget(Player['x']+9,Player['y']++5)!=1 and pyxel.pget(Player['x']+9,Player['y']++6)!=1 and pyxel.pget(Player['x']+9,Player['y']++7)!=1 and pyxel.pget(Player['x']+9,Player['y']++8)!=1 and pyxel.pget(Player['x']+9,Player['y']++9)!=1 and pyxel.pget(Player['x']+9,Player['y']+10)!=1 and pyxel.pget(Player['x']+9,Player['y']+11)!=1 and pyxel.pget(Player['x']+9,Player['y']+12)!=1 and pyxel.pget(Player['x']+9,Player['y']+13)!=1 and pyxel.pget(Player['x']+9,Player['y']+14)!=1): 
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
                Player['x']=Player['x']+Player['Vitesse']
                Player['Sens']='Droite'
    if (pyxel.pget(Player['x']-10,Player['y']-15)!=1 and pyxel.pget(Player['x']-10,Player['y']-15)!=1 and pyxel.pget(Player['x']-10,Player['y']-14)!=1 and pyxel.pget(Player['x']-10,Player['y']-13)!=1 and pyxel.pget(Player['x']-10,Player['y']-12)!=1 and pyxel.pget(Player['x']-10,Player['y']-11)!=1 and pyxel.pget(Player['x']-10,Player['y']-10)!=1 and pyxel.pget(Player['x']-9,Player['y']-9)!=1 and pyxel.pget(Player['x']-8,Player['y']-8)!=1 and pyxel.pget(Player['x']-7,Player['y']-7)!=1 and pyxel.pget(Player['x']-6,Player['y']-6)!=1 and pyxel.pget(Player['x']-5,Player['y']-5)!=1 and pyxel.pget(Player['x']-4,Player['y']-4)!=1 and pyxel.pget(Player['x']-3,Player['y']-3)!=1 and pyxel.pget(Player['x']-2,Player['y']-2)!=1 and pyxel.pget(Player['x']-1,Player['y']-1)!=1 and pyxel.pget(Player['x'],Player['y']-10)!=1 and pyxel.pget(Player['x']+1,Player['y']+1)!=1 and pyxel.pget(Player['x']+2,Player['y']+2)!=1 and pyxel.pget(Player['x']+3,Player['y']+3)!=1 and pyxel.pget(Player['x']+4,Player['y']+4)!=1 and pyxel.pget(Player['x']+5,Player['y']+5)!=1 and pyxel.pget(Player['x']+6,Player['y']+6)!=1 and pyxel.pget(Player['x']+7,Player['y']+7)!=1 and pyxel.pget(Player['x']+8,Player['y']+8)!=1 and pyxel.pget(Player['x']-10,Player['y']-10)!=1 and pyxel.pget(Player['x']+10,Player['y']+10)!=1 and pyxel.pget(Player['x']+10,Player['y']+11)!=1 and pyxel.pget(Player['x']+10,Player['y']+12)!=1 and pyxel.pget(Player['x']+10,Player['y']+13)!=1 and pyxel.pget(Player['x']+10,Player['y']+14)!=1): 
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
            Player['x']=Player['x']-Player['Vitesse']
            Player['Sens']='Gauche'
    if (pyxel.pget(Player['x']-10,Player['y']-16)!=1 and pyxel.pget(Player['x']-9,Player['y']-16)!=1 and pyxel.pget(Player['x']-8,Player['y']-16)!=1 and pyxel.pget(Player['x']-7,Player['y']-16)!=1 and pyxel.pget(Player['x']-6,Player['y']-16)!=1 and pyxel.pget(Player['x']-5,Player['y']-16)!=1 and pyxel.pget(Player['x']-4,Player['y']-16)!=1 and pyxel.pget(Player['x']-3,Player['y']-16)!=1 and pyxel.pget(Player['x']-2,Player['y']-16)!=1 and pyxel.pget(Player['x']-1,Player['y']-16)!=1 and pyxel.pget(Player['x']+9,Player['y']-16)!=1 and pyxel.pget(Player['x']+8,Player['y']-16)!=1 and pyxel.pget(Player['x']+7,Player['y']-16)!=1 and pyxel.pget(Player['x']+6,Player['y']-16)!=1 and pyxel.pget(Player['x']+5,Player['y']-16)!=1 and pyxel.pget(Player['x'],Player['y']-16)!=1 and pyxel.pget(Player['x']+1,Player['y']-16)!=1 and pyxel.pget(Player['x']+2,Player['y']-16)!=1 and pyxel.pget(Player['x']+3,Player['y']-16)!=1 and pyxel.pget(Player['x']+4,Player['y']-16)!=1): 
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z):
            Player['y']=Player['y']-Player['Vitesse']


    if Detectdeplace() == True and pyxel.btn(pyxel.KEY_SHIFT) != True :                     #Si le joueur ce deplace : il a des frames d'animations
        FrameDep(Player,24)
    else:                                                                                   #Sinon : il ne bouge pas
        Player['Frame']= 0
''' Ne marche pas doit être continuer (jsp dutout pk ça marche pas je vais tout casser )
def HitboxJBas():
    for X in range(-10,9):
        pyxel.pset(Player['x']+X,Player['y']+13,7)
        p=pyxel.pset(Player['x']+X,Player['y']+14,7)
        if p==1:
            return True
        else: 
            return False

def HitboxJHaut():
    for X in range(-10,9):
        pyxel.pset(Player['x']+X,Player['y']-15,7)
        p=pyxel.pget(Player['x']+X,Player['y']-16)
        if p==1:
            return True
        else: 
            return False 

def HitboxJDroite():
    for X in range(-16,14):
        pyxel.pset(Player['x']+X,Player['y']+9,7)
        p=pyxel.pget(Player['x']+X,Player['y']+14)
        if p==1:
            return True
        else: 
            return False 

def HitboxJGauche():
    for X in range(-16,14):
        pyxel.pset(Player['x']+X,Player['y']-10,7)
        p=pyxel.pget(Player['x']+X,Player['y']+14)
        if p==1:
            return True
        else: 
            return False 

'''
def PointdeVie():
    global Devmode
    if Player['PV']>=6:                                                   #Montre 3 coueur pour 6 pv
       pyxel.blt(Player['x']-75,Player['y']-80,2,128,16,44,16,1)
    
    if Player['PV']>=5:                                                   #Montre 2,5 coueur pour 5 pv
        pyxel.blt(Player['x']-75,Player['y']-80,2,128,16,39,16,1)
    
    if Player['PV']>=4:                                                   #Montre 2 coueur pour 4 pv
        pyxel.blt(Player['x']-75,Player['y']-80,2,128,16,29,16,1)

    if Player['PV']>=3:                                                   #Montre 1,5 coueur pour 3 pv
        pyxel.blt(Player['x']-75,Player['y']-80,2,128,16,23,16,1)

    if Player['PV']>=2:                                                   #Montre 1 coueur pour 2 pv
        pyxel.blt(Player['x']-75,Player['y']-80,2,128,16,13,16,1)

    if Player['PV']>=1:                                                   #Montre 0,5 coueur pour 1 pv
        pyxel.blt(Player['x']-75,Player['y']-80,2,128,16,6,16,1)


    if pyxel.btn(pyxel.KEY_W):                                            #Touche de test
        Player['PV']=6
    if Player['PV']>1 and Player['PV']<6:                                 #le joueur regenere ses PVs petit a petit
        Player['PV']=Player['PV']+0.001
    


def Course():                                                                   #Course et système de Stamina
    if pyxel.btn(pyxel.KEY_SHIFT) and Player['Fatigue'] != 1:                      #Le joueur cours si il n'est pas fatiguer
        Player['Vitesse']=4
        Player['Stamina']= Player['Stamina']-Player['StamDepletion']               #il perd de la stamina
        FrameDep(Player,12)
        if Player['Stamina']<=5:                                                   #Si il a - de 5 stamina : il devient fatiguer
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
    
def  drawSprint():
    if Player['Energisante']==0:
        if Player['Stamina']<=101 and Player['Stamina']>85 and Player['Fatigue']!=1:                   #Si la stamina restante est entre 100% et 80% et que le joueur n'est pas fatiguer :
            pyxel.blt(Player['x']-77,Player['y']-63,2,96,0,32,16,1)                                          #Montrer la barre remplie
        
        elif Player['Stamina']<=85 and Player['Stamina']>60 and Player['Fatigue']!=1:                  #Si la stamina restante est entre 80% et 60% et que le joueur n'est pas fatiguer:
            pyxel.blt(Player['x']-77,Player['y']-63,2,96,16,32,16,1)                                         #Montrer la barre asser remplie
        
        elif Player['Stamina']<=60 and Player['Stamina']>45 and Player['Fatigue']!=1:                  #Si la stamina restante est entre 60% et 45% et que le joueur n'est pas fatiguer:
            pyxel.blt(Player['x']-77,Player['y']-63,2,96,32,32,16,1)                                         #Montrer la barre à moitié vide
        
        elif Player['Stamina']<= 45 and Player['Stamina']>25 and Player['Fatigue']!=1:                 #Si la stamina restante est entre 45% et 25% et que le joueur n'est pas fatiguer:
            pyxel.blt(Player['x']-77,Player['y']-63,2,96,48,32,16,1)                                         #Montrer la barre presque vide
        
        elif Player['Stamina']<=25 and Player['Fatigue']!=1:                                           #Si la stamina restante est entre 25% et 0% et que le joueur n'est pas fatiguer:
            pyxel.blt(Player['x']-77,Player['y']-63,2,96,64,32,16,1)                                         #Montrer la barre rouge et vide
        
        elif Player['Fatigue']==1:                                                                     #Si le joueur est fatiguer peut importe sa stamina restante :
            pyxel.blt(Player['x']-77,Player['y']-63,2,96,80,32,16,1)                                         #Montrer la barre casser
    else:
        pyxel.blt(Player['x']-77,Player['y']-63,2,128,32,32,16,1)                                        #Montrer la barre casser

global Devmode
Devmode=0

def GODmode():
    global Devmode,Jour,debug
    if pyxel.btnp(pyxel.KEY_END):
        Devmode=Devmode+1
        Jour=Jour+1
    if Devmode>1 or Devmode<0:
        Devmode=0
    if Devmode==1:    
        Player['Stamina']=100
        Player['PV']=6
        debug=1

def BougeMap():                                                                          #Illusion de se déplacer sur la map
    global Xmap,Ymap
    if Player['x']>=635:                                                                      #Dès que le joueur est asser à droite de l'écran
        Xmap-=640                                                                                  #la tilemap va 1 écran à droite
        Player['x']-=630                                                                         #le joueur passe à gauche
        if WarioApparition() == True :
            Bot1['x']-=630
        Player['Xmob']+=1                                                                     #On change de salles sur la Map des Mobs
        MapMobSet()                                                                           #Ont met en place le preset cesser etre sur la map
        
    elif Player['x']<=5:                                                                      #Dès que le joueur est asser à gauche de l'écran
        Xmap=Xmap+640                                                                              #la tilemap va 1 écran à gauche
        Player['x']+=630                                                                           #le joueur passe à droite
        if WarioApparition() == True :
            Bot1['x']+=630
        Player['Xmob']-=1                                                                     #On change de salles sur la Map des Mobs
        MapMobSet()                                                                           #Ont met en place le preset cesser etre sur la map
        
    elif Player['y']>=315:                                                                    #Dès que le joueur est asser en haut de l'écran
        Ymap-=320                                                                                  #la tilemap va 1 écran en haut
        Player['y']-=310                                                                           #le joueur passe en bas
        if WarioApparition() == True :
            Bot1['y']-=310
        Player['Ymob']+=1                                                                     #On change de salles sur la Map des Mobsc
        MapMobSet()                                                                           #Ont met en place le preset cesser etre sur la map
        
    elif Player['y']<=5:                                                                      #Dès que le joueur est asser en bas de l'écran
        Ymap=Ymap+320                                                                              #la tilemap va 1 écran en bas
        Player['y']+=310                                                                           #le joueur passe en haut
        if WarioApparition() == True :
            Bot1['y']+=310
        Player['Ymob']-=1                                                                     #On change de salles sur la Map des Mobs
        MapMobSet()
    if Player['Ymob']==0 and Player['Xmob']==0:
        Bot1['Type']='Mort'
        Bot2['Type']='Mort'
        Bot3['Type']='Mort'
        Bot4['Type']='Mort'                                                                          #Ont met en place le preset cesser etre sur la map










def Immunite():
    if pyxel.frame_count %10 == 0:                                                            #L'immunité baisse toute les demi-seconde
        if Player['Immune']%2==0:                                                             #Avoir de l'immunité procure des effets rouge
            pyxel.pal()
        else:
            pyxel.pal()
        Player['Immune']-=1
    if Player['Immune']==-1:
        Player['Immune']=0

def Attaque():                                                                                #La fonction permettant l'attaque du Joueur
    global Coup
    if pyxel.btn(pyxel.KEY_ALT) and Player['Stamina'] >= 25 and Coup < 0:                         #Le joueur ne peut pas attaquer indéfiniment (La stamina et le cooldown sont ses limites)
        Player['Stamina']-=30
        Coup=3
        Player['Frappe']['Status']=True
    if Player['Frappe']['Status']==True :                                                         #Dès qu'il tappe : le compteur est mis a jour et les frames d'animations et calculs commence 
        if pyxel.frame_count%10==0:
            Coup-=1
        FrameDep(Player['Frappe'],24)
        if Player['Sens']=='Droite':                                                              #L'animation de la frappe suit le joueur (Pas de main détachées quoi)
            Player['Frappe']['x']=Player['x']+20
        else:
            Player['Frappe']['x']=Player['x']-20
        Player['Frappe']['y']=Player['y']
        Player['Frappe']['Sens']=Player['Sens']
        FrameDep(Player,24)
        Player['StamRegen']=0                                                                     #Si le joueur est en train de tapper, sa stamina ne regenere pas (Stress +++)
    if Coup==0:                                                                               #Dès que le compteur est fini, retour a l'état initial.
        Player['Frappe']['Status']=False
        Coup=-1
        Player['StamRegen']=0.5
    
def drawObjets():
    if Player['Objet']=='Jambon':
        if Player['Sens']=='Droite':
            pyxel.blt(Player['x'],Player['y']-8,2,0,40,16,16,1)
        else:
            pyxel.blt(Player['x']-16,Player['y']-8,2,0,40,-16,16,1)
    if JambonBot['Type']=='Lancer':
        pyxel.blt(JambonBot['x'],JambonBot['y'],2,0,40,16,16,1)
    if Player['Objet']=='Boisson':
        if Player['Sens']=='Droite':
            pyxel.blt(Player['x'],Player['y']-8,2,0,56,16,16,1)
        else:
            pyxel.blt(Player['x']-16,Player['y']-8,2,0,56,-16,16,1)

def Objets():
    if Player['Objet']=='Jambon':
        if pyxel.btnp(pyxel.KEY_R) :
            JambonBot['Type']='Lancer'
            JambonBot['x']=Player['x']-8
            JambonBot['y']=Player['y']-8
            Player['Objet']=None
    if JambonBot['Type']=='Lancer':
        if Bot1['Type']=='Arabe':
            JambonLancer(JambonBot,Bot1)
        if Bot2['Type']=='Arabe':
            JambonLancer(JambonBot,Bot2)
        if Bot3['Type']=='Arabe':
            JambonLancer(JambonBot,Bot3)
        else:
            JambonLancer(JambonBot,Bot4)
    if Player['Objet']=='Boisson':
        if pyxel.btnp(pyxel.KEY_R) :
            Player['Energisante']=10
    if Player['Energisante']>0 and pyxel.frame_count%20==0:
        Player['Energisante']-=1
        Player['Stamina']=100
        Player['Objet']=None
        


'''
                                                                                ██████╗░░█████╗░████████╗
                                                                                ██╔══██╗██╔══██╗╚══██╔══╝
                                                                                ██████╦╝██║░░██║░░░██║░░░
                                                                                ██╔══██╗██║░░██║░░░██║░░░
                                                                                ██████╦╝╚█████╔╝░░░██║░░░
                                                                                ╚═════╝░░╚════╝░░░░╚═╝░░░
'''
global StunCauch
StunCauch=0

Bot1=dict()
Bot1['x']=0                                                                    #Indique l'emplacement X du Bot1
Bot1['y']=0                                                                    #Indique l'emplacement Y du Bot1
Bot1['Sens']='Droite'
Bot1['Frame']= 0
Bot1['Type']='Mort'
Bot1['Vitesse']=0
Bot1['PV']=0


Bot2=dict()
Bot2['x']=0                                                                    #Indique l'emplacement X du Bot2
Bot2['y']=0                                                                    #Indique l'emplacement Y du Bot2
Bot2['Sens']='Droite'
Bot2['Frame']=0
Bot2['Type']='Mort'
Bot2['Vitesse']=0
Bot2['PV']=0

Bot3=dict()
Bot3['x']=0                                                                    #Indique l'emplacement X du Bot3
Bot3['y']=0                                                                    #Indique l'emplacement Y du Bot3
Bot3['Sens']='Droite'
Bot3['Frame']=0
Bot3['Type']='Mort'
Bot3['Vitesse']=0
Bot3['PV']=0

Bot4=dict()
Bot4['x']=0                                                                    #Indique l'emplacement X du Bot4
Bot4['y']=0                                                                    #Indique l'emplacement Y du Bot4
Bot4['Sens']='Droite'
Bot4['Frame']=0
Bot4['Type']='Mort'
Bot4['Vitesse']=0
Bot4['PV']=0


bouledefeu=dict()
bouledefeu['x']=0
bouledefeu['y']=0
bouledefeu['Type']='Mort'
bouledefeu['Sens']='Droite'
bouledefeu['Frame']=0

def bot(entity):                                                                 #Fait en sorte que les bots pourusivent le joueur en fonction de leur vitesse 
    if Player['x']-entity['x'] >= 0:                                                 #si le joueur est a droite : le bot va a droite
        entity['Sens']='Droite'
        entity['x']=entity['x']+entity['Vitesse']
    if Player['x']-entity['x'] <= 0:                                                 #si le joueur est a gauche : le bot va a gauche
        entity['Sens']='Gauche'
        entity['x']=entity['x']-entity['Vitesse']
    if Player['y']-entity['y'] >= 0:                                                 #si le joueur est en haut : le bot va en haut
        entity['y']=entity['y']+entity['Vitesse']
    if Player['y']-entity['y'] <= 0:                                                 #si le joueur est en bas : le bot va en bas
        entity['y']=entity['y']-entity['Vitesse']
    FrameDep(entity,36)
        
        
        
        
def types(entity):                                                              #Utilise les différentes fonction selon le type du bot
    global XYmap
    if entity['Type']=='Phantom':                                               #Détecte si le bot est un Fantome
        Phantom(entity)
    if entity['Type']=='Zombie':                                                #Détecte si le bot est un Zombie
        Zombie(entity)
    if entity['Type']=='Arabe':                                                 #Détecte si le bot est un Arabe
        Arabe(entity)
    if entity['Type']=='Mage':                                                  #Détecte si le bot est un Mage
        Mage(entity)
    if entity['Type']=='Golem':                                                 #Détecte si le bot est un Golem
        Golem(entity)
    if entity['Type']=='Cauchemare':                                            #Détecte si le bot est un Cauchemare
        Cauchemare(entity)
    if entity['Type']=='Wario':                                                 #Wario (Pas early acces)
        wario()
    if entity['PV']<=0:
        entity['Type']='Mort'
        if entity==Bot1:
            XYmap['Bot1Map']['Type']='Mort'
        if entity==Bot2:
            XYmap['Bot2Map']['Type']='Mort'
        if entity==Bot3:
            XYmap['Bot3Map']['Type']='Mort'
        else:
            XYmap['Bot4Map']['Type']='Mort'
        entity['PV']=1
    
def boulelance(entity):
    FrameDep(bouledefeu,16)
    if bouledefeu['Type']=='Lancer':                                                 #dès que la boule de feu est lancer,
        Draw32px(bouledefeu,160,128,-1,0)                                            #elle existe
        bouledefeu['x']+=bouledefeu['vx']                                            #Elle va a une direction donnée
        bouledefeu['y']+=bouledefeu['vy']
        if Player['x']<bouledefeu['x']+14 and Player['x']>bouledefeu['x']-14 and Player['y']>bouledefeu['y']-14 and Player['y']<bouledefeu['y']+14 and Player['Immune'] == 0:
            pyxel.play(0,10)                                                         #Infliger des dégats si le joueur est proche (+ Son)
            Player['PV']-=1
            bouledefeu['Type']='Mort'                                                   #Meur si elle réussit a faire des dégats
        for i in range(int(bouledefeu['x']),int(bouledefeu['vx'])):
            for j in range(int(bouledefeu['y']),int(bouledefeu['vy'])):
                if pyxel.pget(i,j)==5:                                               #essai de faire qu'elle ne traverse pas les mur  
                    bouledefeu['Type']='Mort'
        if Player['Frappe']['Status']==True and Player['Frappe']['x']<bouledefeu['x']+30 and Player['Frappe']['x']>bouledefeu['x']-30 and Player['Frappe']['y']>bouledefeu['y']-32 and Player['Frappe']['y']<bouledefeu['y']+32:
            bouledefeu['Type']='Mort'                                                #Si le joueur réussit a tapper la boule de feu : elle disparait
            pyxel.play(0,4)
    
def Phantom(entity):                                                            #Fait les caractéristique du Fantome
    entity['Vitesse']=random.uniform(0.05,1)+random.uniform(0.05,1)             #Sa vitesse change aléatoirement entre 0.1 et 2.
    Draw32px(entity,224,0,-1,1)
    bot(entity)
    if Player['x']<entity['x']+30 and Player['x']>entity['x']-30 and Player['y']>entity['y']-30 and Player['y']<entity['y']+30 and pyxel.frame_count %5==0 and Player['Immune'] == 0:
        Player['PV']-=1                                                         #Infliger des dégats si le joueur est proche (+ Son)
        Player['Immune']=3
        pyxel.play(0,1)
    if Detectflash(entity):                                                     #Si le Phantom se fait Flash : Il devient Mort
        entity['PV']=0
        pyxel.play(0,3)
        
def Zombie(entity):                                                             #Fait les caractéristique du Zombie
    if Player['Frappe']['Status']==False:
        entity['Vitesse']=1.25
    Draw32px(entity,128,0,1,1)
    bot(entity)
    if Player['x']<entity['x']+26 and Player['x']>entity['x']-26 and Player['y']>entity['y']-28 and Player['y']<entity['y']+28 and pyxel.frame_count %5==0 and Player['Immune'] == 0:
        Player['PV']-=1                                                         #Infliger des dégats si le joueur est proche (+ Son)
        Player['Immune']=3
        pyxel.play(0,1)
    if Player['Frappe']['Status']==True and Player['Frappe']['x']<entity['x']+30 and Player['Frappe']['x']>entity['x']-30 and Player['Frappe']['y']>entity['y']-32 and Player['Frappe']['y']<entity['y']+32:
        if entity['Vitesse']==1.25:
            entity['PV']-=1
        entity['Vitesse']=-2                                                   #Si le zombie se fait tapper : il recul
        pyxel.play(0,1)
        


def Arabe(entity):                                                             #Fait les caractéristique de l'Arabe
    if Player['Frappe']['Status']==False:
        entity['Vitesse']=1.75
    Draw32px(entity,96,0,1,1)
    bot(entity)
    if Player['x']<entity['x']+28 and Player['x']>entity['x']-28 and Player['y']>entity['y']-28 and Player['y']<entity['y']+28:
        pyxel.play(0,6)                                                         #Infliger des dégats si le joueur est proche (+ Son)
        Player['PV']-=4
        Player['Immune']=5
        entity['PV']=0                                                              #Meur si il réussit a faire des dégats (Comme un Kamikaze)
    if Player['Frappe']['Status']==True and Player['Frappe']['x']<entity['x']+30 and Player['Frappe']['x']>entity['x']-30 and Player['Frappe']['y']>entity['y']-32 and Player['Frappe']['y']<entity['y']+32:
        entity['Vitesse']=-0.75                                                 #Si le zombie se fait tapper : il recul (moins loin que le zombie)
        pyxel.play(0,1)
        

def Mage(entity):                                                                 #Fait les caractéristique de Mage
    boulelance(entity)
    entity['Vitesse']=0.5
    Draw32px(entity,192,0,1,1)
    bot(entity)
    if Player['x']<entity['x']+26 and Player['x']>entity['x']-26 and Player['y']>entity['y']-28 and Player['y']<entity['y']+28 and pyxel.frame_count %5==0 and Player['Immune'] == 0:
        Player['PV']-=2                                                         #Infliger des dégats si le joueur est proche (+ Son)
        Player['Immune']=3
        pyxel.play(0,1)
    if pyxel.frame_count % 50 == 0 :                                            #Toutes les 2.5 secondes, le mage fait :
        pyxel.play(0,7)                                                             #un son
        bouledefeu['Type']='Lancer'                                                 #lance la boule de feu
        bouledefeu['vx']=(Player['x']-entity['x'])*0.05                             #trouve la direction pour la boule de feu
        bouledefeu['vy']=(Player['y']-entity['y'])*0.05
        bouledefeu['y']=entity['y']                                                 #et la fait partir de son corps
        bouledefeu['x']=entity['x']
    if Player['Frappe']['Status']==True and Player['Frappe']['x']<entity['x']+30 and Player['Frappe']['x']>entity['x']-30 and Player['Frappe']['y']>entity['y']-32 and Player['Frappe']['y']<entity['y']+32:
        entity['PV']=0                                                 #Si le zombie se fait tapper : il recul (moins loin que le zombie)
        pyxel.play(0,1)

def Golem(entity):                                                             #Fait les caractéristique du golem
    entity['Vitesse']=0.05                                                        #Il est immobile
    Draw64px(entity,192,128,4)
    bot(entity)
    if Player['x']<entity['x']+36 and Player['x']>entity['x']-36 and Player['y']>entity['y']-50 and Player['y']<entity['y']+50 and pyxel.frame_count %10==0:
        Player['PV']-=0.5                                                       #Infliger des dégats si le joueur est proche (+ Son)
        pyxel.play(0,4)
    
def Cauchemare(entity):                                                             #Fait les caractéristique du Cauchemare
    global StunCauch
    entity['Vitesse']=3.25
    Draw32px(entity,160,0,1,1)
    if StunCauch<=0:                                                            #Si le Cauchemare n'est pas Stun (Flash) alors il peut bouger
        bot(entity)
    elif pyxel.frame_count%10==0:
        StunCauch-=1                                                            #Timer du Stun qui baisse
    if Player['x']<entity['x']+16 and Player['x']>entity['x']-16 and Player['y']>entity['y']-25 and Player['y']<entity['y']+25 and pyxel.frame_count %2==0:
        Player['PV']-=0.5                                                       #Infliger des dégats si le joueur est proche (+ Son)
        pyxel.play(0,5)
    if Detectflash(entity) and pyxel.frame_count%5==0 :
        StunCauch+=3                                                            #Si le Cauchemare se fait Flash : Il devient immobile pendant 3x secondes
    if pyxel.frame_count%20==0:
        entity['PV']-=1

def wario():                                                                    #Le wario n'est pas fini pour l'early acces
    boulelance(Bot1)
    Bot2['Type']='Mort'
    Bot3['Type']='Mort'
    Bot1['Vitesse']=2.8
    if pyxel.frame_count%36==18:
        pyxel.play(1,9)
    if pyxel.frame_count % 50 == 0 :
        pyxel.play(0,7)
        bouledefeu['Type']='Lancer'
        bouledefeu['vx']=(Player['x']-Bot1['x'])*0.075
        bouledefeu['vy']=(Player['y']-Bot1['y'])*0.075
        bouledefeu['y']=Bot1['y']
        bouledefeu['x']=Bot1['x']
    Draw64px(Bot1,32,128,11)
    bot(Bot1)
    if Player['x']<Bot1['x']+36 and Player['x']>Bot1['x']-36 and Player['y']>Bot1['y']-40 and Player['y']<Bot1['y']+40 and pyxel.frame_count %20==0:
        Player['PV']-=1.5                                                       #Infliger des dégats si le joueur est proche (+ Son)
        pyxel.play(0,4)


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
global Jour
Jour=0

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
        pyxel.blt(Player['x']-80,Player['y']-50,2,64,0,32,16,1)                           #le barre de pile est pleine (vert foncé)
        
    if Player['Batterie']<=80:                                                       #Si la batterie est entre 80% et 60%:
        pyxel.blt(Player['x']-80,Player['y']-50,2,64,16,32,16,1)                          #le barre de pile est 1 barre vide (vert clair)
        
    if Player['Batterie']<=60:                                                       #Si la batterie est entre 60% et 40%:
        pyxel.blt(Player['x']-80,Player['y']-50,2,64,32,32,16,1)                          #le barre de pile est 2 barres vide (jaune)
        
    if Player['Batterie']<=40:                                                       #Si la batterie est entre 40% et 20%:
        pyxel.blt(Player['x']-80,Player['y']-50,2,64,48,32,16,1)                          #le barre de pile à 2 barres restantes (orange)
        
    if Player['Batterie']<=20:                                                       #Si la batterie est à 20% ou moins:
        pyxel.blt(Player['x']-80,Player['y']-50,2,64,64,32,16,1)                          #le barre de pile à 1 barre restante (rouge)

        
        

#prototype lampe V1
def Lampe():                                                                    #Affiche une partie de la map autour du joueur en fonction de la visibilité 
    global Jour
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





global Porte
Porte=0

Objet=dict()
Objet['x']=0
Objet['y']=0
Objet['Type']=None
Objet['Rammasser']=0

JambonBot=dict()
JambonBot['x']=0
JambonBot['y']=0
JambonBot['Type']='Mort'

Levier1={'Status':0}                                                         #statut du levier (on/off)
Levier2={'Status':0}                                                         #statut du levier (on/off)
Levier3={'Status':0}                                                         #statut du levier (on/off)



def typesobj(objet):                                                              #Utilise les différentes fonction selon le type du bot 
    if objet['Type']=='Levier1':                                                #Détecte si l'objet est le 1er levier
        Levier(objet,1)
    if objet['Type']=='Levier2':                                                #Détecte si l'objet est le 2e levier 
        Levier(objet,2)
    if objet['Type']=='Levier3':                                                #Détecte si l'objet est le 3e levier
        Levier(objet,3)
    if objet['Type']=='Boisson':                                                #Détecte si l'objet est une boisson
        Boisson(objet)
    if objet['Type']=='Batterie':                                               #Détecte si l'objet est une batterie
        Pile(objet)
    if objet['Type']=='Jambon':                                                 #Détecte si l'objet est du jambon
        Jambon(objet)
    if objet['Type']=='Coeur':
        Coeur(objet)

def Levier(objet,nb):
    if nb==1:
        LevierDraw(objet,Levier1)
        LevierConfig(objet,Levier1)
    elif nb==2:
        LevierDraw(objet,Levier2)
        LevierConfig(objet,Levier2)
    else:
        LevierDraw(objet,Levier3)
        LevierConfig(objet,Levier3)

def LevierDraw(objet,L):                                              #affiche les leviers sur la map                       
    if L['Status']==0:                                                            #postition du levioer (on/off)
        pyxel.blt(objet['x'],objet['y'],0,136,72,24,16,14)
    if L['Status']==1:
        pyxel.blt(objet['x']+6,objet['y'],0,142,88,24,23,14)

def LevierConfig(objet,L):                                            #Permet l'activation des  leviers
    global Porte
    if Player['x']>objet['x']-30 and Player['x']<objet['x']+30 and Player['y']>objet['y']-30 and Player['y']<objet['y']+30: #si le joueur est pret du levier 
            if pyxel.btnp(pyxel.KEY_E) and L['Status']!=1:
                L['Status']=1                                           #active le levier
                Porte+=1

def Jambon(objet):
    if Player['x']>objet['x']-30 and Player['x']<objet['x']+30 and Player['y']>objet['y']-30 and Player['y']<objet['y']+30: #si le joueur est pret du levier 
            if pyxel.btnp(pyxel.KEY_E) :
                Objet['Type']=Player['Objet']
                XYmap['ObjetMap']['Type']=Player['Objet']
                Player['Objet']='Jambon'
    pyxel.blt(objet['x'],objet['y'],2,0,40,16,16,1)

    
def JambonLancer(Jambon,Arabe):
    if Arabe['x']-Jambon['x'] >= 0:                                                 #si le joueur est a droite : le bot va a droite
        Jambon['x']=Jambon['x']+2
    elif Arabe['x']-Jambon['x'] <= 0:                                                 #si le joueur est a gauche : le bot va a gauche
        Jambon['x']=Jambon['x']-2
    elif Arabe['y']-Jambon['y'] >= 0:                                                 #si le joueur est en haut : le bot va en haut
        Jambon['y']=Jambon['y']+2
    elif Arabe['y']-Jambon['y'] <= 0:                                                 #si le joueur est en bas : le bot va en bas
        Jambon['y']=Jambon['y']-2
    if Arabe['x']<Jambon['x']+28 and Arabe['x']>Jambon['x']-28 and Arabe['y']>Jambon['y']-28 and Arabe['y']<Jambon['y']+28:
        Jambon['Type']='Mort'
        Arabe['PV']=0
        pyxel.play(0,3)
        
def Coeur(objet):
    if Player['x']>objet['x']-30 and Player['x']<objet['x']+30 and Player['y']>objet['y']-30 and Player['y']<objet['y']+30: #si le joueur est pret du levier 
            if pyxel.btnp(pyxel.KEY_E) :
                objet['Type']=None
                XYmap['ObjetMap']['Type']=None
                Player['PV']+=2
    pyxel.blt(objet['x'],objet['y'],2,16,56,16,16,1)

def Pile(objet):
    if Player['x']>objet['x']-30 and Player['x']<objet['x']+30 and Player['y']>objet['y']-30 and Player['y']<objet['y']+30: #si le joueur est pret du levier 
            if pyxel.btnp(pyxel.KEY_E) :
                objet['Type']=None
                XYmap['ObjetMap']['Type']=None
                Player['Batterie']=100
    pyxel.blt(objet['x'],objet['y'],2,16,40,16,16,1)
    
def Boisson(objet):
    if Player['x']>objet['x']-30 and Player['x']<objet['x']+30 and Player['y']>objet['y']-30 and Player['y']<objet['y']+30: #si le joueur est pret du levier 
            if pyxel.btnp(pyxel.KEY_E) :
                Objet['Type']=Player['Objet']
                XYmap['ObjetMap']['Type']=Player['Objet']
                Player['Objet']='Boisson'
    pyxel.blt(objet['x'],objet['y'],2,0,56,16,16,1)
    


def Portail():                                                                #porte
    global Porte
    if  Player['Xmob']==0 and Player['Ymob']==0:                        #si le joueur est dans la salle de la porte 
        if Porte!=4:                                                        #si trois levier ne sont pas activer  
            pyxel.blt(288,-6,0,96,120,64,50,3)                               #fermer la porte
        if Porte==1:
            pyxel.blt(288,17,0,96,175,60,8,3) 
        if Porte==2:
            pyxel.blt(288,17,0,96,191,60,8,3)
        if Porte==3:
            pyxel.blt(288,17,0,96,207,60,8,3)
        if Porte==3:
            if Player['x']>270 and Player['y']>30 and  Player['x']<370 and Player['y']<65:
                if pyxel.btnp(pyxel.KEY_E):
                    Porte=4
        if Porte==4:
            pyxel.blt(288,-6,0,176,0,64,70,3)   
        if pyxel.btnp(pyxel.KEY_RCTRL):
            Porte=Porte+1
        if Porte>4:
            Porte=0

def Boss_Fight():#a continuer 
    global Porte,start
    if Porte==4:
        if Player['x']>295 and Player['y']>0 and  Player['x']<350 and Player['y']<25:
            start=4



'''    
                                                                                ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
                                                                                ████╗░████║██╔════╝████╗░██║██║░░░██║
                                                                                ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
                                                                                ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
                                                                                ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
                                                                                ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
'''
global Choix
Choix=1
def EarlyAcces(x,y):
        pyxel.blt(x,y,2,160,112,32,32,1)
        pyxel.blt(x+33*1,y,2,32,112,32,32,1)
        pyxel.blt(x+33*2,y,2,128,176,32,32,1)
        pyxel.blt(x+33*3,y,2,160,144,32,32,1)
        pyxel.blt(x+33*4,y,2,128,208,32,32,1)

        pyxel.blt(x+33*6,y,2,32,112,32,32,1)
        pyxel.blt(x+33*7,y,2,96,112,32,32,1)
        pyxel.blt(x+33*8,y,2,96,112,32,32,1)
        pyxel.blt(x+33*9,y,2,160,112,32,32,1)
        pyxel.blt(x+33*10,y,2,162,176,32,32,1)

def HauntedDreams(x,y):
        pyxel.blt(x,y,2,32,144,32,32,1)
        pyxel.blt(x+33*1,y,2,32,112,32,32,1)
        pyxel.blt(x+33*2,y,2,224,176,32,32,1)
        pyxel.blt(x+33*3,y,2,224,144,32,32,1)
        pyxel.blt(x+33*4,y,2,192,176,32,32,1)
        pyxel.blt(x+33*5,y,2,160,112,32,32,1)
        pyxel.blt(x+33*6,y,2,128,112,32,32,1)
    
        pyxel.blt(x+33*8,y,2,128,112,32,32,1)
        pyxel.blt(x+33*9,y,2,128,176,32,32,1)
        pyxel.blt(x+33*10,y,2,160,112,32,32,1)
        pyxel.blt(x+33*11,y,2,32,112,32,32,1)
        pyxel.blt(x+33*12,y,2,192,144,32,32,1)
        pyxel.blt(x+33*13,y,2,162,176,32,32,1)

def AnimHD():
    if pyxel.frame_count >137 and pyxel.frame_count <140:
        pyxel.pal(7,6)
    if pyxel.frame_count >140 and pyxel.frame_count <143:
        pyxel.pal(7,12)  
    if pyxel.frame_count >143 and pyxel.frame_count <146:
        pyxel.pal(7,5) 
    if pyxel.frame_count >146 and pyxel.frame_count <149:
        pyxel.pal(7,1) 
    if pyxel.frame_count >149 and pyxel.frame_count <170:
        pyxel.pal(7,0)

def AnimWario():
    if pyxel.frame_count >170 and pyxel.frame_count <185 :
        pyxel.pal()
        pyxel.blt(280,145,1,32,128,64,64,11)
    if pyxel.frame_count >185  and pyxel.frame_count <195:
        pyxel.blt(280,145,1,32,192,64,64,11)
    if pyxel.frame_count >195  and pyxel.frame_count <205:
        pyxel.cls(0)
        pyxel.blt(280,145,1,32,128,64,64,11)
    if pyxel.frame_count >205  and pyxel.frame_count <215:
        pyxel.blt(280,145,1,32,192,64,64,11)
    if pyxel.frame_count >215  and pyxel.frame_count <225:
        pyxel.cls(0)
        pyxel.blt(280,145,1,32,128,64,64,11)
    if pyxel.frame_count >225  and pyxel.frame_count <245:
        pyxel.blt(280,145,1,32,192,64,64,11)
    if pyxel.frame_count >245  and pyxel.frame_count <300:
        pyxel.cls(0)
        pyxel.blt(280,145,1,32,128,64,64,11)




###################
def Introduction():
    global start
    
    if pyxel.frame_count <60 :
        EarlyAcces(160,160)
        pyxel.text(0,0,'Version 0.73',14)
    
    if pyxel.frame_count >90  and pyxel.frame_count <170:
        pyxel.cls(0)
        HauntedDreams(90,160)
    
    AnimHD()
    AnimWario()
    if pyxel.frame_count >260:
        pyxel.cls(0)
        pyxel.pal(7,0)
        start=0

    if pyxel.btnp(pyxel.KEY_SPACE) :
        start=0
        pyxel.pal()


def menuanime():
    if pyxel.frame_count >270  and pyxel.frame_count <275:
       pyxel.pal(7,1)
    if pyxel.frame_count >275  and pyxel.frame_count <280:
        pyxel.pal(7,5)
    if pyxel.frame_count >280  and pyxel.frame_count <285:
        pyxel.pal(7,12)
    if pyxel.frame_count >285  and pyxel.frame_count <290:
        pyxel.pal(7,6)
    if pyxel.frame_count >290: 
        pyxel.pal() 

def startgame(y):
    pyxel.blt(150,y,2,162,176,32,32,1)
    pyxel.blt(183,y,2,192,176,32,32,1)
    pyxel.blt(216,y,2,32,112,32,32,1)
    pyxel.blt(249,y,2,130,176,32,32,1)
    pyxel.blt(283,y,2,192,176,32,32,1)
    pyxel.blt(331,y,2,224,112,32,32,1)
    pyxel.blt(364,y,2,32,112,32,32,1)
    pyxel.blt(397,y,2,192,144,32,32,1)
    pyxel.blt(430,y,2,160,112,32,32,1)
def options(y):
    pyxel.blt(200,y,2,32,176,32,32,1)
    pyxel.blt(233,y,2,64,176,32,32,1)
    pyxel.blt(266,y,2,192,176,32,32,1)
    pyxel.blt(289,y,2,64,144,32,32,1)
    pyxel.blt(312,y,2,32,176,32,32,1)
    pyxel.blt(345,y,2,224,144,32,32,1)
    pyxel.blt(378,y,2,162,176,32,32,1)
def quitgames(y):
    pyxel.blt(170,y,2,96,176,32,32,1)
    pyxel.blt(203,y,2,224,176,32,32,1)
    pyxel.blt(226,y,2,64,144,32,32,1)
    pyxel.blt(249,y,2,192,176,32,32,1)   
    pyxel.blt(306,y,2,224,112,32,32,1)
    pyxel.blt(339,y,2,32,112,32,32,1)
    pyxel.blt(372,y,2,192,144,32,32,1)
    pyxel.blt(405,y,2,160,112,32,32,1)







###################
def menu():                                                                     #Le Menu principale dans sont intégralité : Jouer et Quitter pour l'instant
    global start,Choix
    ys=75
    yo=150
    yq=225
    pyxel.cls(0)

    startgame(ys)
    options(yo)
    quitgames(yq)
      
    if pyxel.btnp(pyxel.KEY_DOWN):
        Choix=Choix+1
    if pyxel.btnp(pyxel.KEY_UP):
        Choix=Choix-1
    if Choix>=4:
        Choix=1
    if Choix<=0:
        Choix=3   
    if Choix==1:
        
        if pyxel.frame_count % 30 >= 0 and pyxel.frame_count % 30 < (30//4) :
            pyxel.blt(130,ys+7,2,0,8,16,16,0)
            pyxel.blt(465,ys+7,2,16,8,16,16,0)   
        else :
            pass
        
        if pyxel.btn(pyxel.KEY_RETURN): 
            start=1
            Player['PV']=6

    if Choix==2:
        
        if pyxel.frame_count % 30 >= 0 and pyxel.frame_count % 30 < (30//4) :
            pyxel.blt(180,yo+7,2,0,8,16,16,0)
            pyxel.blt(418,yo+7,2,16,8,16,16,0)
        else :
            pass

        if pyxel.btn(pyxel.KEY_RETURN): 
            start=-1
    
    if Choix==3:
        
        if pyxel.frame_count % 30 >= 0 and pyxel.frame_count % 30 < (30//4) :
            pyxel.blt(150,yq+7,2,0,8,16,16,0)
            pyxel.blt(445,yq+7,2,16,8,16,16,0)
        else :
            pass

        if pyxel.btn(pyxel.KEY_RETURN): 
            pyxel.quit()








#############
global option
option=1
##############
def option():
    global start,option
    pyxel.cls(0)
    if option==1:
        PageI()
    if option==2:
        PageII()
    if option==3:
        PageIII()
    if option==4:
        PageIIII()
    if pyxel.btnp(pyxel.KEY_RIGHT) :
        if option!=4 :
            option+=1
        else : start=0
    if pyxel.btnp(pyxel.KEY_LEFT):
        if option!=1 :
            option-=1
        else :
            start=0







def PageI():
    pyxel.text(275,20,str("Touches"),4)
    pyxel.text(10,50,str("Pour Accelerer Appuyer sur shift gauche"),3)
    pyxel.text(10,70,"zqsd et fleche directionnel pour se deplacer ",3)
    pyxel.text(10,110,"F pour le flash (rester appuyer, consomme beaucoup de batterie et permet d'impacter certain mob )",3)
    pyxel.text(10,90,"shift pour courrir (consomme de l'endurence)",3)
    pyxel.text(10,310,"tab pour retourner au menu / ouvrir le menu",3)
    pyxel.text(10,130,"ALT pour frapper (consomme de l'endurence)",3)
    pyxel.text(10,150,"E pour interagir / prendre un objet",3)
    pyxel.text(10,170,"R pour utiliser l'objet dans les mains",3)
    pyxel.text(5,340,"<--   Aller au menu",7)
    pyxel.text(580,340,"Les Mobs   -->",7)



def PageII():
    pyxel.text(275,20,str("Mobs"),4)
    pyxel.circ(26,66,18,1)
    pyxel.text(50,50,str("Le Zombie :"),4)
    pyxel.blt(10,50,1,128,0,32,32,1)
    pyxel.text(60,60,str("Ennemis commun, il attaque si vous êtes trop pres."),3)
    pyxel.text(60,70,str("Vous devez le tuez en l'attaquant (attention certain peuvent etre coriace)"),3)
    
    pyxel.circ(26,106,18,1)
    pyxel.text(50,90,str("Le Phantome :"),4)
    pyxel.blt(10,90,1,224,0,-32,32,1)
    pyxel.text(60,100,str("Ennemis commun, il attaque si vous êtes trop pres et ne peut pas etre attaquer"),3)
    pyxel.text(60,110,str("Les Phantomes n'aiment vraiment pas la lumiere forte donc flasher le pour qu'il parte"),3)
    
    pyxel.circ(26,146,18,1)
    pyxel.text(50,130,str("L'Arabe :"),4)
    pyxel.blt(10,130,1,96,0,32,32,1)
    pyxel.text(60,140,str("Ennemis rare, il s'explose sur vous vous causant d'enorme degats."),3)
    pyxel.text(60,150,str("Meme si vous pouver le taper, il partira uniquement si vous lui lancer du jambon."),3)
    
    pyxel.circ(26,186,18,1)
    pyxel.text(50,170,str("Le Mage :"),4)
    pyxel.blt(13,170,1,192,0,32,32,1)
    pyxel.text(60,180,str("Ennemis rare, il vous lance des boule de magies."),3)
    pyxel.text(60,190,str("Meme si il sont dangereux, il ne peuvent pas resister plus d'un coup."),3)
    pyxel.text(60,200,str("Aussi, ses boule de magies peuvent etre arretes si elles ressoivent un coup."),3)
    
    pyxel.circ(26,226,18,1)
    pyxel.text(50,210,str("Le Cauchemare :"),4)
    pyxel.blt(10,213,1,160,0,32,32,1)
    pyxel.text(60,220,str("Ennemis unique, il se jettera sur vous a une vitesse tres rapide."),3)
    pyxel.text(60,230,str("Vous ne pouver pas le tuer, juste attender qu'il parte. (un chrono indique le temps restant en haut a gauche)"),3)
    pyxel.text(60,240,str("Etant un cauchemare, il ne peut pas se deplacer dans la lumiere forte, flasher le pour l'arreter temporairement."),3)
    
    pyxel.circ(42,286,34,2)
    pyxel.text(82,250,str("Le Golem :"),4)
    pyxel.blt(10,254,1,192,128,64,64,4)
    pyxel.text(92,260,str("Se mastodonte Bbouge extremement lentement mais vous bloque votre chemin."),3)
    pyxel.text(92,270,str("Il ne peut pas etre tuer mais vous attaque si vous vous raprochez trop de lui."),3)
    pyxel.text(92,280,str("Si un mastodonte est present, il y a surement quelquechose de cacher deriere lui."),3)
    
    
    pyxel.text(5,340,"<--   Les Touches",7)
    pyxel.text(550,340,"Les Mechaniques   -->",7)




def PageIII():
    pyxel.text(275,20,str("Mechaniques"),4)
    pyxel.text(10,50,str("L'Endurence :"),4)
    pyxel.blt(10,60,2,96,0,32,16,1)
    pyxel.text(60,60,str("L'endurence est une utilisee pour 2 actions : Courir et Attaquer."),3)
    pyxel.text(60,70,str("L'endurence doit etre utiliser avec moderation ou vous deviendrer fatiguer."),3)
    pyxel.text(60,80,str("Si vous etes fatiguer, votre barre sera fissurer et vous ne pourriez plus courir jusqu'a n'etre plus fatiguer."),3)
    pyxel.text(60,90,str("Cependant, vous pouvez boire une boisson energisante pour avoir de l'endurence illimiter pendant un court temps."),3)
    
    pyxel.text(10,100,str("La batterie :"),4)
    pyxel.blt(10,110,2,64,0,32,16,1)
    pyxel.text(60,110,str("C'est une ressource essentielle a la survie."),3)
    pyxel.text(60,120,str("La batterie de votre lampe est utiliser avec le temps ou si vous flashez."),3)
    pyxel.text(60,130,str("Si vous tomber a 0 de batterie, vous mourrez donc utilisez la avec soin !"),3)
    pyxel.text(60,140,str("Le seul moyen de regenerer sa batterie est avec des batteries trouvers sur le sol."),3)
    
    pyxel.text(10,150,str("La sante :"),4)
    pyxel.blt(10,160,2,128,16,32,16,1)
    pyxel.text(60,160,str("Assez simple a comprendre : si vous tombez a 0, vous mourrez."),3)
    pyxel.text(60,170,str("La sante est baisser par les actions des mobs sur vous, attaque ou explosion."),3)
    pyxel.text(60,180,str("Le seul moyen de regenerer sa sante est par les coeurs se trouvant par terre."),3)
    
    pyxel.text(275,200,str("Les Objets"),4)
    pyxel.text(10,230,str("La batterie :"),4)
    pyxel.blt(18,240,2,16,40,16,16,1)
    pyxel.text(60,240,str("Les batteries seront utilisee des que vous la prennez."),3)
    pyxel.text(60,250,str("Elle vous recharge votre batterie entierement."),3)
    
    pyxel.text(330,230,str("Les coeurs :"),4)
    pyxel.blt(338,240,2,16,56,16,16,1)
    pyxel.text(380,240,str("Les coeurs seront utilisee des que vous les prennez."),3)
    pyxel.text(380,250,str("Il vous redonne un coeur de votre sante."),3)
    
    pyxel.text(10,280,str("La boisson :"),4)
    pyxel.blt(18,290,2,0,56,16,16,1)
    pyxel.text(60,290,str("La boisson est un objet que vous utilisez quand vous voulez."),3)
    pyxel.text(60,300,str("Il vous regenere et boost temporairement votre endurence."),3)
    
    pyxel.text(330,280,str("Le jambon"),4)
    pyxel.blt(338,290,2,0,40,16,16,1)
    pyxel.text(390,290,str("Le jambon est un objet que vous utilisez quand vous voulez."),3)
    pyxel.text(390,300,str("Vous devez le lancer sur l'arabe pour le faire fuir."),3)
    
    pyxel.text(5,340,"<--   Les Mobs",7)
    pyxel.text(550,340,"But   -->",7)




def PageIIII():
    pyxel.text(275,20,str("But du jeu"),4)
    pyxel.text(100,50,str("Vous vous réveiller dans une pièce plongé dans le noir et n'avez sur vous qu'un couteau et une lampe torche"),3)
    pyxel.text(100,70,str("Pour sortir d'ici et retrouvez la lumière vous devrez explorer les différente salle de cette endroit peux acceuillant "),3)
   
    pyxel.text(25,80,str("Les Leviers"),4)
    pyxel.blt(20,90,0,128,72,32,16,14)
    pyxel.text(65,100,str("Les Leviers sont disperce aleatoirement Ouvre le portail. s'acctive avec E "),3)
    
    pyxel.text(25,150,str("La Porte"),4)
    pyxel.blt(10,160,0,96,120,64,48,3)
    pyxel.text(80,180.,str("Porte situez a la primeiere Salle, se Deverouille en activant 3 Levier, s'ouvre avec E.  "),3)
    

    pyxel.text(25,240,str("Les Grilles "),4)
    pyxel.text(90,270.,str(" Grille qui se fermeront a chaque fois que vous ne serez pas seul dans une salle, videz la salle pour les ouvrirs. "),3)
    pyxel.blt(10,250,0,176,72,80,48,3)
    
    
    pyxel.text(5,340,"<--   Les Mechanique",7)
    pyxel.text(550,340,"Menu Principale   -->",7)


'''INTERFACE A CHANGER '''
def mort():
    global start                                                                                 #test de mort 
    if Player ['PV']<1:
        Player['PV']=0    
        start=2
        pyxel.clip()
        pyxel.cls(0)
        pyxel.text(230,200,'Appui sur espace pour retourner au menu',7)
        pyxel.text(280,150,'Vous êtes mort ! ',7)
        if pyxel.btn(pyxel.KEY_SPACE):
            start=0










'''
                                                                                ░█████╗░██████╗░██████╗░
                                                                                ██╔══██╗██╔══██╗██╔══██╗
                                                                                ███████║██████╔╝██████╔╝
                                                                                ██╔══██║██╔═══╝░██╔═══╝░
                                                                                ██║░░██║██║░░░░░██║░░░░░
                                                                                ╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░

'''
def JoueurComplet():
    global XYmap
    XYmap=MapMob[Player['Ymob']][Player['Xmob']]
    deplacement()
    Course()
    mort()
    PointdeVie()
    Immunite()
    Attaque()

def BotDraw():
    types(Bot1)
    types(Bot2)
    types(Bot3)
    types(Bot4)

def JoueurDraw():
    if Player['Frappe']['Status']!=True :                                                                            
        Draw32px(Player,0,0,1,1)                                              #affiche le joueur et des animations
    else:
        Draw32px(Player,0,128,1,1)                                            #Si le joueur attaque : Animations
        Draw32px(Player['Frappe'],32,0,1,1)
    BatterieAffichage()
    drawSprint()                   #Stamina en haut a gauche (si elle est faible : elle devient rouge)
    PointdeVie()



class App:
    def __init__(self):                                                         #Initialisation du Jeu 
        pyxel.init(XResol,YResol, title="jeu")                                #Initialisation de la résolution du jeu et de son titre
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

        global start,Jour,XYmap
        if pyxel.btnp(pyxel.KEY_TAB):                                           #Stop le jeu et ouvre le Menu quand on appui sur tab
            start=0
        if pyxel.btnp(pyxel.KEY_U):                                           #Stop le jeu et ouvre le Menu Mort quand on appui sur 
            start=2    
        if start==10:
            Introduction()
            
        elif start==0:                                                          #Si la partie n'est pas démarrée
            menuanime()
            menu()

        
        elif start==-1:                                                         #Si on est dans le menu des options
            option()
        
        if start==1:                                                            #Si la partie est démarrée, lancement des fonction ci dessous:
            XYmap=MapMob[Player['Ymob']][Player['Xmob']]
            JoueurComplet()
            Boss_Fight()
            BougeMap()
        
        
        
        
        elif start==2:
            if pyxel.btn(pyxel.KEY_SPACE):
                start=0
        
        GODmode()
        if pyxel.btnp(pyxel.KEY_HOME):
            Jour=Jour+1
        if Jour>=2 or Jour<0:
            Jour=0
        if start==4:
            pyxel.clip()
            JoueurComplet()
            Boss_Fight()


    def draw(self):
        '''
                                                                                ██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
                                                                                ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
                                                                                ██║░░██║██████╔╝███████║░╚██╗████╗██╔╝
                                                                                ██║░░██║██╔══██╗██╔══██║░░████╔═████║░
                                                                                ██████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░
                                                                                ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░
        '''
        global start,Jour

        if start==1:                                                            #Si la partie est démarrée
            if Jour==0:
                pyxel.clip(Player['x']-75,Player['y']-75,150,150)                   
                pyxel.cls(0)                                                        #colorie toute la map en noir
            if Jour==1:
                pyxel.cls(4)
            if Jour==0:
                LampeLum()                                                          #affiche les couleurs de la lampe  
            SPorte()
            pyxel.bltm(Xmap,Ymap,0,0,0,6400,3200,14)                                     #imprime la tilemap
            typesobj(Objet)
            Portail()                                                                                #Si l'ennemis est dans le flash : il est visible
            BotDraw()
            if Jour==0:
                Lampe()
                                                                         #affiche qu'une certaine partie de la map a l'écran
            JoueurDraw()
                
            drawObjets()                                                 #affiche l'objet que le joueur a actuellement
            
            
            
            if not pyxel.btn(pyxel.KEY_F)   :             #si la touche flash et la battetrie est supérierur a 5
                Batterie()                                                          #Batterie restante en haut a gauche de l'écran           
            if Jour==0:
                flash()                                                                   #Ce changement était nessessaire pour que la batterie s'affiche.
            
            
            
            if Bot1['Type']=='Cauchemare':
                pyxel.text(Player['x']+65,Player['y']-75,str(Bot1['PV']//3),7)
        
            DebugMenu()
        if start==0 or start==-1 or Jour==1:
            pyxel.clip()
        if start==4:
           pyxel.cls(0)
           pyxel.text(280,160,'TO BE CONTINUED',7)
           pyxel.text(20,0,'en construction',7)
           '''
           arena(XX,YY)
           pyxel.bltm(XX,YY,1,0,0,6400,3200,15)
           JoueurDraw()
           WarioApparition()
           '''


App()

'''
code de côté au cas ou 
            XX=(str('X : '))+(str(Xsouris))                                     
            YY=(str('Y : '))+(str(Ysouris))                                     
            pyxel.text(Player['x']-75,Player['y']-75,XX,2)                                                #Position Y du curseur en haut a droite de l'écran                                   
            pyxel.text(Player['x']-45,Player['y']-75,YY,2)                                               #Position Y du curseur en haut a droite de l'écran 

    if (pyxel.pget(Player['x']-10,Player['y']+14)!=1 and pyxel.pget(Player['x']-9,Player['y']+14)!=5 and pyxel.pget(Player['x']-8,Player['y']+14)!=5 and pyxel.pget(Player['x']-7,Player['y']+14)!=5 and pyxel.pget(Player['x']-6,Player['y']+14)!=5 and pyxel.pget(Player['x']-5,Player['y']+14)!=5 and pyxel.pget(Player['x']-4,Player['y']+14)!=5 and pyxel.pget(Player['x']-3,Player['y']+14)!=5 and pyxel.pget(Player['x']-2,Player['y']+14)!=5 and pyxel.pget(Player['x']-1,Player['y']+14)!=5 and pyxel.pget(Player['x']+9,Player['y']+14)!=5 and pyxel.pget(Player['x']+8,Player['y']+14)!=5 and pyxel.pget(Player['x']+7,Player['y']+14)!=5 and pyxel.pget(Player['x']+6,Player['y']+14)!=5 and pyxel.pget(Player['x']+5,Player['y']+14)!=5 and pyxel.pget(Player['x'],Player['y']+14)!=5 and pyxel.pget(Player['x']+1,Player['y']+14)!=5 and pyxel.pget(Player['x']+2,Player['y']+14)!=5 and pyxel.pget(Player['x']+3,Player['y']+14)!=5 and pyxel.pget(Player['x']+4,Player['y']+14)!=5):
     if (pyxel.pget(Player['x']-10,Player['y']-16)!=5 , 1 and pyxel.pget(Player['x']-9,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']-8,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']-7,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']-6,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']-5,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']-4,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']-3,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']-2,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']-1,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']+9,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']+8,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']+7,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']+6,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']+5,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x'],Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']+1,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']+2,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']+3,Player['y']-16)!=5 ,1 and pyxel.pget(Player['x']+4,Player['y']-16)!=5 ,1): 

    for i in range (-10,9):
        p=pyxel.pget(Player['x']+i,Player['y']-16,)
        if p==4:
            
            return True
    for i in range (-10,9):
        p=pyxel.pget(Player['x']+i,Player['y']+14)
        if p==4:
            
            return True
             
    for y in range(-16,14):
            p=pyxel.pget(Player['x']-10,Player['y']+y,)
            if p==4:
                
                return True 
    for y in range(-16,14):
            p=pyxel.pget(Player['x']+9,Player['y']+y,)
            if p==4:
                
                return True
    return False  



'''