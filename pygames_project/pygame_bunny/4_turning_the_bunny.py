# 게임 예제 사이트 - https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python
# 캐릭터 회전시키기 - 마우스 위치
# 1 - Import library
import pygame
from pygame.locals import *
import math

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
# WASD. 배열의 각 항목은 하나의 키 (첫 번째는 W, 두 번째는 A 등)에 해당합니다.
# WASD. Each item in the array corresponds to one key – the first to W, the second to A and so on
keys = [False, False, False, False]
playerpos=[100,100]


# 3 - Load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load ("resources/images/grass.png")
castle = pygame.image.load ("resources/images/castle.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    for x in range(int(width/grass.get_width())+1):
        for y in range(int(height/grass.get_height())+1):
            screen.blit(grass,(x*100,y*100))
            screen.blit(castle,(0,30))
            screen.blit(castle,(0,135))
            screen.blit(castle,(0,240))
            screen.blit(castle,(0,345 ))

    # 6.1 - Set player position and rotation
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)

    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False

    # 9 - Move player
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
