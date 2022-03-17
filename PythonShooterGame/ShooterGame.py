from pygame import * # Imports pygame.
import sys # Imports sys.
import random # Imports the random module.
import os  # Imports os.
init() # Initializes pygame engine.
os.environ['SDL_VIDEO_CENTERED'] = '1' # Centers the window screen. This is done through the SDL_VIDEO variable.

width = 1000 # Sets the screen width to be 1000.
height = 650 # Sets the heigth of the screen to be 650.
size = width, height # Assigns the width and height to be the size of the screen.
screen = display.set_mode(size) # Creates the screen according to the size.

# Colors defined below
BLACK = (0, 0, 0) 
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (105, 105, 105)

font1 = font.SysFont("Chiller",70) # Creates the font Chiller in size 70.
font2 = font.SysFont("Ravie",70) # # Creates the font Ravie also in size 70.
# The following lines of code assign a number to the gamestates.
MENUSTATE = 0 # MENUSTATE will be 0.
GAMESTATE = 1 # GAMESTATE will be 1.
QUITSTATE = 2 # QUITSTATE will be 2.
INSTRUCTIONSTATE = 3 # INSTRUCTIONSTATE will be 3.

# Game states
KEY_RIGHT = False # Sets the right key to be false.
KEY_LEFT = False # Sets the left key to be false.
KEY_UP = False # Sets the up key to be false.
KEY_DOWN = False # Sets the down key to be false.

moveBullet = False
bulletPic = False

x = 0 # The x location of the player. Initialized to be 0.
y = 0 # The y location of the player. Initialized to be 0.
arrowMoveX = 10 # The x location of the bullet. Initialized to be 0.
arrowMoveY = 10 # The y location of the bullet. Initialized to be 0.
count = 0 # count starts at 0.
enemy = [] # Creates an empty list to store the coordinates of each of the enemies.
count2 = 0 # count2 is 0.
enemySize = 75 # This will be the size of the enemy (75 by 75).
enemySpeed = 3 # This is the speed at which the enemies will move. Starts at 3 for now.
# The following variables are for collision detection.
collideEnemyX = False # Initializes collideEnemyX to be False.
collideEnemyY = False # Initializes collideEnemyY to be False.
collisionGame = False # Initializes collisionGame to be False.
myClock = time.Clock() 
running = True # Initializes running to be true. running represents the main game loop. 

enemyVirus = image.load('worm.png') # Loads the picture of the enemy into the variable enemyVirus.
enemyVirus = transform.scale(enemyVirus, (75, 75)) # Changes the size of the picture to 75 pixels by 75 pixels.
rectVirus = enemyVirus.get_rect() # Gets the rect of enemyVirus.

robot1 = image.load('robot3.png') # Loads the spritesheet that contains all of the different positions of the robot character.
robot1 = transform.scale(robot1, (432, 432)) # Enlarges the size to be 432 by 432.
rectRobot = robot1.get_rect() # Gets the rect for robot1.

SPRITERECTX=0 # This is where the first sprite is found on the sheet. This is to crop the sprite sheet later on. The value assigned is 0.
SPRITERECTY=0 # This is to crop the sprite sheet later on. The value assigned is 0.
LENSPRITEX=108 # This is the length of 1 picture in the sprite sheet. LENSPRITEX is 108.
LENSPRITEY=108 # This is the height of 1 sprite in the sprite sheet. LENSPRITEY is 108. Thus, the size of 1 sprite will be 108 by 108.

spriteSheet = robot1 # spriteSheet is robot1.

#downCharacter = [(SPRITERECTX,SPRITERECTY,LENSPRITEX,LENSPRITEY),(LENSPRITEX,SPRITERECTY,LENSPRITEX,LENSPRITEY),(LENSPRITEX*3,SPRITERECTY,LENSPRITEX,LENSPRITEY)]
#upCharacter =  [(SPRITERECTX,LENSPRITEY*3,LENSPRITEX,LENSPRITEY),(LENSPRITEX,LENSPRITEY*3,LENSPRITEX,LENSPRITEY),(LENSPRITEX*3,LENSPRITEY*3,LENSPRITEX,LENSPRITEY)]
#leftCharacter =  [(SPRITERECTX,LENSPRITEY,LENSPRITEX,LENSPRITEY),(LENSPRITEX,LENSPRITEY,LENSPRITEX,LENSPRITEY),(LENSPRITEX*3,LENSPRITEY,LENSPRITEX,LENSPRITEY)]
#rightCharacter =  [(SPRITERECTX,LENSPRITEY*2,LENSPRITEX,LENSPRITEY),(LENSPRITEX,LENSPRITEY*2,LENSPRITEX,LENSPRITEY),(LENSPRITEY*3,LENSPRITEY*2,LENSPRITEX,LENSPRITEY)]

