import os
import random
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

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load(os.path.join(image_path, 'background.png')) # 배경 만들기
character = pygame.image.load(os.path.join(image_path, 'character.png')) # 캐릭터 만들기
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = 0
character_y_pos = (screen_height / 2) - (character_height / 2)

# 적 만들기
enemy = pygame.image.load(os.path.join(image_path,'enemy.png'))
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint((screen_width / 2), screen_width - enemy_width) # randint(시작, 끝)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
# 게임이 진행 여부
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터 왼쪽
                to_x -= 5 # to_x = to_x - 5
            if event.key == pygame.K_RIGHT: # 캐릭터 오른쪽
                to_x += 5 
            if event.key == pygame.K_UP: # 캐릭터 위
                to_y -= 5 
            if event.key == pygame.K_DOWN: # 캐릭터 아래
                to_y += 5
        
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 캐릭터 이동한 값을 전달
    character_x_pos += to_x
    character_y_pos += to_y

    # 화면 밖으로 벗어나는 것을 방지
    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0)) # 배경 화면
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 (0, 가운데)
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 (랜덤, 0)

    pygame.display.update()
# pygame 종료
pygame.quit()