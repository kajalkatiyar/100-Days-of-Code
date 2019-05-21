import pygame
import time

pygame.init()
screen = pygame.display.set_mode((300, 300))
done = False

def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)

happy = pygame.image.load('happy.png') # our happy blue protagonist 
checkers = pygame.image.load('background.png') # 32x32 repeating checkered image 

while not done:
        start = time.time()
        # pump those events! 
        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                        done = True
        # checker the background 
        x = 0
        while x < 300:
                y = 0
                while y < 300:
                        screen.blit(checkers, (x, y))
                        y += 32
                x += 32
        
        # here comes the protagonist 
        #screen.blit(happy, (100, 100))
		
        blit_alpha(screen, happy, (100, 100), 128)
        pygame.display.flip()
		
        # yeah, I know there's a pygame clock method 
        # I just like the standard threading sleep 
        end = time.time()
        diff = end - start
        framerate = 30
        delay = 1.0 / framerate - diff
        if delay > 0:
                time.sleep(delay)