# CLIPS DOWN AND UP MOVEMENT
# The following lines of code clip the down movement from the sprite sheet. The same sprites will be used for the up movement as well.
spriteSheet.set_clip(Rect(SPRITERECTX, SPRITERECTY, LENSPRITEX, LENSPRITEY)) # Locates the sprite.
drawMe = spriteSheet.subsurface(spriteSheet.get_clip()) # Extracts the sprite you want
spriteSheet.set_clip(Rect(LENSPRITEX, SPRITERECTY, LENSPRITEX, LENSPRITEY)) # Locates the sprite.
drawMe2 = spriteSheet.subsurface(spriteSheet.get_clip()) # Extracts the sprite.
spriteSheet.set_clip(Rect(LENSPRITEX*3, SPRITERECTY, LENSPRITEX, LENSPRITEY)) # Locates the sprite.
drawMe3 = spriteSheet.subsurface(spriteSheet.get_clip()) # Extracts the sprite.
drawing = drawMe

# CLIPS RIGHT MOVEMENT
# The following lines of code clip the right movement from the sprite sheet.
spriteSheet.set_clip(Rect(SPRITERECTX, LENSPRITEY*2, LENSPRITEX, LENSPRITEY)) # Locates the sprite.
drawMe7 = spriteSheet.subsurface(spriteSheet.get_clip()) # Extracts the sprite.
spriteSheet.set_clip(Rect(LENSPRITEX, LENSPRITEY*2, LENSPRITEX, LENSPRITEY)) # Locates the sprite.
drawMe8 = spriteSheet.subsurface(spriteSheet.get_clip()) # Extracts the sprite.
spriteSheet.set_clip(Rect(LENSPRITEX*3, LENSPRITEY*2, LENSPRITEX, LENSPRITEY)) # Locates the sprite.
drawMe9 = spriteSheet.subsurface(spriteSheet.get_clip()) # Extracts the sprite.
drawing3 = drawMe7 

# CLIPS LEFT MOVEMENT
# The following lines of code clip the left movement from the sprite sheet.
spriteSheet.set_clip(Rect(SPRITERECTX, LENSPRITEY, LENSPRITEX, LENSPRITEY)) # Locates the sprite.
drawMe4 = spriteSheet.subsurface(spriteSheet.get_clip()) # Extracts the sprite.
spriteSheet.set_clip(Rect(LENSPRITEX, LENSPRITEY, LENSPRITEX, LENSPRITEY)) # Locates the sprite.
drawMe5 = spriteSheet.subsurface(spriteSheet.get_clip()) # Extracts the sprite.
spriteSheet.set_clip(Rect(LENSPRITEX*3, LENSPRITEY, LENSPRITEX, LENSPRITEY)) # Locates the sprite.
drawMe6 = spriteSheet.subsurface(spriteSheet.get_clip()) # Extracts the sprite.
drawing2 = drawMe4

bullet = image.load('bulletfire.png') # Loads the first image of the bullet. This image will be used when the user fires left or right.
bullet = transform.scale(bullet, (40, 20)) # Transforms the size of the bullet to be 40 by 20 pixels.
rectA = bullet.get_rect() # Gets the rect of the bullet.

bullet2 = image.load('bulletfire2.png') # Loads the second image of the bullet. This image will be used when the user fires down.
bullet2 = transform.scale(bullet2, (20, 45)) # Transforms the size of the bullet to be 20 by 40 pixels.
rectB = bullet2.get_rect() # Gets the rect of the bullet.

bulletPic = bullet # bulletPic is bullet for now.

floor = image.load('floor5.png') # Loads the game background, which is the brick floor.
floor = transform.scale(floor, (1000, 693)) # Scales the iamge to the size of 1000 by 693.
rect = floor.get_rect() # Gets the rect of the floor.

for x in range(5): # Gets the location of 5 enemies. The for loop will occur 5 times, thus creating 5 enemies.
    newEnemy = (random.randrange(width),random.randrange(550,650)) # Randomly generates the x and y values of the enemy. 
    enemy.append(newEnemy) # Adds newEnemy into the list called enemy.
    
def enemyState(): # Creates a function to blit the enemies onto the screen.
    for i in enemy: # Goes throught the list enemy and gets each element.
        screen.blit(enemyVirus, (i[0],i[1],enemySize,enemySize)) # Displays the picture onto the screen by getting the x coordinate of the element and the y coordinate of the element.

