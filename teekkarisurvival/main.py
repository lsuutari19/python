"""
high level support for doing this and that.
"""
import pygame
import sys
import time
import random
import math

#initialize the pygame
pygame.init()

#creates the screen with (width, height)
screen = pygame.display.set_mode((800, 600))

#Title and logo
pygame.display.set_caption("Teekkari Survival")
icon = pygame.image.load('tgr.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('player.png')
playerX = 340
playerY = 400
pX_change = 0
pY_change = 0

#Enemies
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 400)
enemyY = random.randint(0, 140)
eX_change = 3
eY_change = 10

#lost
lostImg = pygame.image.load('lost.png')

#bg
bgImg = pygame.image.load('bg.png')

#draws the player character on screen
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def collision(eX, eY, pX, pY):
    distance = math.sqrt((math.pow(eX - pX, 2)) + (math.pow(eY - pY, 2)))
    if distance < 27:
        return True
    else:
        return False

#Game loop, makes sure the game is running, clicking the X closes the game window.
GAMEON = True
RUNNING = True
while RUNNING and GAMEON:
    #fills the background color - rgb values - Red, Green, Blue
    screen.fill((24,24,24))
    screen.blit(bgImg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        
        mods = pygame.key.get_mods()
        #checks if a key is pressed (for movement)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pX_change -= 3
            if event.key == pygame.K_RIGHT:
                pX_change += 3
            if event.key == pygame.K_UP:
                pY_change -= 3
            if event.key == pygame.K_DOWN:
                pY_change += 3

            if event.key == pygame.K_LEFT and (mods and pygame.KMOD_SHIFT):
                pX_change -= 5
            if event.key == pygame.K_RIGHT and (mods and pygame.KMOD_SHIFT):
                pX_change += 5
            if event.key == pygame.K_UP and (mods and pygame.KMOD_SHIFT):
                pY_change -= 5
            if event.key == pygame.K_DOWN and (mods and pygame.KMOD_SHIFT):
                pY_change += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pX_change = 0
                pY_change = 0
    
    playerY += pY_change
    playerX += pX_change

    #boundaries for player when moving
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 400:
        playerY = 400


    enemyY += eY_change
    enemyX += eX_change

    #enemy movement
    if enemyX <= 0:
        eX_change = 3
    elif enemyX >= 736:
        eX_change = -3
    elif enemyY <= 0:
        eY_change = 3
    elif enemyY >= 400:
        eY_change = -3
    
    #collision
    iscollision = collision(enemyX, enemyY, playerX, playerY)
    if iscollision:
        print("Lost")
        GAMEON = False
    enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()


