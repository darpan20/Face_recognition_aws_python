import pygame, sys
from pygame.locals import *
from ctypes import *
import os
import win32gui,win32con
BLACK =    (0,  0,  0)
WHITE =    (255,255,255)#white color in RGB format
windll.user32.SetProcessDPIAware()
true_res = (windll.user32.GetSystemMetrics(0),windll.user32.GetSystemMetrics(1))
SCREENWIDTH=true_res[0]
SCREENHEIGHT=true_res[1]
print(SCREENWIDTH)
print(SCREENHEIGHT)
pygame.mixer.init()
def main():
    from winsound import PlaySound,SND_ASYNC
    from Login_surv import initiate_surv
    from Login_att import initiate_att
    pygame.init()
    pygame.font.init()
    play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"frc.wav"),SND_ASYNC)
    play()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),FULLSCREEN) 
    myfont=pygame.font.SysFont('Comic Sans MS',30)
    textsurface=myfont.render('"esc" to exit',True,WHITE)
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    button_s=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"button_s.png")).convert_alpha()
    button_s=pygame.transform.scale(button_s, (236,56))
    button_a=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"button_a.png")).convert_alpha()
    button_a=pygame.transform.scale(button_a, (238,56))
    mouseClicked = False
    mousex = 0
    mousey = 0
    pygame.display.set_caption('FACE_RECOGNITION') 
    image=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"w1.png")).convert_alpha()
    image=pygame.transform.scale(image, (SCREENWIDTH,SCREENHEIGHT))
    s_icon=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"s_icon.png")).convert_alpha()
    s_icon=pygame.transform.scale(s_icon, (256,256))
    a_icon=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"a_icon2.png")).convert_alpha()
    a_icon=pygame.transform.scale(a_icon, (232,232))
    e1=pygame.image.load(os.path.join(os.path.dirname(os.path.realpath('__file__')),"f.png")).convert_alpha()
    e1=pygame.transform.scale(e1, (1110,78))
    DISPLAYSURF.fill(WHITE)#for white backgorund
    DISPLAYSURF.blit(image,(0,0))
    DISPLAYSURF.blit(s_icon,(SCREENWIDTH/1.5,SCREENHEIGHT/4.3))
    DISPLAYSURF.blit(a_icon,(SCREENWIDTH/5,SCREENHEIGHT/4))
    DISPLAYSURF.blit(button_s,(SCREENWIDTH/1.48,SCREENHEIGHT/1.51))
    DISPLAYSURF.blit(button_a,(SCREENWIDTH/5,SCREENHEIGHT/1.5))
    DISPLAYSURF.blit(e1,(SCREENWIDTH/4.7,SCREENHEIGHT/20))
    DISPLAYSURF.blit(textsurface,(0,0))
    while True: #main game loop
        for event in pygame.event.get():
            
            if event.type is KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        if mouseClicked == True:
         if Rect(SCREENWIDTH/5,SCREENHEIGHT/1.97,SCREENWIDTH/5+238,SCREENHEIGHT/1.97+56).collidepoint(mousex,mousey):
          
          PlaySound(None,SND_ASYNC)
          play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"b3.wav"),SND_ASYNC)
          play()
          pygame.quit()
          initiate_att()
          
          sys.exit()
         elif Rect(SCREENWIDTH/1.48,SCREENHEIGHT/2,SCREENWIDTH/1.48+236,SCREENHEIGHT/2+56).collidepoint(mousex,mousey):
           
          PlaySound(None,SND_ASYNC)
          play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"b3.wav"),SND_ASYNC)
          play()
          pygame.quit()
          initiate_surv()
            
          sys.exit()
        pygame.display.update()
if __name__=='__main__':
    main()           
        