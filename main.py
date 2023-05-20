import pygame

pygame.init()

FPS = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 800

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player_size = (20, 20)

player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_speed = [1, 1]

playing = True

while playing:
    FPS.tick(120)

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            playing = False

    main_display.fill(COLOR_BLACK)

    # if player_rect.bottom >= HEIGHT and player_speed == [1, 1]:
    #     player_speed = [1, -1]

    # if player_rect.bottom >= HEIGHT and player_speed == [-1, 1]:
    #     player_speed = [-1, -1]

    # if player_rect.right >= WIDTH and player_speed == [1, -1]:
    #     player_speed = [-1, -1]

    # if player_rect.right >= WIDTH and player_speed == [1, 1]:
    #     player_speed = [-1, 1]

    # if player_rect.top <= 0 and player_speed == [-1, -1]:
    #     player_speed = [-1, 1]

    # if player_rect.top <= 0 and player_speed == [1, -1]:
    #     player_speed = [1, 1]

    # if player_rect.left <= 0 and player_speed == [-1, 1]:
    #     player_speed = [1, 1]

    # if player_rect.left <= 0 and player_speed == [-1, -1]:
    #     player_speed = [1, -1]

    player_rect = player_rect.move(player_speed)

    if player_rect.bottom >= HEIGHT or player_rect.top <= 0:
        player_speed[1] = -player_speed[1]

    if player_rect.right >= WIDTH or player_rect.left <= 0:
        player_speed[0] = -player_speed[0]

    main_display.blit(player, player_rect)

    pygame.display.flip()