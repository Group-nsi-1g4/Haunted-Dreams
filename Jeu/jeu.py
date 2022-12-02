#Mathieu brodard, Mathieu vilmot, Mohamed Latreche, Sailan Sivakumar
import pyxel



global Player1
global Player2
global x1
global y1
global x2
global y2
global x3
global y3
x1,y1=0,57
x2,y2=50,57
x3=60
y3=57
Player1 = {'position':[x1,y1] , 'Vitesse': 2,}
bot2 = {'position':[x2,y2] , 'Vitesse': 0.09}
bot1= {'position':[x3,y3] , 'Vitesse': 0.05}

test

def deplacement1():
    global x1,y1
    colorD=pyxel.pget(x1+8,y1+15)
    colorU=pyxel.pget(x1+8,y1)
    colorR=pyxel.pget(x1+13,y1+7)
    colorL=pyxel.pget(x1+2,y1+7)
    if pyxel.btn(pyxel.KEY_P):
        Player1['Vitesse']=Player1['Vitesse']+1
    if pyxel.btn(pyxel.KEY_M):
        Player1['Vitesse']=Player1['Vitesse']-1
    if colorD !=14:
        if pyxel.btn(pyxel.KEY_DOWN):
            y1=y1+Player1['Vitesse']
    if colorR !=14:   
        if pyxel.btn(pyxel.KEY_RIGHT):
            x1=x1+Player1['Vitesse']
    if colorL !=14 :
        if pyxel.btn(pyxel.KEY_LEFT):
            x1=x1-Player1['Vitesse']
    if colorU !=14 :
        if pyxel.btn(pyxel.KEY_UP):
            y1=y1-Player1['Vitesse']
def ai2():
    global x2,y2
    x2=x2+((x1-x2)*bot2['Vitesse'])
    y2=y2+((y1-y2)*bot2['Vitesse'])

def ai1():
    global x3,y3
    x3=x3+((x1-x3)*bot1['Vitesse'])
    y3=y3+((y1-y3)*bot1['Vitesse'])

def flash():
    global x1,y1
    pyxel.circb(x1+8,y1+8,20,1)
    pyxel.circb(x1+8,y1+8,19,1)
    pyxel.circb(x1+8,y1+8,21,5)
class App:
    def __init__(self):
        pyxel.init(160, 80, title="Projet jeu Pyxel")
        pyxel.load("media.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        deplacement1() 
        ai2()
        ai1()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0,0,0,0,0,320,320,0)
        pyxel.blt(x1,y1,1,0,0,16,16,0)
        pyxel.blt(x2,y2,1,16,0,16,16,0)
        pyxel.blt(x3,y3,1,32,0,16,16,0)
        flash()

App()