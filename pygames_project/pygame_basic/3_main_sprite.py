import pygame # pip install pygame

# 캐릭터 이미지 생성

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

# 배경 이미지 불러오기
background = pygame.image.load('studyPython/pygames_project/pygame_basic/background.png')

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load('studyPython/pygames_project/pygame_basic/character.png')
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

# 이벤트 루프
# 게임이 진행중인가?
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
    
    # 배경 그리기(이미지 파일, 좌표(왼쪽, 오른쪽)) 
    screen.blit(background, (0, 0))
    #캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    # 게임화면 다시 그리기 - 필수 없으면 이미지가 안 보인다.
    pygame.display.update()

# pygame 종료
pygame.quit()