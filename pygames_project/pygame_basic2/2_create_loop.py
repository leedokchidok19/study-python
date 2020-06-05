import pygame
pygame.init()

display_width = 640  # 가로 길이
display_height = 480 # 세로 길이
# 화면 크기 설정
ourScreen = pygame.display.set_mode((display_width, display_height))

game_title = '파이썬 게임' # 게임명
pygame.display.set_caption(game_title)

finish = False
colorBlue = True

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # 스페이스 바를 누를 경우 색 변경
            colorBlue = not colorBlue

        if colorBlue:
            color = (0, 128, 255)
        else:
            color = (255, 255, 255)

        #사각형 그리기 draw.rect(화면크기, (rgb), 위치(x, y, width, height))
        pygame.draw.rect(ourScreen, color, pygame.Rect(0, 0, 60, 60))
        # 화면 업데이트 방법 2가지
        # pygame.display.update()
        pygame.display.flip()