def collisionE(playerRect,enemy): # This function checks for collision detection. 
    for e in enemy: # Goes throught the list enemy.
        eRect = Rect(e[0],e[1],enemySize,enemySize) # Creates a rect for each of the enemies. 
        if playerRect.colliderect(eRect): # Checks if playerRect (the character) collides with eRect (the enemies).
            return True # If they do collide, returns true.
    return False # If they dont collide, returns false.

def updateE(i):
    xE,yE = i
    if x > xE:
        xE += enemySpeed
    else:
        xE -= enemySpeed
    if y > yE:
        yE += enemySpeed
    else:
        yE -= enemySpeed
    return xE,yE

enemy = [updateE(i) for i in enemy]
        
def drawScreen(locationx,locationy):
    global drawing, enemy, moveBullet, arrowMoveX, arrowMoveY, bulletPic
    #draw.rect(screen, BLACK, (0, 0, width, height))
    screen.blit(floor,rect)
    enemy = [updateE(i) for i in enemy]
    enemyState()
    screen.blit(drawing, (locationx,locationy,locationx,locationy))
    if moveBullet == True:
        screen.blit(bulletPic, (arrowMoveX+43,arrowMoveY+35,40,30))
    playerRect = Rect(locationx,locationy,LENSPRITEX,LENSPRITEY)
    if collisionE(playerRect,enemy) == True: # Checks the collision.
        collisionGame = True # If the enemy collides with the player, than collisionGame is true. The loop will than break.
        return collisionGame
    display.flip()
    
