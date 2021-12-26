import pygame
import time
from pygame import mouse
import random
from pygame.constants import MOUSEBUTTONDOWN

pygame.init()
pygame.font.init()

black=0, 0, 0
white= 255, 255, 255


(width,height)=(400,400)
l=[0,0,0,0,0,0,0,0,0]

#Screen
screen=pygame.display.set_mode((width,height))

#Caption
pygame.display.set_caption("Tic Tac Toe")

#Icons
icon=pygame.image.load("D:\VSC Codes\PRG\TicTacToeUI\icon.png")
pygame.display.set_icon(icon)

#Background
background=pygame.image.load("D:\VSC Codes\PRG\TicTacToeUI\plane.jpg").convert()
background=pygame.transform.scale(background,(width,400))

#Rect
x=pygame.image.load("D:\VSC Codes\PRG\TicTacToeUI\X.png")
x=pygame.transform.scale(x,(105,105))
o=pygame.image.load("D:\VSC Codes\PRG\TicTacToeUI\O.png")
o=pygame.transform.scale(o,(105,105))

#X and O random
choice={1 : "X", 0 : "O"}
def rand():
    return random.choice(choice)
def print_x(x_axis,y_axis):
    screen.blit(x,(x_axis,y_axis))
def print_o(x_axis,y_axis):
    screen.blit(o,(x_axis,y_axis))

#Win condition
def Win(turn):
    if l[4]==l[0] and l[8]==l[0] and l[0]!=0:
        return turn
    if l[2]==l[4] and l[6]==l[2] and l[2]!=0:
        return turn
    for i in range(0,9,3):
        if l[i]==l[i+1] and l[i]==l[i+2] and l[i]!=0:
            return turn
    for i in range(0,3):
        if l[i]==l[i+3] and l[i]==l[i+6] and l[i]!=0:
            return turn
    return False

# Winner 
'''
font=pygame.font.SysFont('freesansbold.ttf',26)
winner=font.render("Winner is ", True, black)
winRect = winner.get_rect()
winRect.center=(width // 2,height // 2)
'''

#Main loop
running= True
turn=rand()
print(str(turn + " goes first"))
nr=0
w=0
while running:
    ev=pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position=pygame.mouse.get_pos()
            ok=1
            if mouse_position[1]<133: 
                if mouse_position[0]<133:
                    if l[0]==0:
                        l[0]=turn
                        ok=0
                elif mouse_position[0]<266:
                    if l[1]==0:
                        l[1]=turn
                        ok=0
                elif mouse_position[0]<400:
                    if l[2]==0:
                        l[2]=turn
                        ok=0
            elif mouse_position[1]<266 : 
                if mouse_position[0]<133:
                    if l[3]==0:
                        l[3]=turn
                        ok=0
                elif mouse_position[0]<266:
                    if l[4]==0:
                        l[4]=turn
                        ok=0
                elif mouse_position[0]<400:
                    if l[5]==0:
                        l[5]=turn
                        ok=0
            elif mouse_position[1]<400 : 
                if mouse_position[0]<133:
                    if l[6]==0:
                        l[6]=turn
                        ok=0
                elif mouse_position[0]<266:
                    if l[7]==0:
                        l[7]=turn
                        ok=0
                elif mouse_position[0]<400:
                    if l[8]==0:
                        l[8]=turn
                        ok=0
            if ok==0:
                if Win(turn):
                    w=1
                    print(turn + " WON")
                    running=False
                    break
                if turn=='X':
                    turn='O'
                else:
                    turn='X'
                nr+=1
            if nr==9: 
                running=False
                print("Draw")
    screen.blit(background,(0,0))
    for i in range(0,9):
        if l[i]:
            if l[i]=='X':
                print_x(15+int(i%3)*133,15+int(i/3)*133)
            elif l[i]=='O':
                print_o(15+int(i%3)*133,15+int(i/3)*133)
    pygame.display.update()


if Win(turn):   
    height=100
    width=100

    font=pygame.font.SysFont('freesansbold.ttf',26)

    winner=font.render("Winner is " + str(turn) , True,black,white)
    winRect = winner.get_rect()
    winRect.center=(width // 2,height // 2)
