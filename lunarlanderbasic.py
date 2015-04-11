import pygame
import sys
import random

######################
# lunarlanderbasic.py
# By 2BoysAndHats
# Please Make your own!!!
#
#
#######################

#Start defining sprites

#Lander class (extends Sprite class)
class Lander(pygame.sprite.Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('module.gif')
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed = [0,3]
    def move(self):
        self.rect = self.rect.move(self.speed)

#Lander class (extends Sprite class)
class Moon(pygame.sprite.Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('moon.gif')
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location

#Start initing stuff

done = False

pygame.init() #Initlises pygame

screen = pygame.display.set_mode([640,480]) #Sets up the screen (width 640, height 480)

font = pygame.font.SysFont("comicsansms", 30) #Makes a 'Base font' to use later
 
pygame.display.set_caption('Lunar Lander') #Set window name

pygame.key.set_repeat(50,50) #Set key repeat (delay,interval)

lander = Lander([random.randint(0,640-25),0]) #Makes a new lander object at random x, y 0

lander_group = pygame.sprite.Group() # A group in pygame is a way of orginizing things, it is also used in colision detection

lander_group.add(lander) # Adds the lander to lander_group

moon = Moon([0,330]) # Makes a new moon at [x 0, y 330]

background = pygame.image.load('background.gif') # Loads the background image into a varible

screen.blit(background,[0,0]) # In pygame, blit means copy so copy the background surface to [x 0 ,y 0]

screen.blit(lander.image,lander.rect) # Copy the lander image to coords defined in its rect

screen.blit(moon.image,moon.rect) # Blit the moon (but it doesn't show yet (look on next line))

pygame.display.flip() # In pygame we draw (blit) onto the screen the we 'flip' to the screen we drawed on, so it all appears at once

#Main game loop

while True:
    try: # This is to handle Control-C
        screen.fill([255,255,255]) #Fill the screen, (to wipe out everything else)
        for event in pygame.event.get(): #Get all event
            if event.type == pygame.QUIT: #If x clicked...
                sys.exit() #...Then quit the program
            elif event.type == pygame.KEYDOWN: #Check if key is pressed
                if event.key == pygame.K_UP: #Check the key pressed
                    if lander.speed[1] > -2:
                        lander.speed[1] -= 0.25 # Modifiys the speed array
                elif event.key == pygame.K_DOWN:
                    if lander.speed[1] < 2:
                        lander.speed[1] += 0.25
                elif event.key == pygame.K_LEFT:
                    if lander.speed[0] > -2:
                        lander.speed[0] -= 0.25
                elif event.key == pygame.K_RIGHT:
                    if lander.speed[0] < 2:
                        lander.speed[0] += 0.25
                        
        if pygame.sprite.spritecollide(moon,lander_group,True): #Checks for collisions between moon sprite
            done = True # Set done to true...
            
        if not done: #... So lander doesn't move
            lander.move()

        screen.blit(background,[0,0]) #Blit the screen every time through the loop
        screen.blit(lander.image,lander.rect) # And the lander
        screen.blit(moon.image,moon.rect) # And the moon

        if done:#Check if done...
            label = font.render("Game over,Thanks for playing!!!", 1, (255,255,255)) # Make a surface out of the base font
            screen.blit(label,[320,240]) # Blit the label

        pygame.display.flip() #Flip to the new screen
        pygame.time.delay(30) # Delay so that lander doesn't move 100km/h

    except KeyboardInterrupt : #Catch Control-C 
        sys.exit() #And quit.