def drawMenu(button, mouseX, mouseY):
    global screen, width, height
    #draw.rect(screen, BLACK, (0, 0, width, height))
    #music()
    menuBack = image.load('fantasy_border5.jpg')
    menuBack = transform.scale(menuBack, (1000, 650))
    rect = menuBack.get_rect()
    rect = rect.move((0, 0))   
    screen.blit(menuBack, rect)

    st = MENUSTATE
    

    # for displaying the play game box
    playRect = Rect(width//4, height//4, width//2, height//8)
    if width//2 > mouseX > width//4 and height//8 > mouseY > height//4:
        draw.rect(screen, RED, playRect)
    else: 
        draw.rect(screen, GREY, playRect)
    #draw.rect(screen, boxColor, playRect)
    # Creating font...we’ll get to that later
    string = "Play Game"
    playText = font1.render(string, 1, RED)
    playSize = font1.size(string)
    playTitleRect = Rect(width//4 + (width//2 - playSize[0])//2, height//4 + (height//8 - playSize[1])//2, playSize[0], playSize[1])
    screen.blit(playText, playTitleRect)
    
    # for displaying the play game box
    instructionRect = Rect(width//4, height//2.2, width//2, height//8)
    draw.rect(screen, GREY, instructionRect)
    # Creating font...we’ll get to that later
    string = "Instructions"
    instructionText = font1.render(string, 1, RED)
    instructionSize = font1.size(string)
    instructionTitleRect = Rect(width//4 + (width//2 - instructionSize[0])//2, height//4 + (height//1.9 - instructionSize[1])//2, instructionSize[0], instructionSize[1])
    screen.blit(instructionText, instructionTitleRect)    

    # for displaying the quit game box
    quitRect = Rect(width//4, height//1.5, width//2, height//8)
    draw.rect(screen, GREY, quitRect)
    # Creating font
    string = "Quit Game"
    quitText = font1.render(string, 1, RED)
    quitSize = font1.size(string)
    quitTitleRect = Rect(width//4 + (width//2 - quitSize[0])//2, height//2 + (height//2.2- quitSize[1])//2, quitSize[0], quitSize[1])
    screen.blit(quitText, quitTitleRect)
    
    string = "ZOMBIE INVASION"
    titleText = font2.render(string, 1, RED)
    titleSize = font2.size(string)
    titleTitleRect = Rect(width//4 + (width//2 - titleSize[0])//2, height//6 + (height//400 - titleSize[1])//2, titleSize[0], titleSize[1])
    screen.blit(titleText, titleTitleRect)     

    if button == 1:
        if playRect.collidepoint(mouseX, mouseY) == True:
            st = GAMESTATE
        elif quitRect.collidepoint(mouseX, mouseY) == True:
            st = QUITSTATE
        elif instructionRect.collidepoint(mouseX,mouseY)==True:
            st = INSTRUCTIONSTATE
            
    display.flip()
    return st

def drawGame(button,x,y):
    global screen, width, height
    st = GAMESTATE   
    #screen.blit(floor,rect)
    if button == 3:
        st = MENUSTATE
        
    display.flip()
    return st

def drawInstruction(button, mouseX, mouseY):
    global screen, width, height
    st = INSTRUCTIONSTATE
    instruct = image.load('rpgbackground.jpg')
    instruct = transform.scale(instruct, (1000, 650))     
    rect2 = instruct.get_rect()
    back = image.load('backbutton.png')
    rect3 = back.get_rect()    
    rect3 = rect3.move((15, 510))
    screen.blit(instruct,rect2)
    screen.blit(back,rect3)      
    draw.rect(screen, GREY, (width//4, height//4, width//2, height//2))
    if rect3.collidepoint(mouseX,  mouseY) == True:
        st = MENUSTATE
        
    display.flip()
    return st      

state = MENUSTATE
mx = my = 0

# Game Loop
while running:
    button = 0
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            mx, my = evnt.pos          
            button = evnt.button        
        #screen.fill(Color('black'))  
        if evnt.type == KEYDOWN:
            if evnt.key == K_LEFT:
                KEY_LEFT = True
            if evnt.key == K_RIGHT:
                KEY_RIGHT = True
            if evnt.key == K_UP:
                KEY_UP = True
            if evnt.key == K_DOWN:
                KEY_DOWN = True
            if evnt.key == K_SPACE:
                moveBullet = True
                arrowMoveX = x
                arrowMoveY = y
        
        if evnt.type == KEYUP:
            if evnt.key == K_LEFT:
                KEY_LEFT = False
            if evnt.key == K_RIGHT:
                KEY_RIGHT = False
            if evnt.key == K_UP:
                KEY_UP = False
            if evnt.key == K_DOWN:
                KEY_DOWN = False           
            if evnt.key == K_SPACE:
                moveBullet = False
                
    #draw.rect(screen, BLACK, (0, 0, width, height)) 
    if state == MENUSTATE:
        state = drawMenu(button, mx, my) 
    elif state == GAMESTATE:
        if KEY_LEFT == True:
            #arrowMove = x
            x = x - 8
            count +=1   
            test = 48
            if count%test < test//3:
                drawing = drawMe4
            if count%test >= test/3 and count % test < 2*test//3:
                drawing = drawMe5
            if count%test >= 2*test//3:
                drawing = drawMe6
            if moveBullet == True:
                arrowMoveX -= 30
                bulletPic = bullet
            else:
                arrowMoveX = x
                bulletPic = bullet
            #drawScreen2(x,y)
        elif KEY_RIGHT == True:
            #arrowMove = x
            x = x + 8
            count +=1   
            test = 48
            if count%test < test//3:
                drawing = drawMe7
            if count%test >= test/3 and count % test < 2*test//3:
                drawing = drawMe8
            if count%test >= 2*test//3:
                drawing = drawMe9
            if moveBullet == True:
                arrowMoveX += 30 
                bulletPic = bullet
            else:
                arrowMoveX = x
                bulletPic = bullet
            #drawScreen3(x,y)
        elif KEY_UP == True:
            y = y - 8
            count +=1   
            test = 48
            if count%test < test//3:
                drawing = drawMe # drawing4 = drawMe10
            if count%test >= test/3 and count % test < 2*test//3:
                drawing = drawMe2 # drawing4 = drawMe11
            if count%test >= 2*test//3:
                drawing = drawMe3 # drawing4 = drawMe12
            if moveBullet == True:
                arrowMoveY += 30 
                bulletPic = bullet2
            else: 
                arrowMoveY = y
                bulletPic = bullet2
            #drawScreen(x,y)  
            if KEY_UP == False:
                arrowMoveY = y          
        elif KEY_DOWN == True:
            y = y + 8
            count +=1   
            test = 48
            if count%test < test//3:
                drawing = drawMe
            if count%test >= test/3 and count % test < 2*test//3:
                drawing = drawMe2
            if count%test >= 2*test//3:
                drawing = drawMe3
            if moveBullet == True:
                arrowMoveY += 30 
                bulletPic = bullet2
            else: 
                arrowMoveY = y
                bulletPic = bullet2
            
            if KEY_DOWN == False:
                arrowMoveY = y          
        else:
            drawing = drawMe
            arrowMove = x
            arrowMoveY = y
        if x >= 1000:
            x = 0
        elif x <= -30:
            x = 1000
        if y <= 125:
            y = 125
        elif y >= 560:
            y = 560
        if moveBullet == True:
            if arrowMoveY >=650 and arrowMoveY < 0 and arrowMoveX < 0 and arrowMoveX > 1000:
                moveBullet = False   
                arrowMoveX = x
                arrowMoveY = y
        if collisionGame == True: # Checks if collisionGame is true. If so, the loop will break.
            print ("COLLIDED")   
            break
        drawScreen(x,y)
        
    elif state == INSTRUCTIONSTATE:
        state = drawInstruction(button,mx,my)
    else:
        running = False                   
    display.flip()
    myClock.tick(60)

quit()


        