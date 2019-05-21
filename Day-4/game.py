import pygame, sys, time
pygame.init()

winw = 800
winh = 800
winsurf=pygame.display.set_mode((winw,winh),0,32)
pygame.display.set_caption('Animation')

dl = 1
dr = 3
ul = 7
ur = 9

ms = 4

BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

b1 = {'rect':pygame.Rect(300, 80, 0, 0),'color':RED, 'dir':ur}
b2 = {'rect':pygame.Rect(200, 200, 0, 0),'color':GREEN, 'dir':ul}
b3 = {'rect':pygame.Rect(300, 150, 0, 0),'color':BLUE, 'dir':dl}
blocks = [b1,b2,b3]

while True:
	for event in pygame.event.get():
		if event.type == quit:
			pygame.quit()
			sys.exit()
			
	for b in blocks:
		
		if b['dir']== dl:
			b['rect'].left -= ms
			b['rect'].top += ms
		if b['dir']== dr:
			b['rect'].left += ms
			b['rect'].top += ms
		if b['dir']== ul:
			b['rect'].left -= ms
			b['rect'].top -= ms
		if b['dir']== ur:
			b['rect'].left += ms
			b['rect'].top -= ms
			
		if b['rect'].top < 0:
			if b['dir']== ul:
				b['dir'] = dl
			if b['dir']== ur:
				b['dir'] = dr
		if b['rect'].bottom > winh:
			if b['dir']== dl:
				b['dir']= ul
			if b['dir']== dr:
				b['dir']= ur
		if b['rect'].left < 0:
			if b['dir']== dl:
				b['dir']= dr
			if b['dir']== ul:
				b['dir']= ur
		if b['rect'].right > winw:
			if b['dir']== dr:
				b['dir']= dl
			if b['dir']== ur:
				b['dir']= ul
				
		pygame.draw.rect(winsurf,b['color'],b['rect'])
		
	pygame.display.update()
	time.sleep(0.02)