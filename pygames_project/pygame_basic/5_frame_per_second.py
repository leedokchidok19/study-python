import pygame # pip install pygame
# FPS : 초당 프레임 수

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

# FPS : 초당 프레임 수
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load('studyPython/pygame_basic/background.png')

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load('studyPython/pygame_basic/character.png')
# 캐릭터 크기 가져오기
character_size = character.get_rect().size
#캐릭터 가로 크기
character_width = character_size[0]
# 캐릭터 세로 크기
character_height = character_size[1]
# 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_x_pos = (screen_width / 2) - (character_width / 2)
# 화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도 (fps에 상관 없이 동일한 속도를 내야한다.)
character_speed = 0.6

# 이벤트 루프
# 게임이 진행중인가?
running = True
while running:
    # 게임 화면의 초당 프레임 수를 설정 - clock.tick(프레임 수))
    dt = clock.tick(60)
    # 현재 프레임 수 구하기
    print('fps : '+ str(clock.get_fps()))

    # 캐릭터가 1초 동안에 100 만큼 이동을 해야함
    # 10 fps : 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동? 10만큼! 10 * 10 =100
    # 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼! 5 * 20 =100

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터 왼쪽
                to_x -= character_speed # to_x = to_x - 5 -> fps에 맞는 속도
            if event.key == pygame.K_RIGHT: # 캐릭터 오른쪽
                to_x += character_speed 
            if event.key == pygame.K_UP: # 캐릭터 위
                to_y -= character_speed 
            if event.key == pygame.K_DOWN: # 캐릭터 아래
                to_y += character_speed
        
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # 캐릭터 이동한 값을 전달
    character_x_pos += to_x * dt # fps에 맞게 이동 속도 변화
    character_y_pos += to_y * dt

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

    # 배경 그리기(이미지 파일, 좌표(왼쪽, 오른쪽)) 
    screen.blit(background, (0, 0))
    #캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    # 게임화면 다시 그리기 - 필수 없으면 이미지가 안 보인다.
    pygame.display.update()

# pygame 종료
pygame.quit()