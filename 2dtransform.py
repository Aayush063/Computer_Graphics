import pygame
import sys
pygame.init()
w,h=1000,1000
screen=pygame.display.set_mode((w,h))
WHITE = (255,255,255)
BLACK=(0,0,0)
# tx=100
# ty=150
# sx=5
# sy=8
def translate (x1,y1,x2,y2):
    # pygame.draw.line(screen,"RED",(x1,y1),(x2,y2),2)
    i=0
    while (i<300):
        x11=x1+i
        x22=x2+i
        y11=y1
        y22=y2
        i+=1
        clock.tick(10)
        pygame.display.flip()

        pygame.draw.line(screen,"GREEN",(x11,y11),(x22,y22),4)

# def scaling (x1,y1,x2,y2):
#     pygame.draw.line(screen,"RED",(x1,y1),(x2,y2),2)
#     x11=x1*sx
#     x22=x2*sx
#     y11=y1*sy
#     y22=y1*sy
#     pygame.draw.line(screen,"GREEN",(x11,y11),(x22,y22),2)

# def rotation (x1,y1,x2,y2):
#     pygame.draw.line(screen,"RED",(x1,y1),(x2,y2),2)
#     x11=x1*math.cos(math.radians(45))-y1*math.sin(math.radians(45))
#     x22=x2*math.cos(math.radians(45))-y2*math.sin(math.radians(45))
#     y11=x1*math.sin(math.radians(45))+y1*math.sin(math.radians(45))
#     y22=x2*math.sin(math.radians(45))+y2*math.sin(math.radians(45))
#     pygame.draw.line(screen,"GREEN",(x11,y11),(x22,y22),2)



 

clock=pygame.time.Clock()

# while True:

#     screen.fill(BLACK)
#     # scaling(25,60,90,80)
#     # rotation(25,50,150,140)
#     translate(100,100,400,400)
#     pygame.display.flip()
   
while True:
     for event in pygame.event.get():
         if(event.type==pygame.QUIT):
            pygame.quit()
            sys.exit()
     screen.fill(WHITE)
     pygame.draw.line(screen,BLACK,(100,100),(600,600),2)
     translate(100,100,600,600)
     pygame.display.flip()

