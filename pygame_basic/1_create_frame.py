import pygame # pip install pygame

# 프레임 생성

# 초기화(반드시 필요)
pygame.init()

# 화면 크기 설정
# 가로 크기
screen_width = 480
# 세로 크기
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
gameName = 'Nado Game Clone' # 게임 이름
pygame.display.set_caption(gameName)

# 이벤트 루프
# 게임이 진행중인가?
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

# pygame 종료
pygame.quit()