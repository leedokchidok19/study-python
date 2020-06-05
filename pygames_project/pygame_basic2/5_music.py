import pygame
pygame.init()
pygame.mixer.music.load('keithmitchell_forthemoment_320kbps') # https://www.soundclick.com/
pygame.mixer.music.play(0) # play(int) 재생 횟수

display_width = 640  # 가로 길이
display_height = 480 # 세로 길이
# 화면 크기 설정
ourScreen = pygame.display.set_mode((display_width, display_height))

game_title = '파이썬 게임' # 게임명
pygame.display.set_caption(game_title)

img = pygame.image.load('pygame_image.png')
def myimg(x, y):
    ourScreen.blit(img, (x, y))

x = (display_width * 0.5) # x축 값
y = (display_height * 0.5) # y축 값

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        ourScreen.fill((255, 255, 255))
        myimg(x, y)

        pygame.display.flip()
pygame.quit()
quit()
