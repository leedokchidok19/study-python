# coding=utf-8 < - 한글이 깨질 경우
import pygame
pygame.init()

display_width = 640  # 가로 길이
display_height = 480 # 세로 길이
# 화면 크기 설정
ourScreen = pygame.display.set_mode((display_width, display_height))

game_title = '파이썬 게임' # 게임명
pygame.display.set_caption(game_title)

finish = False

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        # 화면 업데이트 방법 2가지
        # pygame.display.update()
        pygame.display.flip()
