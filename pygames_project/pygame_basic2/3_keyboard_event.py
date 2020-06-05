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
x = 30 # x축 값
y = 30 # y축 값
clock = pygame.time.Clock()

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # 스페이스 바를 누를 경우 색 변경
            colorBlue = not colorBlue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3

        ourScreen.fill((0, 0, 0))

        if colorBlue:
            color = (0, 128, 255)
        else:
            color = (255, 255, 255)

        #사각형 그리기 draw.rect(화면크기, (rgb), 위치(x, y, width, height))
        pygame.draw.rect(ourScreen, color, pygame.Rect(x, y, 60, 60))
        # 화면 업데이트 방법 2가지
        # pygame.display.update()
        pygame.display.flip()
        #초당 프레임 tick(프레임 수)
        clock.tick(60)
