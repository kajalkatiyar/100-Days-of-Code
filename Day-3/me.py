import time
import pygame
pygame.init()

win=pygame.display.set_mode((600,600),0,32)

BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)
WHITE=(255,255,255)

win.fill(WHITE)
pygame.draw.circle(win,BLUE,(100,100),90,0)
pygame.draw.circle(win,RED,(500,100),90,0)
pygame.draw.ellipse(win,GREEN,(100,50,400,400))

pygame.display.update()

pixArray = pygame.PixelArray(win)
pixArray[480][380] = BLACK
del pixArray

time.sleep(9)
pygame.quit()
