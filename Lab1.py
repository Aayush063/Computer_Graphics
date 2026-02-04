import pygame
import sys
pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DDA line")
WHITE=(255,255,255)
BLACK=(0,0,0)
def DDA(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    steps=max(abs(dx),abs(dy))
    x_inc=dx/steps
    y_inc=dy/steps
    x,y=x1,y1
    for i in range(steps):
        pygame.draw.circle(screen,WHITE,(round(x),round(y)),1)
        x+=x_inc
        y+=y_inc
    print("ednj")    
def main():
    screen.fill(BLACK)
    x1,y1=100,100
    x2,y2=700,500
    DDA(x1,y1,x2,y2)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
if __name__=="__main__":
    main()
