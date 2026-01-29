# def ellipse(xc,yc,rx,ry):
#     x=0
#     y=ry
#     p1= (ry*ry)-(rx*rx*ry)+(0.25*rx*rx)
#     while((2*ry*ry*x)<=(2*rx*rx*y)):
#         if (p1<0):
#             x=x+1
#             y=y
#             p1=p1+(2*ry*ry*x)+(ry*ry)
#         else:
#             x=x+1
#             y=y-1
#             p1=p1+(2*ry*ry*x)-(2*rx*rx*y)+(ry*ry)
#         print (x,y)
#     p2=(ry*ry*((x+0.5)**2))+(rx*rx*((y-1)**2))-(rx*rx*ry*ry)
#     while (y!=0):
#         if (p2>0):
#             y=y-1
#             x=x
#             p2=p2-(x*rx*rx*y)+(rx*rx)
#         else:
#             x=x+1
#             y=y-1
#             p2=p2-(2*rx*rx*y)+(2*ry*ry*x)+(ry*ry)
#         print(x,y)
# ellipse(150,100,5,5)
import pygame
import sys
pygame.init()
w,h=800,800
screen=pygame.display.set_mode((w,h))
WHITE = (255,255,255)
BLACK=(0,0,0)
def ellipse(xc,yc,rx,ry):
    x=0
    y=ry
    p1=(ry*ry)-(rx*rx*ry)+(0.25*rx*rx)
    while (2*ry*ry*x <= 2*rx*rx*y):
        if (p1<0):
            x=x+1
            y=y
            p1=p1+(2*ry*ry*x)+(ry*ry)     
        else:
            x=x+1
            y=y-1
            p1=p1+(2*ry*ry*x)-(2*rx*rx*y)+(ry*ry)
        screen.set_at((xc+x,yc+y),WHITE)
        screen.set_at((xc+x,yc-y),WHITE)
        screen.set_at((xc-x,yc+y),WHITE)
        screen.set_at((xc-x,yc-y),WHITE)

    p2=(ry*ry*((x+0.5)**2))+(rx*rx*((y-1)**2))-(rx*rx*ry*ry)
    while(y!=0):
        if(p2>0):
            y=y-1
            x=x
            p2=p2-(2*rx*rx*y)+(rx*rx)
        else:
            y=y-1
            x=x+1
            p2=p2-(2*rx*rx*y)+(2*ry*ry*x)+(rx*rx)
        screen.set_at((xc+x,yc+y),WHITE)
        screen.set_at((xc+x,yc-y),WHITE)
        screen.set_at((xc-x,yc+y),WHITE)
        screen.set_at((xc-x,yc-y),WHITE)            
def main():
    screen.fill(BLACK)
    ellipse(250,250,150,175)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
if __name__=="__main__":
    main()                

        
