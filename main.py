from turtledemo.penrose import start

import pygame


def background(ground):
    maze = pygame.image.load(ground).convert()
    mask = pygame.mask.from_threshold(maze, (0, 0, 0, 255), (1, 1, 1, 255))
    return maze, mask


def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mizulina")
    clock = pygame.time.Clock()
    running = True

    pygame.mixer.init()
    pygame.mixer.music.load('sound/level_song.mp3')
    pygame.mixer.music.play(loops=-1, start=0.0)

    square_size = 30
    STEP = 5
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    player_img = pygame.image.load('skins/v1_sprite.png')
    player_img = pygame.transform.scale(player_img, (square_size, square_size))
    maze, mask = background('grounds/main_ground.png')

    square_x = 10
    square_y = 10
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()


        if mouse_pressed[0]:
            square_x = mouse_x - square_size // 2
            square_y = mouse_y - square_size // 2


        square_mask = pygame.Mask((square_size, square_size), fill=True)
        if mask.overlap(square_mask, (square_x, square_y)) is not None:
            square_x, square_y = 10, 10
        screen.fill(WHITE)
        screen.blit(maze, (0, 0))
        screen.blit(player_img, (square_x, square_y))


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
