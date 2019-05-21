import pygame
pygame.init()

winsurf = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('gROWTH')

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,128,0)
BLUE=(0,0,255)
LIME=(0,255,0)

texttype=pygame.font.SysFont(None,48)

text=texttype.render('gROWTH',True,WHITE,BLUE)
box=text.get_rect()
box.centerx=winsurf.get_rect().centerx
box.centery=winsurf.get_rect().centery

winsurf.fill(WHITE)
pygame.draw.polygon(winsurf,GREEN,((146,0),(291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(winsurf, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(winsurf, BLUE, (120, 60), (60, 120))
pygame.draw.line(winsurf, BLUE, (60, 120), (120, 120), 4)

pygame.draw.circle(winsurf, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(winsurf, RED, (300, 250, 40, 80), 1)

#pygame.draw.rect(winsurf, RED, (box.left - 20, box - 20, box.width + 40, box.height + 40))
pygame.draw.rect(winsurf,RED,(50,200,60,20))

pixArray = pygame.PixelArray(winsurf)
pixArray[480][380] = BLACK
del pixArray

winsurf.blit(text,box)
pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type==quit:
			pygame.quit()
			sys.exit()