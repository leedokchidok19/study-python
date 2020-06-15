import pygame # version : 1.9.6 - pip install pygame


# 초기화(반드시 필요)
pygame.init()

# 화면 크기 설정 (800 * 600) / (1280 * 720)
screen_width = 1280 # 가로 크기
screen_height = 720 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

current_path = os.path.dirname(__file__) # 현재 파일의 위치를 반환
image_path = os.path.join(current_path, "images") # 이미지 폴더 위치 반환

# 화면 타이틀 설정
gameName = 'Lombardia' # 게임 이름 - 롬바르디아
pygame.display.set_caption(gameName)
# 화면 아이콘
icon = pygame.image.load(os.path.join(image_path, 'icon.png'))
pygame.display.set_icon(icon)

# 이벤트 루프
# 게임이 진행 여부
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

# pygame 종료
pygame.quit()