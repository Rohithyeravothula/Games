import pygame
from pygame.locals import*
import sys, types
import time
pygame.init()
white=(255,255,255)
black=((0,0,0))
class screen():
    def __init__(self):
        self.playernames=[]
        self.playercount=[0,0]
        self.position=[0,0,0,0,0,0,0,0,0]    
        self.turn=1
    window=pygame.display.set_mode((600,600))
    pygame.display.set_caption("Tic Tac Toi")
    window.fill(white)
    #pygame.draw.line(window,black,(600,0),(600,600),5)
    pygame.draw.line(window,black,(200,0),(200,600),5)
    pygame.draw.line(window,black,(400,0),(400,600),5)
    pygame.draw.line(window,black,(0,200),(600,200),5)  
    pygame.draw.line(window,black,(0,400),(600,400),5)
    def clearscreen(self):
        self.position=[0,0,0,0,0,0,0,0,0]
        self.turn=1
        self.window.fill(white)
        #pygame.draw.line(self.window,black,(600,0),(600,600),5)
        pygame.draw.line(self.window,black,(200,0),(200,600),5)
        pygame.draw.line(self.window,black,(400,0),(400,600),5)
        pygame.draw.line(self.window,black,(0,200),(600,200),5)  
        pygame.draw.line(self.window,black,(0,400),(600,400),5)
        pygame.display.update()
    def completeclear(self):
        self.window.fill(white)
        pygame.display.update()
        
    pygame.display.update() 
       
def drawcircle(pos,window):
    try:
        pygame.draw.circle(window,black,pos,80)
        pygame.display.update()
    except:
        print "Not possible"
def drawmark(pos,window):
    l1start=(pos[0]-40,pos[1]-40)
    l1end=(pos[0]+40,pos[1]+40)
    l2start=(pos[0]+40,pos[1]-40)
    l2end=(pos[0]-40,pos[1]+40)
    try:
        pygame.draw.line(window,black,l1start,l1end,30)
        pygame.draw.line(window,black,l2start,l2end,30)
        pygame.display.update()
    except:
        print "Not possible"
def chpoint(pos):
    quad=-1
    if (pos[0]>0 and pos[0]<200) and ((pos[1]>0 and pos[1]<200)):
        quad=1
    elif (pos[0]>200 and pos[0]<400) and (pos[1]>0 and pos[1]<200):
        quad=2
    elif (pos[0]>400 and pos[0]<600) and ((pos[1]>0 and pos[1]<200)):
        quad=3
    elif (pos[0]>0 and pos[0]<200) and ((pos[1]>200 and pos[1]<400)):
        quad=4
    elif (pos[0]>200 and pos[0]<400) and ((pos[1]>200 and pos[1]<400)):
        quad=5
    elif (pos[0]>400 and pos[0]<600) and ((pos[1]>200 and pos[1]<400)):
        quad=6
    elif (pos[0]>0 and pos[0]<200) and ((pos[1]>400 and pos[1]<600)):
        quad=7
    elif (pos[0]>200 and pos[0]<400) and ((pos[1]>400 and pos[1]<600)):
        quad=8
    elif (pos[0]>400 and pos[0]<600) and ((pos[1]>400 and pos[1]<600)):
        quad=9
    return quad
def centre(a):
    if a==0:
        return (100,100)
    elif a==1:
        return (300,100)
    elif a==2:
        return (500,100)
    elif a==3:
        return (100,300)
    elif a==4:
        return (300,300)
    elif a==5:
        return (500,300)
    elif a==6:
        return (100,500)
    elif a==7:
        return (300,500)
    elif a==8:
        return (500,500)
    
def response(window,pos):
    a=chpoint(pos)-1
    if window.position[a]==0:
        window.turn=window.turn+1
        if window.turn%2==0:
            drawcircle(centre(a),window.window)
            window.position[a]=1
        else:
            drawmark(centre(a),window.window)
            window.position[a]=-1    
def chposition(a):
    if   a[0]==a[1] and a[0]==a[2] and a[0]!=0:
        return a[0]
    elif a[3]==a[4] and a[3]==a[5] and a[3]!=0:
        return a[3]
    elif a[6]==a[7] and a[6]==a[8] and a[6]!=0:
        return a[6]
    elif a[0]==a[3] and a[0]==a[6] and a[0]!=0:
        return a[0]
    elif a[1]==a[4] and a[1]==a[7] and a[1]!=0:
        return a[1]
    elif a[2]==a[5] and a[2]==a[8] and a[2]!=0:
        return a[2]
    elif a[0]==a[4] and a[0]==a[8] and a[0]!=0:
        return a[0]
    elif a[2]==a[4] and a[2]==a[6] and a[2]!=0:
        return a[2]
    u=1
    for i in range(0,9):
        if a[i]==0:
            u=0
    if u==1:
        return -2
    else:
        return 0

def gameend(window,a,v):
    if v==1:
        window.playercount[0]=window.playercount[0]+1
    else:
        window.playercount[1]=window.playercount[1]+1
    
    window.completeclear()
    font = pygame.font.Font(None, 60)
    text = font.render("Game Over", 1, (250, 10, 10))
    window.window.blit(text, (200,250))
    font = pygame.font.Font(None, 30)
    S="Player1: "+str(window.playercount[0])+" "+"Player2: "+str(window.playercount[1])+" "
    text = font.render(S, 1, (250, 10, 10))
    window.window.blit(text, (200,350))
    pygame.display.update()
    time.sleep(1)
    pygame.event.clear()
    main()
def drawgame(window):
    window.completeclear()
    font = pygame.font.Font(None, 60)
    text = font.render("Draw Game", 1, (250, 10, 10))
    window.window.blit(text, (200,250))
    font = pygame.font.Font(None, 30)
    S="Player1: "+str(window.playercount[0])+" "+"Player2: "+str(window.playercount[1])+" "
    text = font.render(S, 1, (250, 10, 10))
    window.window.blit(text, (200,350))
    pygame.display.update()
    time.sleep(1)
    pygame.event.clear()
    main()
    
def main():
    window.clearscreen()
    player1count=0
    player2count=0
    a=[player1count,player2count]
    while True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                response(window,pos)
                v=chposition(window.position)
                if v==1 or v==-1:
                    time.sleep(1)
                    pygame.event.clear()
                    gameend(window,a,v)
                if v==-2:
                    time.sleep(1)
                    pygame.event.clear()
                    drawgame(window)
                #print window.position
            elif event.type==QUIT:
                pygame.quit()
                sys.exit()

window=screen()      
main()
        
    
